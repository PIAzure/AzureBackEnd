import os
import django
import sys
# Configurar as variáveis de ambiente e inicializar o Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "azureback.settings")
django.setup()

class Script:
    pass

if __name__ == "__main__":
    seed_data()
