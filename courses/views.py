from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from Django_api.custom_storage.azure_utils import check_azure_connection
from Django_api.custom_storage.custom_azure import AzureMediaStorage as AMS
from django.conf import settings
from Django_api.settings import AZURE_CONNECTION_STRING

from .filters import Courses_Filter 

from .serializers import CourseSerializer
from .models import Course

@api_view(['GET'])
def get_courses(request):
    
    #filter by order or id  
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


@api_view(['POST'])
def connectioncheker(request):
    # connection = check_azure_connection(AZURE_CONNECTION_STRING)
    # print(connection)
    # print(AMS.check())
    return Response({"Container":check_azure_connection(AZURE_CONNECTION_STRING)})


@api_view(['POST'])
def upload_courses_images(request):
    
    data = request.data
    
    files = request.FILES.getlist('images')
    if files is  None:
       return Response(Exception("No files found"))

    print("data", data )
    print('files',files)
    
    return Response({"message":"Image was uploaded successfully"})


