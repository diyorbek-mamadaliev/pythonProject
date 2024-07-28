from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    USER = (
        (1, 'HOD'),
    )

    user_type = models.CharField(choices=USER,max_length=50, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')

class Product(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    class Meta:
        verbose_name = 'Maxsulot'
        verbose_name_plural = 'Maxsulotlar'

class SoldItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_sold = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    sold_at = models.DateTimeField(auto_now_add=True)
    PAYMENT_CHOICES = [
        ('cash', 'Naqd'),
        ('card', 'Karta'),
        ('online', 'Nasiya'),
    ]
    payment_type = models.CharField(max_length=20, choices=PAYMENT_CHOICES, blank=True, null=True)

    def product_name(self):
        return self.product.name

    product_name.short_description = 'Product Name'
    class Meta:
        verbose_name = 'Sotilgan Maxsulot'
        verbose_name_plural = 'Sotilgan Maxsulotlar'

    def get_payment_type_display(self):
        return dict(self.PAYMENT_CHOICES).get(self.payment_type, self.payment_type)

