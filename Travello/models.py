from django.db import models

# Create your models here.

# Model migration command
# 1-> python manage.py makemigrations
# 2-> python manage.py sqlmigrate Travello migration_number
# 3-> python manage.py migrate


class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
