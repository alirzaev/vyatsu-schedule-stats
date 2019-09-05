from django.core.validators import URLValidator
from django.db import models


class Source(models.Model):
    TYPES = (('API', 'API server'), ('BOT', 'Telegram bot'))

    url = models.CharField(
        max_length=200,
        validators=[URLValidator(schemes=['mongodb'])]
    )

    name = models.CharField(max_length=50)

    source_type = models.CharField(choices=TYPES, max_length=3)

    def __str__(self):
        return self.name
