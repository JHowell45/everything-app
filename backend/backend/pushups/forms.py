from django import forms
from pygments.lexer import default


class PushupForm(forms.Form):
    body_weight: float = forms.FloatField(label="weight", min_value=50)
    amount: int = forms.IntegerField(label="amount", min_value=0)
    on_knees: bool = forms.BooleanField(label="on knee", required=False)
