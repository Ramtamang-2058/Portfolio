from rest_framework import serializers
from .models import About, MyResume, MySkills, MyProject

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class MySkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = MySkills
        fields = '__all__'


class MyProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProject
        fields = '__all__'


class MyResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyResume
        fields = '__all__'