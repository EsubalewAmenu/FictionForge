from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, DataSubmissionViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'data-submissions', DataSubmissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
