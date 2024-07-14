from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Vendor, Product
from .forms import VendorRegistrationForm, VendorLoginForm, ProductForm, ContactForm
import os

def index(request):
    return render(request, 'vendors/index.html')

def about(request):
    return render(request, 'vendors/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Handle the contact form submission (e.g., send an email)
            # For simplicity, we'll just redirect to a thank you page
            return redirect('contact_thank_you')
    else:
        form = ContactForm()
    return render(request, 'vendors/contact.html', {'form': form})

def contact_thank_you(request):
    return render(request, 'vendors/contact_thank_you.html')

def vendor_register(request):
    if request.method == 'POST':
        form = VendorRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            vendor = Vendor(
                user=user,
                vendor_name=form.cleaned_data['vendor_name'],
                details=form.cleaned_data['details'],
                website_url=form.cleaned_data['website_url'],
                profile_picture=form.cleaned_data['profile_picture']
            )
            vendor.save()
            return redirect('product_list')
    else:
        form = VendorRegistrationForm()
    return render(request, 'vendors/register.html', {'form': form})

def vendor_login(request):
    if request.method == 'POST':
        form = VendorLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('product_list')
    else:
        form = VendorLoginForm()
    return render(request, 'vendors/login.html', {'form': form})

@login_required
def vendor_logout(request):
    logout(request)
    return redirect('vendor_login')

@login_required
def product_list(request):
    products = Product.objects.filter(vendor=request.user.vendor)
    return render(request, 'vendors/product_list.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor  # Assuming vendor is associated with user
            product.save()
            return redirect('product_list')  
    else:
        form = ProductForm()
    
    context = {
        'form': form,
    }
    return render(request, 'vendors/product_create.html', context)

@login_required
def view_pdf(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if product.pdf_document:
        with open(product.pdf_document.path, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(product.pdf_document.name)
            return response
    else:
        return HttpResponse("No PDF file available.")
