from django.urls import path
from . import views

urlpatterns = [
    path("", views.fiction_list, name="fiction_list"),
    path('<int:pk>/', views.fiction_detail, name='fiction_detail'),
    path('health/', views.health_check, name='health_check'),  # health check endpoint
]