from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=256)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")

    class Meta:
        db_table = "projects"
