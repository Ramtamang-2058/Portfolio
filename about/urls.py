from django.urls import path, include
from rest_framework import routers
from .views import (TeamLeadsView,
                    TeamMembersView,
                    TeamView,
                    OrganizationView,
                    TeamLeadsNepaliView,
                    TeamMembersNepaliView,
                    OrganizationNepaliView)

route = routers.DefaultRouter()
route.register('post_members', TeamView)
route.register('get_team_leads/en', TeamLeadsView)
route.register('get_team_members/en', TeamMembersView)
route.register('get_organization/en', OrganizationView)
route.register('get_team_leads/np', TeamLeadsNepaliView)
route.register('get_team_members/np', TeamMembersNepaliView)
route.register('get_organization/np', OrganizationNepaliView)


urlpatterns = [
    path('api/', include(route.urls)),
]

