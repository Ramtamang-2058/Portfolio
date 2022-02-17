from django.urls import path, include
from rest_framework import routers
from .views import *

route = routers.DefaultRouter()
route.register('about', AboutView),
route.register('myskills', MySkillView)
route.register('myproject', MyProjectView)
route.register('resume', MyResumeView)

urlpatterns = [
    path('api/', include(route.urls)),
]
