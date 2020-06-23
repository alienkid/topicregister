from rest_framework import serializers
from .models import Topic, Application, Student, ScientificDirector

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name_S', 'last_name_S', 'num', 'group']

class ScientificDirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScientificDirector
        fields = ['position_name', 'last_name_D', 'first_name_D', 'patronymic']