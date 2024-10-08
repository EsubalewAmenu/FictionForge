from rest_framework import viewsets
from .models import Category, DataSubmission ,Evidence ,Verification , ReputationChange ,DataType
from .serializers import CategorySerializer, DataSubmissionSerializer ,EvidenceSerializer ,VerificationSerializer ,ReputationChangeSerializer,DataTypeSerializer

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

class ReputationChangeViewSet(viewsets.ModelViewSet):
    queryset = ReputationChange.objects.all()
    serializer_class = ReputationChangeSerializer

class DataTypeViewSet(viewsets.ModelViewSet):
    queryset = DataType.objects.all()
    serializer_class = DataTypeSerializer