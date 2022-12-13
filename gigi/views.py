from django.shortcuts import render
from .models import Customer, Collection, Feature, Order, OrderItem, ShippingAddress 

def collections(request):
    return {
        'collections': Collection.objects.all()
    }
def all_features(request):
    features = Feature.objects.all()
    return render(request, 'gigi/home.html', {'features': features})
