import apiazure.views.Eventsview as func
from rest_framework.urls import path
urlpatterns = [
    path('',func.post_event,name="criar usuário"),
    path('<str:email>/',func.get_all_events,name="pegar todos os users"),
    path("event/<int:primary_key>/",func.get_update_delete_event,name="pegar,atualizar e deletar"),
    path("admin/all/",func.get_all_events_admin,name="pegar todos os eventos cadastrados")
]