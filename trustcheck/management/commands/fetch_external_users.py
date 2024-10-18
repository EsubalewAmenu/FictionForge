import requests
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from trustcheck.models import ExternalUser
import environ
import sys, os
from pathlib import Path


env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent.parent  
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


class Command(BaseCommand):
    help = 'Fetch external users and store in database'
    def handle(self, *args, **kwargs):
        api_key = str(env('X_API_KEY')) 
        com_id = str(env('COM_ID'))
        api_url = str(env('EXTERNAL_USER_API_URL'))

        url = api_url
        headers = {
            'x-api-key': api_key,
            'com-id': com_id
        }

        user_ids = [6, 13, 19]  # Example user IDs
        response = requests.get(url, headers=headers, json={"ids": user_ids})

        if response.status_code == 200:
            users_data = response.json()
            for user_data in users_data:
                user_id = user_data['user']
                mpxr_value = user_data['mpxr']

                user = User.objects.filter(id=user_id).first()
                if not user:
                    username = f'user_{user_id}' 
                    user = User.objects.create(username=username)
                
                external_user, ext_created = ExternalUser.objects.get_or_create(user=user)
                external_user.mpxr = mpxr_value
                external_user.save()
        else:
            self.stdout.write(f"Error fetching users: {response.status_code}")
