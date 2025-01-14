from datetime import datetime
from django.test import Client
import sys
import django
import os



# Configura o caminho do projeto Django
sys.path.append(f'/home/guilherme/Azure/AzureBackEnd/azureback')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'azureback.settings')

# Inicializa o Django
django.setup()

from EventScript import EventScript
from UserScript import UserScript
from OrganizationScript import OrganizationScript


def createusersseed(userapi):
    userapi.createuser(email="usuario1@gmail.com",name="usuário1",password="12345678",imagefield="./ImagesSeed/perfil.jpeg")
    userapi.createuser(email="usuario2@gmail.com",name="usuário2",password="12345678",imagefield="./ImagesSeed/perfil.jpeg")
    userapi.createuser(email="usuario3@gmail.com",name="usuário3",password="12345678",imagefield="./ImagesSeed/perfil.jpeg")
    
        

def createorgevent(eventapi,orgapi):
    organizator1=organizationapi.createorganization(email="usuario4@gmail.com",name="usuário4",password="12345678",imagefield="ImagesSeed/perfil.jpeg")
    organizator2=organizationapi.createorganization(email="usuario5@gmail.com",name="usuário5",password="12345678",imagefield="ImagesSeed/perfil.jpeg")
    organizator3=organizationapi.createorganization(email="usuario6@gmail.com",name="usuário6",password="12345678",imagefield="ImagesSeed/perfil.jpeg")
    
    #create events organizator 1    
    eventapi.createevent(description="Evento 1",location="Anfitearo da UTFPR",organizator="usuario4@gmail.com",
                         banner="ImagesSeed/perfil.jpeg",max_particpant=10,max_voluntary_per_horary=5,
                         escale="2024-11-20T20:24:00Z",begin="2024-11-20T11:24:00Z",bscale="2024-11-20T20:24:00Z",end="2024-11-21T20:24:00Z")
    
    eventapi.createevent(description="Evento 2",location="Anfitearo da UTFPR",organizator="usuario4@gmail.com",
                         banner="ImagesSeed/perfil.jpeg",max_particpant=10,max_voluntary_per_horary=5,
                         escale="2024-11-21T20:24:00Z",begin="2024-11-21T11:24:00Z",bscale="2024-11-21T20:24:00Z",end="2024-11-22T20:24:00Z")
    eventapi.createevent(description="Evento 3",location="Anfitearo da UTFPR",organizator="usuario4@gmail.com",
                         banner="ImagesSeed/perfil.jpeg",max_particpant=10,max_voluntary_per_horary=5,
                         escale="2024-11-20T23:24:00Z",begin="2024-11-23T11:24:00Z",bscale="2024-11-23T20:24:00Z",end="2024-11-24T20:24:00Z")
    
    #create events organizator 2
    eventapi.createevent(description="Evento 1",location="Anfitearo da UTFPR",organizator="usuario5@gmail.com",
                         banner="ImagesSeed/perfil.jpeg",max_particpant=10,max_voluntary_per_horary=5,
                         escale="2024-11-20T20:24:00Z",begin="2024-11-20T11:24:00Z",bscale="2024-11-20T20:24:00Z",end="2024-11-21T20:24:00Z")
    eventapi.createevent(description="Evento 2",location="Anfitearo da UTFPR",organizator="usuario5@gmail.com",
                         banner="ImagesSeed/perfil.jpeg",max_particpant=10,max_voluntary_per_horary=5,
                         escale="2024-11-21T20:24:00Z",begin="2024-11-21T11:24:00Z",bscale="2024-11-21T20:24:00Z",end="2024-11-22T20:24:00Z")
    eventapi.createevent(description="Evento 3",location="Anfitearo da UTFPR",organizator="usuario5@gmail.com",
                         banner="ImagesSeed/perfil.jpeg",max_particpant=10,max_voluntary_per_horary=5,
                         escale="2024-11-20T23:24:00Z",begin="2024-11-23T11:24:00Z",bscale="2024-11-23T20:24:00Z",end="2024-11-24T20:24:00Z")
    
    #create events orgnizator 3
    eventapi.createevent(description="Evento 1",location="Anfitearo da UTFPR",organizator="usuario6@gmail.com",
                         banner="ImagesSeed/perfil.jpeg",max_particpant=10,max_voluntary_per_horary=5,
                         escale="2024-11-20T20:24:00Z",begin="2024-11-20T11:24:00Z",bscale="2024-11-20T20:24:00Z",end="2024-11-21T20:24:00Z")
    eventapi.createevent(description="Evento 2",location="Anfitearo da UTFPR",organizator="usuario6@gmail.com",
                         banner="ImagesSeed/perfil.jpeg",max_particpant=10,max_voluntary_per_horary=5,
                         escale="2024-11-21T20:24:00Z",begin="2024-11-21T11:24:00Z",bscale="2024-11-21T20:24:00Z",end="2024-11-22T20:24:00Z")
    eventapi.createevent(description="Evento 3",location="Anfitearo da UTFPR",organizator="usuario6@gmail.com",
                         banner="ImagesSeed/perfil.jpeg",max_particpant=10,max_voluntary_per_horary=5,
                         escale="2024-11-20T23:24:00Z",begin="2024-11-23T11:24:00Z",bscale="2024-11-23T20:24:00Z",end="2024-11-24T20:24:00Z")
    
if __name__ == "__main__":
    
    #API 
    eventapi=EventScript()
    userapi=UserScript()
    organizationapi=OrganizationScript()
    
    createusersseed(userapi=userapi)
    
    createorgevent(eventapi=eventapi,orgapi=organizationapi)
