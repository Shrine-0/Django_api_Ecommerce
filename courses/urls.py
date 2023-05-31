from django.urls import path,include
from . import views

urlpatterns = [
 path('courses/',views.get_courses,name="courses"),
 path('courses/<str:pk>',views.get_course,name="get_course details")
]
