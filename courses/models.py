from django.db import models

class Course(models.Model):#base class models.Model is inherited as it provides all the functionality to interact with the database
    name = models.CharField(max_length=255)
    language = models.CharField(max_length=200)
    price = models.FloatField()
    
    def __str__ (self):
        return self.name