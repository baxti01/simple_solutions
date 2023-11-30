from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

from simple_solutions import settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()

        username = settings.env('DJANGO_SUPERUSER_USERNAME')
        email = settings.env('DJANGO_SUPERUSER_EMAIL')
        password = settings.env('DJANGO_SUPERUSER_PASSWORD')

        if User.objects.filter(username=username).exists():
            print('Пользователь уже создан.')
        else:
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            print('Пользователь успешно создан!')
