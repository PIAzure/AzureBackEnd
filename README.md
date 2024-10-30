# AzureBackEnd






# Instalação
   
Para garantir o correto funcionamento do aplicativo, é recomendável especificar a versão exata do Python ao instalar. Execute o comando abaixo para instalar o Python 3:

```bash
sudo apt install python3
```

Em seguida, instale o Django e o Django REST Framework com o comando:

```bash
pip install django djangorestframework 
```

Para rodar a aplicação, certifique-se de ter o Docker instalado, pois ele permitirá executar o PostgreSQL em um ambiente controlado, configurado de acordo com as especificações da aplicação. Use o comando a seguir para iniciar um contêiner PostgreSQL:

```bash
   docker run --name meu_postgres -e POSTGRES_DB=public -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -p 5433:5432 -d postgres:latest
```
Para criar as tabelas no banco e baixar as dependências execute o comando:

```bash
   python3 manage.py migrations && python3 manage.py migrate
```

Para rodar o servidor execute o comando:

```bashrn
   python3 manage.py runserver
```
