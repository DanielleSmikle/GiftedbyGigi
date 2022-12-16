from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.urls import reverse

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=255, unique=True, default='customer')

    def __str__(self):
        return self.name

class Collection(models.Model):
    name = models.CharField(max_length =255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, default='collection')

    class Meta:
        verbose_name_plural = 'collections'

    def get_absolute_url(self):
        return reverse('gigi:feature_detail', args=[self.slug])

    def __str__(self):
        return self.name

SIZE_CHOICES = (
    ('small', 'SMALL'),
    ('large', 'LARGE')
)
class Feature(models.Model):
    collection = models.ForeignKey(Collection, related_name='feature', on_delete=models.CASCADE)
    scent = models.CharField(max_length= 255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255, default='features')
    size = models.CharField(max_length=5, choices= SIZE_CHOICES, default='small')
    price = models.FloatField()
    in_stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    #image

    class Meta:
        verbose_name_plural= 'Features'
        ordering=('-created', )

    def get_absolute_url(self):
        return reverse('gigi:feature_detail', args=[self.slug])

    def __str__(self):
        return self.scent

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    feature= models.ForeignKey(Feature, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete= models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added= models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model): 
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    country= CountryField()
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    phone_number= models.CharField(max_length=15, blank= True)
    date_added= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
    







