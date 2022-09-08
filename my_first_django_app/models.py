from django.db import models

# Create your models here.

# ORM --> Object Relational Mapping
# takes python objects and stores them in db

# Model for To-Do app
# Inherit from Model
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        # This is equivalent to object.toString() in Java
        # Gives a human-readable representation of the object
        return self.name


class Task(models.Model):
    content = models.TextField()
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    completed_at = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    class TaskStatus(models.TextChoices):  # This is enumeration
        COMPLETED = "CO", "COMPLETED"
        PENDING = "PE", "PENDING"
        DROPPED = "DR", "DROPPED"

    status = models.CharField(
        choices=TaskStatus.choices,
        default=TaskStatus.PENDING,
        max_length=2,
    )  # The choices must be restricted

    @property
    def foo(self):
        return "Hello"

    def __str__(self):
        return f'{self.content} - {self.get_status_display()}'

    def get_status_display(self):
        pass

# Relationship between Task and Tag
# 1 task can have 1/more tags and 1 tag can have 1/more tasks
# Hence a Many-To-Many relationship exists
