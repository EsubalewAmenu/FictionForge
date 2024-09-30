from django.core.management.base import BaseCommand
from trustcheck.models import Category, DataType

class Command(BaseCommand):
    help = 'Seed the database with initial categories and data types'

    def handle(self, *args, **kwargs):
        categories = [
            "Politics", "Science", "Economics", "Technology", "Health", "Education", 
            "Environment", "Business", "Social Issues", "Geopolitics"
        ]
        for category in categories:
            Category.objects.get_or_create(name=category)

        data_types = [
            "News Articles", "Scientific Research", "Statistics", "Public Statements", 
            "Multimedia Content", "Legal and Regulatory Documents", 
            "Reports & Whitepapers", "Financial Data"
        ]
        for data_type in data_types:
            DataType.objects.get_or_create(name=data_type)

        self.stdout.write(self.style.SUCCESS('Database seeded successfully'))
