from django.conf import settings
from django.core.files.base import File
# from azure.storage.blob import BlockBlobService
from storages.backends.azure_storage import AzureStorage
from django.core.files.storage import Storage
import os
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient,BlobClient,ContainerClient

from Django_api.settings import AZURE_ACCOUNT_NAME, AZURE_ACCOUNT_KEY
from django.utils.deconstruct import deconstructible


class AzureMediaStorage(AzureStorage):  
    account_name = os.getenv("AZURE_ACCOUNT_NAME")
    # print(account_name)
    account_key = os.getenv("AZURE_ACCOUNT_KEY")
    # print(account_key)
    azure_container = 'media/'
    expiration_secs = None
    # az_storage = AzureStorage()   
    # az_url = az_storage.url(blob_name,parameters={"content_type" : "text/html;"})


class AzureStaticStorage(AzureStorage):
    account_name = os.getenv("AZURE_ACCOUNT_NAME")
    # print(account_name)
    account_key = os.getenv("AZURE_ACCOUNT_KEY")
    # print(account_key)
    azure_container = 'static/'
    expiration_secs = None


@deconstructible
class AzureBlobStorage_SAS(Storage):
    def __init__ (self,account_url,sas_token,container_name):
        self.account_url =account_url
        self.sas_token = sas_token
        self.container_name = container_name
        self.blob_service_client = BlobServiceClient(account_url=self.account_url,credential=self.sas_token)
        self.container_client = self.blob_service_client.get_container_client(self.container_name)

    def _open(self,name,mode='rb'):
        blob_client = self.container_client.get_blob_client(name)
        return blob_client.download_blob().readinto()

    def _save(self,name,content):
        blob_client = self.container_client.get_blob_client(name)
        blob_client.upload_blob(content,overwrite = True)
        return name
    
    def exists(self, name):
        blob_client = self.container_client.get_blob_client(name)
        return blob_client.exists()
    
    def url(self, name):
        blob_client = self.container_client.get_blob_client(name)
        return blob_client.url