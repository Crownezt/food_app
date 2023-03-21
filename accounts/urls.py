from django.urls import path

from accounts import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name="sign_up")
]