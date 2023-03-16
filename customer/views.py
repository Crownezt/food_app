from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def buy_food(request):
    return HttpResponse("Thank you for patronizing")


def rate_food(request):
    return HttpResponse("Thank you for the feedback")


def contact(request):
    return render(request, 'customer/contact.html')
