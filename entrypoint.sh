#!/bin/sh

# Wait for the database to be ready (if you're using a service like PostgreSQL or MySQL)
# Uncomment and adjust the following line if necessary
# sleep 10

# Run migrations and create superuser if it doesn't exist
python manage.py makemigrations
python manage.py migrate

echo "Creating superuser..."
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'password123')" | python manage.py shell
echo "Superuser created."

python manage.py seed_data

# Start the Django development server
python manage.py runserver 0.0.0.0:8080
