from uuid import uuid4

from django.db import models


class BaseModelMixin(models.Model):
    """
    Abstract Model class creation and modification datetimes
    ['site', 'created', 'updated']
    """

    slug = models.SlugField(
        max_length=100, unique=True, db_index=True,
        default=uuid4, editable=False
    )

    created = models.DateTimeField(
        ("creation date and time"),
        editable=False,
        auto_now_add=True,)

    updated = models.DateTimeField(
        ("update date and time"),
        auto_now=True,
        editable=False
    )

    class Meta:
        abstract = True
