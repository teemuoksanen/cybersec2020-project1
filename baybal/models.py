from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	balance = models.IntegerField()

class Transaction(models.Model):
	user_from = models.TextField()
	user_to = models.TextField()
	message = models.TextField()
	amount = models.IntegerField()