from django.conf import settings

CUSTOMER_MODEL       = getattr(settings, 'PAY_CUSTOMER_MODEL', 'pay.Customer')
PAYMENT_METHOD_MODEL = getattr(settings, 'PAY_PAYMENT_METHOD_MODEL', 'pay.PaymentMethod')
PLAN_MODEL           = getattr(settings, 'PAY_PLAN_MODEL', 'pay.Plan')
SUBSCRIPTION_MODEL   = getattr(settings, 'PAY_SUBSCRIPTION_MODEL', 'pay.Subscription')
TRANSACTION_MODEL    = getattr(settings, 'PAY_TRANSACTION_MODEL', 'pay.Transaction')
