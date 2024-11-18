from django.contrib import admin
from apiazure.Modelo.User import User
from apiazure.Modelo.Events import Event 


# Register your models here.
admin.site.register(User)
admin.site.register(Event)
admin.site.register(Organization)
