# house_price_prediction/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_house_price, name='predict_house_price'),
]
