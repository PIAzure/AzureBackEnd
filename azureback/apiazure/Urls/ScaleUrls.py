from apiazure.views.Scaleview import ScaleDetailsList, ScaleDetailsDelete, ScaleDetailVoluntary
from rest_framework.urls import path
urlpatterns = [
    path('/<int:id>/',ScaleDetailsList.as_view(),name="pegar todos os users"),
    path("/<int:horaryid>/horary/<str:email>/",ScaleDetailsDelete.as_view()),
    path("/<int:horaryid>/delete/<int:voluntaryid>/",ScaleDetailVoluntary.as_view())
]