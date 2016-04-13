from django.db import models
from django.conf import settings
from pay.settings import *


class Sync(models.Model):
    "History of transaction sync runs"
    synced = models.DateTimeField(auto_now_add=True)


class BaseCustomer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    ### TODO

    class Meta:
        abstract = True

    def create_update_remote(self):
        pass

    def delete_remote(self):
        pass


class BasePaymentMethod(models.Model):
    "in Stripe it's Tokens"
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='payment_methods')
    ### TODO

    class Meta:
        abstract = True

    def create_update_remote(self):
        pass

    def delete_remote(self):
        pass


class BasePlan(models.Model):
    "in Braintree, you must create plans and re-enter their ID's here"
    "in Stripe you can use the API to manage plans"
    name = models.CharField(max_length=255)
    plan_ref = models.CharField()  # required and can only be created via braintree control panel
    ### TODO

    class Meta:
        abstract = True

    def create_update_remote(self):
        # No-op for braintree
        pass

    def delete_remote(self):
        # No-op for braintree
        pass


class BaseSubscription(models.Model):
    "in Stripe you can't specify an amount, it uses the plan amount"
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='subscriptions')
    plan = models.ForeignKey(PAY_PLAN_MODEL, related_name='subscriptions')
    payment_method = models.ForeignKey(PAY_PAYMENT_METHOD_MODEL, related_name='subscriptions', null=True, blank=True)
    ### TODO

    class Meta:
        abstract = True

    def create_remote(self):
        "Creates and commences subscription - including taking first charge, return the transaction"
        pass

    def update_remote(self, prorate=True, revert_on_fail=True):
        """
        Updates the subscription
        Stripe: 
            updates the subscription 
                if prorate=True, 
                    creates an invoice, 
                    creates the transaction & charges it
                    if it fails, and revert_on_fail=True
                        reverts the subscription to previous (hmmm how do I retrieve previous?)
        Braintree: 
            updates the subscription 
                passes prorate_charges, revert_subscription_on_proration_failure
                retrieve the transaction
        
        return proration transaction or True if prorate=False
        """

    def cancel_remote(self):
        pass


class BaseTransaction(models.Model):
    "in Stripe it's a Charge or Refund"
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='transactions')
    subscription = models.ForeignKey(PAY_SUBSCRIPTION_MODEL, related_name='transactions', null=True, blank=True)
    payment_method = models.ForeignKey(PAY_PAYMENT_METHOD_MODEL, related_name='transactions', null=True, blank=True)
    ### TODO

    class Meta:
        abstract = True

    def cancel_remote(self):
        "Cancel a pre-auth"
        pass

    def refund_remote(self):
        "Refund the transaction - creates a new transaction, returns it"
        pass

    def sale_remote(self, capture=True):
        "Create a sale/charge, or a preauth"
        pass

    def capture_remote(self):
        "Capture preauth funds"
        pass



class Customer(BaseCustomer):
    class Meta(BaseCustomer.Meta):
        swappable = 'PAY_CUSTOMER_MODEL'

class PaymentMethod(BasePaymentMethod):
    class Meta(BasePaymentMethod.Meta):
        swappable = 'PAY_PAYMENT_METHOD_MODEL'

class Plan(BasePlan):
    class Meta(BasePlan.Meta):
        swappable = 'PAY_PLAN_MODEL'

class Subscription(BaseSubscription):
    class Meta(BaseSubscription.Meta):
        swappable = 'PAY_SUBSCRIPTION_MODEL'

class Transaction(BaseTransaction):
    class Meta(BaseTransaction.Meta):
        swappable = 'PAY_TRANSACTION_MODEL'



