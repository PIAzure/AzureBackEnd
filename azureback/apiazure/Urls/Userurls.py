import apiazure.Views.Userviews as func
from rest_framework.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
urlpatterns = [
    path('',func.post_user,name="criar usuário"),
    path('all/',func.getalluser,name="pegar todos os users"),
    path("<str:primary_key>/",func.getupdateuser,name="pegar,atualizar e deletar"),
    path("token",func.authuser,name="autenticar usuário")
]