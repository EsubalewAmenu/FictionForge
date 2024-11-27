from django.urls import path
from .views import PersonaListView, QueryView

urlpatterns = [
    path('personas/', PersonaListView.as_view(), name='persona-list'),
    path('query/', QueryView.as_view(), name='query'),
]
