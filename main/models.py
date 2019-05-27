from django.db import models
from django.core.exceptions import ValidationError
from .validator import validate_number

# Create your models here.
class Register(models.Model):
	email = models.EmailField(primary_key=True)
	phone_number = models.CharField(max_length=10, validators=[validate_number])

	def __str__(self):
		return self.email
