import uuid

from django.db import models


class Service(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField(
        max_length=200,
        db_index=True,
        unique=True,
    )
    url = models.URLField(
        max_length=500,
        db_index=True,
        unique=True,
    )
    failure_threshold = models.PositiveIntegerField(
        default=5
    )
    reset_time = models.FloatField(
        default=30.0
    )
    created_at = models.DateTimeField(auto_now_add=True)
