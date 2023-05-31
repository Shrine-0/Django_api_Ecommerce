from django.http import JsonResponse

def handler404(request,exception):
    message = "Route not resolved"
    response  = JsonResponse(data={"Error_message":message})
    response.status_code = 404
    return response

def handler500(request): 
    message = "Internal server error"
    response = JsonResponse(data={'Error_message':message})
    response.status_code =500
    return response