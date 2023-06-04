from django.conf import settings
# from azure.storage.blob import BlockBlobService
from storages.backends.azure_storage import AzureStorage
import os
# from settings import AZURE_ACCOUNT_NAME, AZURE_ACCOUNT_KEY

class AzureMediaStorage(AzureStorage):
    
    account_name = os.getenv("AZURE_ACCOUNT_NAME")
    account_key = os.getenv("AZURE_ACCOUNT_KEY")
    azure_container = 'media'
    expiration_secs = None
    # az_storage = AzureStorage()   
    # az_url = az_storage.url(blob_name,parameters={"content_type" : "text/html;"})

class AzureStaticStorage(AzureStorage):
    account_name = os.getenv("AZURE_ACCOUNT_NAME")
    account_key = os.getenv("AZURE_ACCOUNT_KEY")
    azure_container = 'static'
    expiration_secs = None