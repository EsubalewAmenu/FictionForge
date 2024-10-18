import logging
from rest_framework import viewsets, permissions ,status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response



from django_comments.models import Comment
from django.contrib.contenttypes.models import ContentType
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404



from .models import Category, DataSubmission ,Evidence ,Verification , ReputationChange ,DataType 
from .serializers import CategorySerializer, DataSubmissionSerializer ,EvidenceSerializer ,VerificationSerializer ,ReputationChangeSerializer,DataTypeSerializer ,CommentSerializer, CommentCreateSerializer

logger = logging.getLogger(__name__)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class DataSubmissionViewSet(viewsets.ModelViewSet):
    queryset = DataSubmission.objects.all()
    serializer_class = DataSubmissionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class EvidenceViewSet(viewsets.ModelViewSet):
    queryset = Evidence.objects.all()
    serializer_class = EvidenceSerializer

    def create(self, request, *args, **kwargs):
        submission_id = request.data.get('submission')
        evidence_link = request.data.get('link')
        evidence_description = request.data.get('description')
        evidence_file = request.data.get('document')

        submission = get_object_or_404(DataSubmission, id=submission_id)

        existing_evidence = Evidence.objects.filter(
            submission=submission, 
            link=evidence_link, 
            document=evidence_file, 
            description__icontains=evidence_description
        ).first()

        if existing_evidence:
            # Evidence exists, add a vote
            existing_evidence.add_vote(request.user)
            return Response(
                {'message': 'You have voted on this existing evidence.'}, 
                status=status.HTTP_200_OK
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        evidence = serializer.instance
        evidence.add_vote(request.user)

        return Response(
            {'message': 'New evidence submitted and vote added.', 'evidence': serializer.data}, 
            status=status.HTTP_201_CREATED
        )

    @action(detail=True)
    def vote(self, request, pk=None):
        """Allow users to vote on evidence separately."""
        evidence = get_object_or_404(Evidence, pk=pk)
        evidence.add_vote(request.user)
        return Response({'message': 'Vote added to this evidence.'}, status=status.HTTP_200_OK)

    @action(detail=True)
    def unvote(self, request, pk=None):
        
        """Allow users to remove their vote."""
        evidence = get_object_or_404(Evidence, pk=pk)
        evidence.remove_vote(request.user)
        return Response({'message': 'Vote removed from this evidence.'}, status=status.HTTP_200_OK)
    
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