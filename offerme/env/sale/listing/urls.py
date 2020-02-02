from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.IndexView, name="index"),
    path('additem/', views.listing_create, name="index"),
    path('listing/<slug:slug>/', views.listingdetail, name='detail'),
    


]
