from django.test import Client
from django.http import JsonResponse
class EventScript:
    
    cliente=Client()
    
    def createevent(self,name:str)->JsonResponse:
        pass
    
    def getevent(self)->JsonResponse:
        pass
    
    def getevent(self,email:str)->JsonResponse:
        pass        