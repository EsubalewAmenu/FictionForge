# trustcheck/management/commands/seed_data.py

from django.core.management.base import BaseCommand
from trustcheck.models import Category, DataType

class Command(BaseCommand):
    help = 'Clear the database and seed with initial categories, subcategories, and data types'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Starting database reset and seeding process...'))
        self.clear_existing_data()
        self.seed_categories()
        self.seed_data_types()
        self.stdout.write(self.style.SUCCESS('Database reset and seeding completed successfully.'))

    def clear_existing_data(self):
        """
        Deletes all existing Category and DataType entries.
        """
        self.stdout.write(self.style.WARNING('Clearing existing data...'))

        # Delete DataType entries first to handle hierarchical relationships
        data_type_count = DataType.objects.count()
        DataType.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'Deleted {data_type_count} DataType entries.'))

        # Delete Category entries
        category_count = Category.objects.count()
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'Deleted {category_count} Category entries.'))

    def seed_categories(self):
        """
        Seeds the database with predefined categories and their subcategories.
        """
        self.stdout.write(self.style.WARNING('Seeding Categories...'))

        categories = {
            "Politics": [
                "Election Results",
                "Legislation",
                "Political Parties",
                "Government Officials",
                "International Relations"
            ],
            "Science": [
                "Climate Data",
                "Environmental Studies",
                "Space Exploration",
                "Biomedical Research",
                "Physics & Chemistry"
            ],
            "Economics": [
                "Financial Markets",
                "Trade Data",
                "Employment Statistics",
                "Inflation & GDP",
                "Cryptocurrency"
            ],
            "Technology": [
                "AI & Machine Learning",
                "Cybersecurity",
                "Blockchain",
                "Software Development",
                "Emerging Technologies"
            ],
            "Health": [
                "Medical Research",
                "Epidemics & Pandemics",
                "Public Health Policies",
                "Nutrition Data",
                "Pharmaceutical Studies"
            ],
            "Education": [
                "Academic Research",
                "Student Performance Data",
                "Online Learning Platforms",
                "Curriculum Studies",
                "Education Policies"
            ],
            "Environment": [
                "Climate Change",
                "Deforestation Data",
                "Wildlife Conservation",
                "Water Resources",
                "Pollution Statistics"
            ],
            "Business": [
                "Corporate Earnings",
                "Industry Trends",
                "Startups & Innovation",
                "Market Research",
                "Mergers & Acquisitions"
            ],
            "Social Issues": [
                "Human Rights",
                "Gender Equality",
                "Social Justice Movements",
                "Migration Data",
                "Poverty & Welfare"
            ],
            "Geopolitics": [
                "Territorial Disputes",
                "International Sanctions",
                "Global Conflicts",
                "Diplomatic Relations",
                "Military Expenditure"
            ]
        }

        for category_name, subcategory_names in categories.items():
            # Create main category
            category, created = Category.objects.get_or_create(name=category_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'  Created Category: {category_name}'))
            else:
                self.stdout.write(self.style.NOTICE(f'  Category already exists: {category_name}'))

            # Create subcategories for this category
            for subcategory_name in subcategory_names:
                subcategory, sub_created = Category.objects.get_or_create(
                    name=subcategory_name,
                    parent=category
                )
                if sub_created:
                    self.stdout.write(self.style.SUCCESS(f'    Created Subcategory: {subcategory_name}'))
                else:
                    self.stdout.write(self.style.NOTICE(f'    Subcategory already exists: {subcategory_name}'))

    def seed_data_types(self):
        """
        Seeds the database with predefined data types and their sub-data-types.
        """
        self.stdout.write(self.style.WARNING('Seeding Data Types...'))

        data_types = {
            "News Articles": [
                "Online News Reports",
                "Print Media Articles",
                "Broadcast News Summaries",
                "Press Releases",
                "Editorials & Opinion Pieces"
            ],
            "Scientific Research": [
                "Peer-Reviewed Journal Papers",
                "Research Studies",
                "Experimental Data",
                "Lab Reports",
                "Meta-Analysis & Reviews"
            ],
            "Statistics": [
                "Government Reports",
                "Surveys & Polls",
                "Economic Data (e.g., GDP, Unemployment)",
                "Demographic Data",
                "Industry & Market Statistics"
            ],
            "Public Statements": [
                "Political Speeches",
                "Official Announcements",
                "Interviews & Press Conferences",
                "Social Media Posts from Verified Sources",
                "Legal Documents (e.g., court rulings, laws)"
            ],
            "Multimedia Content": [
                "Video Clips (e.g., news segments, interviews)",
                "Audio Recordings (e.g., podcasts, public statements)",
                "Photographs (e.g., events, protests)",
                "Infographics & Charts"
            ],
            "Legal and Regulatory Documents": [
                "Court Decisions",
                "Legislative Bills & Acts",
                "Regulatory Reports",
                "International Treaties"
            ],
            "Reports & Whitepapers": [
                "Government Reports",
                "NGO Studies",
                "Corporate Whitepapers",
                "Policy Briefs"
            ],
            "Financial Data": [
                "Stock Market Reports",
                "Company Earnings Statements",
                "Investment Reports",
                "Budget Statements"
            ]
        }

        for data_type_name, subdata_type_names in data_types.items():
            # Create main data type
            data_type, dt_created = DataType.objects.get_or_create(name=data_type_name)
            if dt_created:
                self.stdout.write(self.style.SUCCESS(f'  Created DataType: {data_type_name}'))
            else:
                self.stdout.write(self.style.NOTICE(f'  DataType already exists: {data_type_name}'))

            # Create sub-data-types
            for subdata_type_name in subdata_type_names:
                subdata_type, sub_dt_created = DataType.objects.get_or_create(
                    name=subdata_type_name,
                    parent=data_type
                )
                if sub_dt_created:
                    self.stdout.write(self.style.SUCCESS(f'    Created Sub-DataType: {subdata_type_name}'))
                else:
                    self.stdout.write(self.style.NOTICE(f'    Sub-DataType already exists: {subdata_type_name}'))
