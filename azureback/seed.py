
from datetime import datetime
import sys
import django
import os

# Configura o caminho do projeto Django
sys.path.append(f'/home/guilherme/Azure/AzureBackEnd/azureback')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'azureback.settings')

# Inicializa o Django
django.setup()

# Agora você pode importar os modelos e trabalhar normalmente
from apiazure.Modelo.Horario import Horary
from apiazure.Modelo.Voluntary import Voluntary
from apiazure.models import User
def main():
    Horary.objects.create(datetime="2024-11-20T13:24:00Z",max_voluntary_scale=10)
    horatio1=Horary.objects.get(id=7)
    print(horatio1.voluntarys)
if __name__ == "__main__":
    main()
