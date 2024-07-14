from django.db import models
from django.contrib.auth.models import User

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vendor_name = models.CharField(max_length=255)
    details = models.TextField()
    website_url = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        app_label = 'vendors' 

class Product(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    pdf_document = models.FileField(upload_to='pdf_documents/', blank=True)
    # Add other product fields as needed

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'vendors'


class VendorProduct(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.vendor.user.username} - {self.product.name}"

    class Meta:
        unique_together = ('vendor', 'product')
        app_label = 'vendors'
