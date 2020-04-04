from django.urls import path, re_path
from core import views


urlpatterns = [
    path('', views.index),
    path('vacancies/<int:pk>/', views.show_vacancy)
]