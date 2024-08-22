from rest_framework import serializers
from .models import Category, DataSubmission , Evidence , Verification , ReputationChange

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
        
class VerificationSerializer(serializers.ModelSerializer):
     class Meta:
         model = Verification
         ields = '__all__'
         
class ReputationChangeSerializer(serializers.ModelSerializer):
     class Meta:
         model = ReputationChange
         ields = '__all__'