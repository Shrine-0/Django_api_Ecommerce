from django.contrib import admin
from .models import Course#we import the model Course from models.py

admin.site.register(Course)#registering the model with the admin site

