from django.urls import path, include
from . import views




urlpatterns = [
    path('osoby/', views.osoby),
    path('osoba/get/<int:pk>/', views.osoba_get),
    path('osoba/update/<int:pk>/', views.osoba_update),
    path('osoba/delete/<int:pk>/', views.osoba_delete),
    path('osoba/create/', views.osoba_create),
    path('stanowiska/', views.stanowiska),
    path('stanowisko/get/<int:pk>/', views.stanowisko_get),
    path('stanowisko/update/<int:pk>/', views.stanowisko_update),
    path('stanowisko/delete/<int:pk>/', views.stanowisko_delete),
    path('stanowisko/create/', views.stanowisko_create),
    path('stanowisko/<int:pk>/members/', views.stanowisko_members),


]