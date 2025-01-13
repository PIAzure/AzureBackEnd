from django.test import Client
from django.http import JsonResponse
from multipledispatch import dispatch
class UserScript:
    
    cliente=Client()
    
    def createuser(self,email:str,name:str,password:str,
                   imagefield:str,isadmin:bool=False)->JsonResponse:
        with open(file=imagefield,mode="rb") as f:
            data=self.cliente.post("/users/",data={"email":email,"name":name,
                                               "password":password,"imagefield":f,"isadmin":isadmin})
        return data.json()
    
    @dispatch()
    def getuser(self)->JsonResponse:
        data=self.cliente.get("/users/")
        return data.json()
    
    @dispatch(str)
    def getuser(self,email:str)->JsonResponse:
        data=self.cliente.get(f"/users/{email}")
        return data.json()
    