
from datetime import datetime
import sys
import django
import os

# Configura o caminho do projeto Django
sys.path.append(f'/home/guilherme/Azure/AzureBackEnd/azureback')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'azureback.settings')

# Inicializa o Django
django.setup()

from apiazure.Modelo.Events import Event
from apiazure.Modelo.Scale import Scale
def main():
    event=Event.objects.get(id=1)
    scale=Scale.objects.select_related("horarys").filter(id=1)
    print(scale.values())
    
if __name__ == "__main__":
    main()
