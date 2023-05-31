from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .filters import Courses_Filter 

from .serializers import CourseSerializer
from .models import Course

@api_view(['GET'])
def get_courses(request):
     
    filterset = Courses_Filter(request.GET,queryset=Course.objects.all().order_by('id'))#queryset is the data that is to be filtered 
    count = filterset.qs.count()#count is the total no of data by id shown in the page 
    
    #Pagination
    resPerpage = 3 # number of results per page
    paginator = PageNumberPagination() # function to paginate the results
    paginator.page_size = resPerpage
    
    queryset = paginator.paginate_queryset(filterset.qs,request)# qs is the filtered data that is to be paginated
    
    # Courses = Course.objects.all()#query sets 
    
    serializer = CourseSerializer(queryset,many=True)
    
    # print(Courses)
    # return Response({"products":serializer.data})
    return Response({
        "count":count,
        "resPerpage":resPerpage,
        "Courses":serializer.data
        })


@api_view(['GET'])
def get_course(request,pk): #pk is the primary key of the course
    
    Courses_pk = get_object_or_404(Course,id=pk)# if the course is not found then it will return a 404 error
    
    serializers = CourseSerializer(Courses_pk,many=False) 
    
    return Response({"Courses":serializers.data})#data is the data that is to be sent to the frontend


