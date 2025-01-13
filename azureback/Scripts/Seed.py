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

from UserScript import UserScript


if __name__ == "__main__":
    
    user=UserScript()
    print(user.getuser())
