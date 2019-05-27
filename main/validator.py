from django.core.exceptions import ValidationError

def validate_number(value):
		if not (str(value).isdigit()) and len(str(value)) != 10:
			raise ValidationError("Invalid Phone Number")