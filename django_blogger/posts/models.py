from django.db import models
from django.utils import timezone


class Label(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name or super().__str__()


class Group(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name or super().__str__()


class Post(models.Model):
    title = models.CharField(max_length=255, blank=True)
    slug = models.CharField(max_length=255, null=True, unique=True)
    private = models.BooleanField(blank=True, default=False)
    created = models.DateTimeField(blank=True, default=timezone.localtime)

    class Type(models.IntegerChoices):
        TEXT = 1, 'Text'
        MD = 2, 'Markdown'
        HTML = 3, 'HTML'

    type = models.PositiveIntegerField(default=Type.TEXT, choices=Type.choices)

    group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.PROTECT)
    labels = models.ManyToManyField(Label, blank=True)

