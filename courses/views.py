from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response 

from .serializers import CourseSerializer
from .models import Course

@api_view(['GET'])
def get_courses(request):
    Courses = Course.objects.all()#query sets 
    serializer = CourseSerializer(Courses,many=True)
    # print(Courses)
    # return Response({"products":serializer.data})
    return Response({"Courses":serializer.data})
    
