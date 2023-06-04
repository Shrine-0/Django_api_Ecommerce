from azure.storage.blob import BlobServiceClient
from django.conf import settings


def check_azure_connection(connection_string):
    try:
        
        #create a blob service client using the connection string
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        
        #list the containers in the storage account
        container = blob_service_client.list_containers()
        for conatiners in container:
            print(conatiners.name)
        
        #if the containers are listed then the connection is successful
        return True
    
    except Exception as e :
         return False
        
        