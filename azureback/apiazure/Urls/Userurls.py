import apiazure.views.Userviews as func
from rest_framework.urls import path
urlpatterns = [
    path('',func.UserListDetail.as_view(),name="criar usuário e pegar todos os usuarios"),
    path("<str:primary_key>/",func.UserDetail.as_view(),name="pegar,atualizar e deletar"),
    path("auth/token/",func.UserAdminDetail.as_view(),name="autenticar usuário"),
]