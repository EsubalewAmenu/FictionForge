from django.core.management.base import BaseCommand
from trustcheck.models import Category, DataType

class Command(BaseCommand):
    help = 'Seed the database with initial categories, subcategories, and data types'

    def handle(self, *args, **kwargs):
        # Seed Categories and Subcategories
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
            category, _ = Category.objects.get_or_create(name=category_name)
            # Create subcategories for this category
            for subcategory_name in subcategory_names:
                Category.objects.get_or_create(name=subcategory_name, parent=category)

        # Seed Data Types
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

        for data_type_name, descriptions in data_types.items():
            data_type, _ = DataType.objects.get_or_create(name=data_type_name)

        self.stdout.write(self.style.SUCCESS('Database seeded successfully'))
