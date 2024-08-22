from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, DataSubmissionViewSet ,EvidenceViewSet ,VerificationViewSet,ReputationChangeViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'data-submissions', DataSubmissionViewSet)
router.register(r'evidences', EvidenceViewSet)
router.register(r'verifications', VerificationViewSet)
router.register(r'reputaion-changes', ReputationChangeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
