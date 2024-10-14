
from django.core.management.base import BaseCommand
from trustcheck.models import Category, DataType

class Command(BaseCommand):
    help = 'Clear the database by deleting all Category and DataType entries.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Starting database clearing process...'))
        self.clear_existing_data()
        self.stdout.write(self.style.SUCCESS('Database clearing completed successfully.'))

    def clear_existing_data(self):
        """
        Deletes all existing Category and DataType entries.
        """
        self.stdout.write(self.style.WARNING('Clearing existing DataType entries...'))
        data_type_count = DataType.objects.count()
        DataType.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'Deleted {data_type_count} DataType entries.'))

        self.stdout.write(self.style.WARNING('Clearing existing Category entries...'))
        category_count = Category.objects.count()
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'Deleted {category_count} Category entries.'))
