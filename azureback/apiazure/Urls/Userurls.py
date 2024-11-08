import apiazure.Views.Userviews as func
from rest_framework.urls import path
urlpatterns = [
    path('',func.post_user,name="criar usuário"),
]