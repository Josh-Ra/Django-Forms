from django import forms


class AgeInForm(forms.Form):
    end = forms.IntegerField()
    birthyear = forms.IntegerField()


class HeyForm(forms.Form):
    name = forms.CharField()

class OrderTotalForm(forms.Form):
    burgers = forms.IntegerField()
    fries = forms.IntegerField()
    drinks = forms.IntegerField()
