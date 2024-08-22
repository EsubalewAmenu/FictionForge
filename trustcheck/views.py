from rest_framework import viewsets
from .models import Category, DataSubmission ,Evidence ,Verification
from .serializers import CategorySerializer, DataSubmissionSerializer ,EvidenceSerializer ,VerificationSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class DataSubmissionViewSet(viewsets.ModelViewSet):
    queryset = DataSubmission.objects.all()
    serializer_class = DataSubmissionSerializer
    
class EvidenceViewSet(viewsets.ModelViewSet):
    queryset = Evidence.objects.all()
    serializer_class = EvidenceSerializer
    
class VerificationViewSet(viewsets.ModelViewSet):
    queryset = Verification.objects.all()
    serializer_class = VerificationSerializer