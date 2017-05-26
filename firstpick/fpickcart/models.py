from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Cart(models.Model):
	user_id = models.CharField(max_length=200)
	product_id = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=10, decimal_places=2)

