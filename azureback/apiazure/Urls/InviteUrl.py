from apiazure.views.Inviteview import InviteDetailsPost, InviteDetatailAceptRecuse, InviteDetailList
from rest_framework.urls import path
urlpatterns = [
    path('',InviteDetailsPost.as_view(),name="criar usuário"),
    path('/<str:email>/',InviteDetailList.as_view(),name="pegar todos os users"),
    path("/acept/<int:idinvite>/",InviteDetatailAceptRecuse.as_view(),name="pegar,atualizar e deletar"),
]