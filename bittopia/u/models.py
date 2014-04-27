from django.db import models

from django.core.validators import *

# Create your models here.

class User(models.Model):

	# Inherent Qualities
	name = models.CharField(max_length=40)

	MALE = 'M'
	FEMALE = 'F'
	GENDER_CHOICES = ((MALE, 'Male'), (FEMALE, 'Female'))

	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

	age = models.IntegerField(default=1)

	ASTURIAN = 'A'
	BREEBLE = 'B'
	CLEMISH = 'C'
	DOJOJO = 'D'
	ETHNICITY_CHOICES = ((ASTURIAN, 'Asturian'), (BREEBLE, 'Breeble'), (CLEMISH, 'Clemish'), (DOJOJO, 'Dojojo'))

	ethnicity = models.CharField(max_length=3, choices=ETHNICITY_CHOICES)

	nationality = models.CharField(max_length=40, default='Bittopia')

	occupation = models.CharField(max_length=40, default='Unemployed')

	# Variable Qualities
	health = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(100.0)], default = 100.0)

	hunger = models.BooleanField(default=False)

	happiness = models.FloatField(default=0.0)