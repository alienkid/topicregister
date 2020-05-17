from django.contrib import admin
from .models import Topic, ScientificDirector, Student, Application

admin.site.register(Topic)
admin.site.register(ScientificDirector)
admin.site.register(Student)
admin.site.register(Application)