from django.urls import path
from . import views

urlpatterns = [
   path('grandexchange', views.get_ge_prices, name='restaurant data json'),
]