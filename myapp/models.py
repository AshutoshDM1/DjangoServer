from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField()
    age = models.IntegerField(max_digits=4, null=True)

