from django.contrib import admin
from .models import Topic, ScientificDirector, Student, Application, User

admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Student)
admin.site.register(ScientificDirector)
admin.site.register(Application)

