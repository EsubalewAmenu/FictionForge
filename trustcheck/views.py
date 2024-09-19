from rest_framework import viewsets
from .models import Category, DataSubmission ,Evidence ,Verification , ReputationChange
from .serializers import CategorySerializer, DataSubmissionSerializer ,EvidenceSerializer ,VerificationSerializer ,ReputationChangeSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializnoba
    er_class = CategorySerializer

class DataSubmissionViewSet(viewsets.ModelViewSet):
    queryset = DataSubmission.objects.all()
    serializer_class = DataSubmissionSerializer
    
class EvidenceViewSet(viewsets.ModelViewSet):
    queryset = Evidence.objects.all()
    serializer_class = EvidenceSerializer
    
class VerificationViewSet(viewsets.ModelViewSet):
    queryset = Verification.objects.all()
    serializer_class = VerificationSerializer

class ReputationChangeViewSet(viewsets.ModelViewSet):
    queryset = ReputationChange.objects.all()
    serializer_class = ReputationChangeSerializer

