from django.db import models
from django.contrib.auth.models import User as AuthUser


class Setting(models.Model):
    class Theme(models.TextChoices):
        DARK = "DARK", "Dark"
        LIGHT = "LIGHT", "Light"

    class AccountType(models.TextChoices):
        FREE = "FREE", "Free"
        PRO = "PRO", "PRO"
        MAX = "MAX", "MAX"

    theme = models.CharField(max_length=20, choices=Theme.choices, default=Theme.LIGHT)

    account_type = models.CharField(
        max_length=20, choices=AccountType.choices, default=AccountType.FREE
    )

    auth_user = models.OneToOneField(
        AuthUser, on_delete=models.SET_NULL, blank=True, null=True
    )

    class Meta:
        db_table = "settings"

    def __str__(self):
        return (
            f"Settings for {self.auth_user.first_name if self.auth_user else 'No User'}"
        )
