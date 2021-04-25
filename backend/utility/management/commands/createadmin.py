from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import logging


class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.count() == 0:
            username = 'admin'
            email = 'raunakritesh14@gmail.com'
            password = 'admin'
            admin = User.objects.create_superuser(email=email, username=username, password=password)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
            print("Created Admin User")