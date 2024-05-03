from django import forms

class CreditCardForm(forms.Form):
    name_on_card = forms.CharField(label='Name on Card', max_length=100)
    card_number = forms.CharField(label='Card Number', max_length=16)
    expiration_date = forms.DateField(label='Expiration Date')
    cvv = forms.CharField(label='CVV', max_length=3)
