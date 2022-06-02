"""zlom_bike URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from bike_app.views import StartView, OfferDetailView, CategoryContainView, UserRegistrationView, LoginView, \
    LogoutView, ResetPasswordView, UpdateUserView, AddOfferView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StartView.as_view(), name="start"),
    path('ogloszenia/<int:pk>/', OfferDetailView.as_view(), name="offer_detail"),
    path('kategoria/<slug:slug>', CategoryContainView.as_view(), name="category_content"),
    path('rejestracja/', UserRegistrationView.as_view(), name="registration"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('zmien_haslo/', ResetPasswordView.as_view(), name='reset_password'),
    path('zmien_dane/', UpdateUserView.as_view(), name='update_user'),
    path('dodaj_ogloszenie/', AddOfferView.as_view(), name='add_offer'),
]
