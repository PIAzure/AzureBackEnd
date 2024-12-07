import apiazure.views.Participantsviews as func
from rest_framework.urls import path

urlpatterns = [
    path('/<int:eventid>/',func.ParticipantsDetailsGet.as_view(),name="Pegar todos os participantes de evento"),
    path("/<int:id_participant>/delete",func.ParticipantsDetailsDelete.as_view(),name="sair de evento"),
    path("",func.ParticipantsDetailsPost.as_view(),name="entrar em evento"),
]