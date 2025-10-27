from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    class Status(models.TextChoices):
        TODO = "TODO", "Todo"
        IN_PROGRESS = "IN_PROGRES", "In progress"
        DONE = "DONE", "Done"
        ARCHIVED = "ARCHIVED", "Archived"

    title = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=256)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.TODO
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "tasks"

    def __str__(self):
        return f"{self.title}"
