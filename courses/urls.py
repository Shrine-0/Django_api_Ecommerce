from django.urls import path,include 
from . import views

urlpatterns = [
 path('courses/',views.get_courses,name="courses"),
 path('courses/upload_images/',views.upload_courses_images,name="upload_course_images"),
 path('courses/connection_checker/',views.connectioncheker,name="connection_checker"),
 path('courses/<str:pk>',views.get_course,name="get_course details"),
]
 