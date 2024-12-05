from apiazure.views.Eventsview import EventDetailListPost, EventAdminDetail, EventDetail,EventDetailListGet
from rest_framework.urls import path
urlpatterns = [
    path('',EventDetailListPost.as_view(),name="criar usuário"),
    path('<str:email>/',EventDetailListGet.as_view(),name="pegar todos os users"),
    path("event/<int:primary_key>/",EventDetail.as_view(),name="pegar,atualizar e deletar"),
    path("admin/all/",EventAdminDetail.as_view(),name="pegar todos os eventos cadastrados")
]