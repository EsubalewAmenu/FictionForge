# Generated by Django 5.0 on 2024-08-17 12:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trustcheck', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(help_text='Provide a brief description of the evidence.')),
                ('link', models.URLField(blank=True, help_text='Optional URL link to the evidence.', null=True)),
                ('document', models.FileField(blank=True, help_text='Optional file upload for the evidence.', null=True, upload_to='evidences/')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Timestamp when the evidence was created.')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evidences', to='trustcheck.datasubmission')),
            ],
            options={
                'verbose_name': 'Evidence',
                'verbose_name_plural': 'Evidences',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ReputationChange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change', models.IntegerField(help_text='Amount of reputation points changed. Positive for gains, negative for losses.')),
                ('reason', models.TextField(help_text='Description of the reason for the reputation change.')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Timestamp when the reputation change was recorded.')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reputation Change',
                'verbose_name_plural': 'Reputation Changes',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.BooleanField(help_text='Indicates if the data is valid (True) or invalid (False).')),
                ('staked_tokens', models.DecimalField(decimal_places=2, default=0.0, help_text='Amount of tokens staked on the verification.', max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Timestamp when the verification was created.')),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verifications', to='trustcheck.datasubmission')),
            ],
            options={
                'verbose_name': 'Verification',
                'verbose_name_plural': 'Verifications',
                'ordering': ['-created_at'],
            },
        ),
    ]