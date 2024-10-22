"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mainapp.viewsets import guest_view, room_view, transaction_view

router = DefaultRouter()

router.register(r'guests', guest_view.GuestsViewSet, basename='guests')
router.register(r'rooms', room_view.RoomsViewSet, basename='rooms')
router.register(r'transactions', transaction_view.TransactionsViewSet, basename='transactions')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
]
