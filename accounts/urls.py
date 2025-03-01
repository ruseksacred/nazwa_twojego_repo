from django.urls import path
from . import views
from .views import user_login

urlpatterns = [
    path('register/', views.register, name='register'),
    path("login/", user_login, name="login"),
]
