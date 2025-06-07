from django import forms
from .models import Product

# Form based on Product model
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity']


# What’s happening:
# ModelForm automatically creates a form from your Product model.

# fields defines which fields will be shown in the form.