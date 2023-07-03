from django import forms
from .models import Address
from django.forms import Select, TextInput


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address', 'area', 'city']
        widgets = {
            'address': TextInput(attrs={'class': 'form-control form-control-sm',
                                        'placeholder': 'Example : 2nd Floor , H#224, R#06'}),
            'area': TextInput(attrs={'class': 'form-control form-control-sm',
                                     'placeholder': 'Example : Dhanmondi'}),
            'city': TextInput(attrs={'class': 'form-control form-control-sm',
                                     'placeholder': 'Example : Dhaka'}),
        }
