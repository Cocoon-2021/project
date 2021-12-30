from django.urls import path
from prtest import views

urlpatterns = [
    path('', views.home),
    path('details', views.detail)
]
