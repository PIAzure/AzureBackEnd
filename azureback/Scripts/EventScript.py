from django.test import Client
from django.http import JsonResponse
from multipledispatch import dispatch

class EventScript:
    
    __cliente=Client()
    
    def createevent(self,description:str,location:str,begin:str,banner:str,organizator:str,
                    max_particpant:int,end:str,max_voluntary_per_horary:int,bscale:str,escale:str)->JsonResponse:
        with open(banner,mode="rb") as f:
            data=self.__cliente.post("/events/",data={"description":description,"location":location,
                                                 "begin":begin,"banner":f,"max_particpant":max_particpant,"end":end,
                                                 "max_voluntary_per_horary":max_voluntary_per_horary,"bscale":bscale,"escale":escale})
        return data.json()
    
    @dispatch(int)
    def getevent(self,idevent:int)->JsonResponse:
        data=self.__cliente.get(f"/events/event/organizator/{idevent}")
        return data.json()
    
    @dispatch(str)
    def getevent(self,email:str)->JsonResponse:
        data=self.__cliente.get(f"/events/event/organizator/{email}")
        return data.json()
    