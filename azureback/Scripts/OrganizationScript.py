from django.test import Client
from django.http import JsonResponse
from multipledispatch import dispatch
class OrganizationScript:
    
    __cliente=Client()
    
    def createorganization(self,email:str,name:str,password:str,
                   imagefield:str,isadmin:bool=False)->JsonResponse:
        with open(file=imagefield,mode="rb") as f:
            data=self.__cliente.post("/organization/",data={"email":email,"name":name,
                                               "password":password,"imagefield":f,"isadmin":isadmin})
        return data.json()
    
    @dispatch()
    def getorganization(self)->JsonResponse:
        data=self.__cliente.get("/organization/")
        return data.json()
    
    @dispatch(str)
    def getorganization(self,email:str)->JsonResponse:
        data=self.__cliente.get(f"/organization/{email}")
        return data.json()   
