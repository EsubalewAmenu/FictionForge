from rest_framework import serializers
from django_comments.models import Comment
from .models import Category, DataSubmission , Evidence , Verification , ReputationChange ,DataType

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  
    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'comment',
            'submit_date',
            'is_public',
        ]
        read_only_fields = ['id', 'user', 'submit_date', 'is_public']
        
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
        read_only_fields = ['id', 'user', 'created_at', 'updated_at', 'is_verified']

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'content_type',
            'object_pk', 
            'comment',
            'user_name',
            'user_email',
            'user_url',
        ]

    def validate(self, attrs):
        if not self.context['request'].user.is_authenticated:
            if not attrs.get('user_name'):
                raise serializers.ValidationError("Name is required for anonymous comments.")
        return attrs

    def create(self, validated_data):
        request = self.context['request']
        user = request.user if request.user.is_authenticated else None
        comment = Comment.objects.create(
            content_type=validated_data['content_type'],
            object_pk=validated_data['object_pk'], 
            comment=validated_data['comment'],
            user=user,
            user_name=validated_data.get('user_name', ''),
            user_email=validated_data.get('user_email', ''),
            user_url=validated_data.get('user_url', ''),
            site_id=1  
        )
        return comment

        
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
