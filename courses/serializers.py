from rest_framework import serializers
from .models import Course

 #this class converts query sets to json
 
class CourseSerializer(serializers.ModelSerializer):
     class Meta: #meta class is a must for all serializers
         model = Course
         fields = "__all__" #all the fields of the model are to be serialized
        #  fields = ['id','name','category','language','price','description','ratings','user']