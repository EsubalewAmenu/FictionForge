from django.contrib import admin
from .models import Category, DataSubmission, Evidence, Verification, ReputationChange, ExternalUser, DataType, Comment
from django_comments.admin import CommentsAdmin

@admin.register(ExternalUser)
class ExternalUserAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'mpxr')

    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'description')
    search_fields = ('name',)
    list_filter = ('parent',)

@admin.register(DataSubmission)
class DataSubmissionAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'category', 'is_verified', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('category', 'is_verified', 'created_at')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    


@admin.register(Evidence)
class EvidenceAdmin(admin.ModelAdmin):
    list_display = ('submission', 'description', 'link', 'document', 'created_at')
    search_fields = ('description', 'submission__title')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': ('submission', 'description', 'link', 'document', 'created_at')
        }),
    )

@admin.register(Verification)
class VerificationAdmin(admin.ModelAdmin):
    list_display = ('submission', 'vote', 'staked_tokens', 'created_at')
    search_fields = ('submission__title',)
    list_filter = ('vote', 'created_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': ('submission', 'vote', 'staked_tokens', 'created_at')
        }),
    )

@admin.register(ReputationChange)
class ReputationChangeAdmin(admin.ModelAdmin):
    list_display = ('user', 'change', 'reason', 'created_at')
    search_fields = ('user__username', 'reason')
    list_filter = ('change', 'created_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': ('user', 'change', 'reason', 'created_at')
        }),
    )


@admin.register(DataType)
class DataTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)
    
admin.site.unregister(Comment)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content_type', 'object_pk', 'user', 'comment', 'submit_date', 'is_public', 'is_removed')
    list_filter = ('is_public', 'is_removed', 'submit_date', 'content_type')
    search_fields = ('comment', 'user__username', 'user_email')