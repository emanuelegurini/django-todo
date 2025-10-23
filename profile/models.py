from django.db import models
from django.contrib.auth.models import User as AuthUser


class Profile(models.Model):
    auth_user = models.OneToOneField(
        AuthUser, 
        on_delete=models.CASCADE,
        related_name='profile'
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    #email = models.EmailField(max_length=254, unique=True)

    class Meta:
        db_table = "profiles"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
