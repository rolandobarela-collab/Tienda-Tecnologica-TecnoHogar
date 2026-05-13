#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
cd tecnohogar
python manage.py collectstatic --no-input
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@tecnohogar.com', 'admin123')" | python manage.py shell
