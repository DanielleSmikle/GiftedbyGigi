from django.shortcuts import render
from .models import *


def all_features(request):
    features = Feature.objects.all()
    return render(request, 'gigi/home.html', {'features': features})
