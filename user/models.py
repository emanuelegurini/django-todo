from django.db import models

class User(models.Model): 
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.CharField(unique=True)

	class Meta:
		db_table = 'users'

	def __str__(self):
		return f"{self.first_name} {self.last_name}"
