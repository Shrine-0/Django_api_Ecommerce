from django.contrib import admin
from django.urls import path,include
from .utils.error_view import handler404,handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('courses.urls')),
    path('transac/',include('transaction.urls')),
]

handler404
handler500