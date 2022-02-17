from .models import About, MyResume, MySkills, MyProject
from rest_framework import viewsets
from .serializers import *


class AboutView(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    ordering = ['-id']


class MySkillView(viewsets.ModelViewSet):
    queryset = MySkills.objects.all()
    serializer_class = MySkillSerializer
    ordering = ['-id']


class MyProjectView(viewsets.ModelViewSet):
    queryset = MyProject.objects.all()
    serializer_class = MyProjectSerializer
    ordering = ['-id']


class MyResumeView(viewsets.ModelViewSet):
    queryset = MyResume.objects.all()
    serializer_class = MyResumeSerializer