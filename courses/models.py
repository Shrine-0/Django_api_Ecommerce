from django.db import models
# from django.utils.text import TextChoices
from django.contrib.auth.models import User
from Django_api.custom_storage.custom_azure import AzureBlobStorage_SAS
from Django_api.settings import ACCOUNT_URL,AZURE_ACCOUNT_NAME,AZURE_ACCOUNT_KEY


AMS  =  AzureBlobStorage_SAS()

class Category (models.TextChoices):
    AI ="AI(Artificial Intelligence)",
    ML ="ML(Machine Learning)",
    Graphics = "Graphics/Vfx",
     

#maintained locally by postgresql 
class Course(models.Model):#base class models.Model is inherited as it provides all the functionality to interact with the database
    name = models.CharField(max_length=255,default="",blank= False)#CharField is used to store strings
    category =  models.CharField(max_length =200,choices = Category.choices,default = Category.AI) 
    language = models.CharField(max_length=200,default = "JAVA")
    price = models.DecimalField(max_digits = 6,decimal_places =2,default = 0)
    description = models.TextField(max_length=500,default='')
    ratings =  models.DecimalField(max_digits = 2,decimal_places =1,default = 0)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.name
    




#maintained by azure blob storage or cloud
class CoursesImages(models.Model):
    
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null =True,related_name='images')
    image = models.ImageField(default = 'default.jpg',storage= AMS,upload_to = "media") 