from rest_framework import serializers
from .models import Category, DataSubmission , Evidence

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class DataSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSubmission
        fields = '__all__'
class EvidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evidence
        fields = '__all__'
        