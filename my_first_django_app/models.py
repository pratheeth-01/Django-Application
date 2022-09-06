from django.db import models


# Create your models here.

# ORM --> Object Relational Mapping
# takes python objects and stores them in db

# Model for To-Do app
# Inherit from Model
class Tag(models.Model):
    name = models.CharField(max_length=250)


class Task(models.Model):
    content = models.TextField()
    deadline = models.DateTimeField()
    created_at = models.DateTimeField()
    completed_at = models.DateTimeField()
    tags = models.ManyToManyField(Tag)

    class TaskStatus(models.TextChoices):  # This is enumeration
        COMPLETED = "CO", "COMPLETED"
        PENDING = "PE", "PENDING"
        DROPPED = "DR", "DROPPED"

    status = models.CharField(
        choices=TaskStatus.choices,
        default=TaskStatus.PENDING,
        max_length=2,
    )  # The choices must be restricted

# Relationship between Task and Tag
# 1 task can have 1/more tags and 1 tag can have 1/more tasks
# Hence a Many-To-Many relationship exists
