from django import forms
from .models import Subscription


class subForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = "__all__"
