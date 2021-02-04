from django.contrib import admin
from .models import Destination

# Register your models here.

# create superuser -> python manage.py createsuperuser

admin.site.register(Destination)
