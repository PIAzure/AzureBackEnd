from apiazure.views.Scaleview import ScaleDetailsList, ScaleDetailsDelete
from rest_framework.urls import path
urlpatterns = [
    path('/<int:eventid>/',ScaleDetailsList.as_view(),name="pegar todos os users"),
    path("/<int:horaryid>/horary/<str:email>/",ScaleDetailsDelete.as_view())
]