from django import forms

from .models import CreditProduct


class CreditProductForm(forms.ModelForm):

    class Meta:
        model = CreditProduct
        fields = '__all__'