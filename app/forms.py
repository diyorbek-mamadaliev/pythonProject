from django import forms
from .models import Product, SoldItem


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'image']

class SellProductForm(forms.Form):
    quantity_sold = forms.IntegerField(label='Soni')
    comment = forms.CharField(label='Izoh', widget=forms.Textarea, required=False)
    PAYMENT_CHOICES = [
        ('cash', 'Naqd'),
        ('card', 'Karta'),
        ('online', 'Nasiya'),
    ]
    payment_type = forms.ChoiceField(choices=PAYMENT_CHOICES, label='To\'lov turi')

class SoldItemForm(forms.ModelForm):
    class Meta:
        model = SoldItem
        fields = ['payment_type']
        labels = {
            'payment_type': 'Toʻlov turi',
        }


