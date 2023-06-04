from azure.storage.blob import BlobServiceClient
from django.conf import settings


def check_azure_connection(connection_string):
    contain = []
    try:
        
        #create a blob service client using the connection string
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        
        #list the containers in the storage account
        container = blob_service_client.list_containers()
        for containers in container:
            print(containers.name)
            contain.append(containers.name)
            print(contain)
        # for i , v in enumerate(contain):
        #     dictionary [i] 
        #if the containers are listed then the connection is successful
        return True,contain
    
    except Exception as e :
         return False
        
        