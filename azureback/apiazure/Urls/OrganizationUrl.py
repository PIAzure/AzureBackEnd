from django.urls import path
from apiazure.views.Organizationviews import OrganizationListView, OrganizationViewDetail


urlpatterns = [
    path('organization/',OrganizationListView.as_view()),
    path('organization/<str:primary_key>',OrganizationViewDetail.as_view())    
]