from django import forms


class PushupForm(forms.Form):
    body_weight: float = forms.FloatField(label="weight", min_value=50)
    amount: int = forms.IntegerField(label="amount", min_value=0)
