from apiazure.views.Followviews import FollowPost, FollowDelete
from apiazure.views.Notifyview import NotifyView
from rest_framework.urls import path
urlpatterns = [
    path('',FollowPost.as_view(),name="criar usuário"),
    path('<str:useremail>/unfollow/<str:oremail>/',FollowDelete.as_view(),name="criar usuário"),
    path("<str:email>/",FollowDelete.as_view()),
    path("notifys/<str:useremail>/",NotifyView.as_view())
]