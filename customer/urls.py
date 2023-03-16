from django.urls import path
from . import views

urlpatterns = {
    path('buyfood/', views.buy_food, name='buy_food'),
    path('ratefood/', views.rate_food, name='rate_food'),
    path('contact/', views.contact, name='contact')
    # path('contact/', views.contact, name='')
}
