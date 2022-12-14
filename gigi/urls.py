from django.urls import path
from . import views

app_name = 'gigi'

urlpatterns = [
    path('', views.all_features, name='all_features'), 
    path('item/<slug:slug>/', views.feature_detail, name='feature_detail'),

]