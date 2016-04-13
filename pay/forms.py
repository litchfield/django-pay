from django import forms


class CreditCardForm(forms.Form):
    "Form with credit card details"


class PaymentMethodForm(CreditCardForm, forms.ModelForm):
    "Create/update a payment method, which can be used for subscriptions/transactions"


class TransactionForm(CreditCardForm, forms.ModelForm):
    "Create transaction"


