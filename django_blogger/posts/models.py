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

    type = models.PositiveIntegerField(choices=Type.choices, default=Type.TEXT)
    content = models.TextField(blank=True, default='')

    group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.PROTECT, related_name='posts')
    labels = models.ManyToManyField(Label, blank=True, related_name='posts')

    def __str__(self):
        return self.title or super().__str__()



class PostChangeLog(models.Model):
    post = models.ForeignKey(Post, related_name='logs', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created = models.DateTimeField(blank=True, default=timezone.localtime)
    # by = models.ForeignKey(User, )

    def __str__(self):
        return self.title or super().__str__()