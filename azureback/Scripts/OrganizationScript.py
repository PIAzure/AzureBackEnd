from django.test import Client
from django.http import JsonResponse
class OrganizationScript:
    
    cliente=Client()
    
    def createorganization(self,name:str)->JsonResponse:
        pass
    
    def getorganization(self)->JsonResponse:
        pass
    
    def getorganization(self,email:str)->JsonResponse:
        pass        
