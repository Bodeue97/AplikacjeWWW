from django.urls import path
from . import views

urlpatterns = [
    path('osoby/', views.OsobyList.as_view()),
    path('osoba/get/<int:pk>/', views.OsobaDetail.as_view()),
    path('osoba/update/<int:pk>/', views.OsobaDetail.as_view()),
    path('osoba/delete/<int:pk>/', views.OsobaDetail.as_view()),
    path('osoba/create/', views.OsobyList.as_view()),
    path('stanowiska/', views.StanowiskoList.as_view()),
    path('stanowisko/get/<int:pk>/', views.StanowiskoDetail.as_view()),
    path('stanowisko/update/<int:pk>/', views.StanowiskoDetail.as_view()),
    path('stanowisko/delete/<int:pk>/', views.StanowiskoDetail.as_view()),
    path('stanowisko/create/', views.StanowiskoList.as_view()),
]
