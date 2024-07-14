from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Vendor, Product

class VendorRegistrationForm(UserCreationForm):
    vendor_name = forms.CharField(max_length=255)
    details = forms.CharField(widget=forms.Textarea)
    website_url = forms.URLField(required=False)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'vendor_name', 'details', 'website_url', 'profile_picture']

class VendorLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ProductForm(forms.ModelForm):
    vendors = forms.ModelMultipleChoiceField(queryset=Vendor.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'pdf_document', 'vendors']

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Message'}))

