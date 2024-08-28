from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL, related_name='subcategories'
    )
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class DataSubmission(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Data Submission"
        verbose_name_plural = "Data Submissions"

    def __str__(self):
        return self.title


class Evidence(models.Model):
    submission = models.ForeignKey(
        'DataSubmission',
        on_delete=models.CASCADE,
        related_name='evidences'
    )
    user = models.ForeignKey(
        User,  
        on_delete=models.CASCADE
    )
    description = models.TextField(
        help_text="Provide a brief description of the evidence."
    )
    link = models.URLField(
        blank=True,
        null=True,
        help_text="Optional URL link to the evidence."
    )
    document = models.FileField(
        upload_to='evidences/',
        blank=True,
        null=True,
        help_text="Optional file upload for the evidence."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the evidence was created."
    )

    class Meta:
        verbose_name = "Evidence"
        verbose_name_plural = "Evidences"
        ordering = ['-created_at']

    def __str__(self):
        return f"Evidence for '{self.submission.title}'"


class Verification(models.Model):
    submission = models.ForeignKey(
        'DataSubmission',
        on_delete=models.CASCADE,
        related_name='verifications'
    )
    user = models.ForeignKey(
        User,  
        on_delete=models.CASCADE
    )
    vote = models.BooleanField(
        help_text="Indicates if the data is valid (True) or invalid (False)."
    )
    staked_tokens = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.0,
        help_text="Amount of tokens staked on the verification."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the verification was created."
    )

    class Meta:
        verbose_name = "Verification"
        verbose_name_plural = "Verifications"
        ordering = ['-created_at']

    def __str__(self):
        return f"Verification on '{self.submission.title}'"


class ReputationChange(models.Model):
    user = models.ForeignKey(
        User,  
        on_delete=models.CASCADE
    )
    change = models.IntegerField(
        help_text="Amount of reputation points changed. Positive for gains, negative for losses."
    )
    reason = models.TextField(
        help_text="Description of the reason for the reputation change."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the reputation change was recorded."
    )

    class Meta:
        verbose_name = "Reputation Change"
        verbose_name_plural = "Reputation Changes"
        ordering = ['-created_at']

    def __str__(self):
        return f"Reputation change for {self.user.username}: {self.change} points"


