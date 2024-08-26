from django import forms

from tasktest2.models import Shop


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'
