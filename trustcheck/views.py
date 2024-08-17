from rest_framework import viewsets
from .models import Category, DataSubmission
from .serializers import CategorySerializer, DataSubmissionSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # Optionally, add permissions or custom methods here

class DataSubmissionViewSet(viewsets.ModelViewSet):
    queryset = DataSubmission.objects.all()
    serializer_class = DataSubmissionSerializer
    # Optionally, add permissions or custom methods here
