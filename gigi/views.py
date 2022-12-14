from django.shortcuts import get_object_or_404, render
from .models import Customer, Collection, Feature, Order, OrderItem, ShippingAddress 

def collections(request):
    return {
        'collections': Collection.objects.all()
    }
def all_features(request):
    features = Feature.objects.all()
    return render(request, 'gigi/home.html', {'features': features})

def feature_detail(request,slug):
    feature = get_object_or_404(Feature, slug=slug, in_stock=True)
    return render(request, 'gigi/features/detail.html', {'feature': feature})
