from django.contrib import admin
from apiazure.models import User
from apiazure.Modelo.Events import Event 
from  apiazure.Modelo.Organization import Organization

# Register your models here.
admin.site.register(User)
admin.site.register(Event)
admin.site.register(Organization)
