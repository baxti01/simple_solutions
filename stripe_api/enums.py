from django.db import models


class RatesType(models.TextChoices):
    USD = 'usd'
    EUR = 'eur'
