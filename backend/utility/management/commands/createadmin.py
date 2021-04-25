from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings
import logging


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            if User.objects.count() == 0:
                username = settings.ADMIN_USER_NAME
                email = 'raunakritesh14@gmail.com'
                password = settings.ADMIN_PASSWORD
                admin = User.objects.create_superuser(email=email, username=username, password=password)
                admin.is_active = True
                admin.is_admin = True
                admin.save()
                logging.info("Created Admin User")
        except Exception as e:
            logging.warning("Not creating admin user - {}".format(e))
