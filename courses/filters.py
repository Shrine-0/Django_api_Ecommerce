from django_filters import rest_framework as filters
from .models import Course

class Courses_Filter(filters.FilterSet):
    
    keyword = filters.CharFilter(field_name="name",lookup_expr='icontains')#icontains is used to search for the keyword in the name of the course
    min_price = filters.NumberFilter(field_name="price" or 0,lookup_expr='gte')#gte is greater than or equal to
    max_price = filters.NumberFilter(field_name="price" or 1000000,lookup_expr="lte")#lte is less than or equal to
    
    class Meta:
        
        model = Course
        fields = ("keyword","category","price","min_price","max_price")