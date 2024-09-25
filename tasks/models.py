from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    finish_mark = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["-finish_mark", "-datetime"]
