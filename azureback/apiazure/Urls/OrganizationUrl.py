from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apiazure.views.Organizationviews import OrganizationListView, OrganizationViewDetail


urlpatterns = [
    path('organization/',OrganizationListView.as_view()),
    path('organization/<str:primary_key>',OrganizationViewDetail.as_view())    
]