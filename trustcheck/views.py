from rest_framework import viewsets, permissions
from django_comments.models import Comment
from django.contrib.contenttypes.models import ContentType

from .models import Category, DataSubmission ,Evidence ,Verification , ReputationChange ,DataType 
from .serializers import CategorySerializer, DataSubmissionSerializer ,EvidenceSerializer ,VerificationSerializer ,ReputationChangeSerializer,DataTypeSerializer ,CommentSerializer, CommentCreateSerializer

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
    

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['create']:
            return CommentCreateSerializer
        return CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user if self.request.user.is_authenticated else None)