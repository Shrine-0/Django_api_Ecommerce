
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import exception_handler
from http import HTTPStatus 


def custom_exception_handler(exc,context):#exc is exception both built in or custom exception context gives how where and what made the error
    
    response = exception_handler(exc,context)

    print(f'reponse: {response}')
    
    if response != None : 
        http_code_to_message  = {v.value :v.description for v in HTTPStatus}
        error_payload = {
            'error':{
                'status_code' : 0,
                'messages':'',
                'details':[]
            }
        }
        error  = error_payload['error']
        status_code  = response.status_code
        
        error['status_code'] = status_code
        error['messages'] = http_code_to_message[status_code]
        error['details']= response.data
        
        response.data = error_payload
        # print("WOWWWWW")
        # print(i for i in response.data)
        
        
        return response
    else: 
        error={
            'error':'Something went wrong please reload'
        }
        return Response(error,status=status.HTTP_500_INTERNAL_SERVER_ERROR)