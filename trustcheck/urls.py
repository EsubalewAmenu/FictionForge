from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
 CategoryViewSet,
 DataTypeViewSet, 
 DataSubmissionViewSet,
 EvidenceViewSet,
 VerificationViewSet,
 ReputationChangeViewSet
 )

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'data-types', DataTypeViewSet)
router.register(r'data-submissions', DataSubmissionViewSet)
router.register(r'evidences', EvidenceViewSet)
router.register(r'verifications', VerificationViewSet)
router.register(r'reputaion-changes', ReputationChangeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # login and logout views for the browsable API
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
