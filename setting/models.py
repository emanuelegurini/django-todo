from django.db import models

class Setting(models.Model): 

	class Theme(models.TextChoices):
		DARK = "DARK", "Dark"
		LIGHT = "LIGHT", "Ligth"

	class AccountType(models.TextChoices):
		FREE = "FREE", "Free"
		PRO = "PRO", "PRO" 
		MAX = "MAX", "MAX"

	theme = models.CharField(
		max_length=20,
		choices=Theme.choices, 
		default=Theme.LIGHT 
	)

	account_type = models.CharField(
		max_length=20,
		choices=AccountType.choices, 
		default=AccountType.FREE 
	)

	class Meta:
		db_table = "settings"

