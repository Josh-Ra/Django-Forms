from django import forms


class Warmup2Form(forms.Form):
    word = forms.CharField()
    number = forms.IntegerField()


class Logic2Form(forms.Form):
    number1 = forms.IntegerField()
    number2 = forms.IntegerField()
    number3 = forms.IntegerField()


class String2Form(forms.Form):
    word = forms.CharField()


class List2Form(forms.Form):
    Number0 = forms.IntegerField()
    Number1 = forms.IntegerField()
    Number2 = forms.IntegerField()
    Number3 = forms.IntegerField()
    Number4 = forms.IntegerField(required=False)
    Number5 = forms.IntegerField(required=False)
    Number6 = forms.IntegerField(required=False)
