from django import forms
from .models import MenuItem, Order


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['table','items','status']

        weights = {
            'items':forms.CheckboxSelectMultiple(),
        }