from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, DataSubmissionViewSet ,EvidenceViewSet ,VerificationViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'data-submissions', DataSubmissionViewSet)
router.register(r'evidences', EvidenceViewSet)
router.register(r'evidences', VerificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
