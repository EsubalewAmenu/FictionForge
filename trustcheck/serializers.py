from rest_framework import serializers
from django_comments.models import Comment
from .models import Category, DataSubmission , Evidence , Verification , ReputationChange ,DataType

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class DataSubmissionSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)  

    class Meta:
        model = DataSubmission
        fields = [
            'id',
            'user',
            'title',
            'content',
            'category',
            'data_type',
            'created_at',
            'updated_at',
            'is_verified',
            'comments',  
        ]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'content_type',
            'object_pk',
            'site',
            'user',
            'user_name',
            'user_email',
            'comment',
            'submit_date',
            'ip_address',
            'is_public',
            'is_removed',
        ]
        read_only_fields = ['submit_date', 'ip_address', 'is_public', 'is_removed']

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment']
        
class EvidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evidence
        fields = '__all__'
        
class VerificationSerializer(serializers.ModelSerializer):
     class Meta:
         model = Verification
         fields = '__all__'
         
class ReputationChangeSerializer(serializers.ModelSerializer):
     class Meta:
         model = ReputationChange
         fields = '__all__'
         

class DataTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataType
        fields = '__all__'
