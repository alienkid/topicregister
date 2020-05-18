from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = "regvkr"

urlpatterns = [
	path('topics/', views.TopicList.as_view()),
	# path('topics/<int:pk>/', views.TopicDetail.as_view()),
	path('topics/application/<int:pk>/', views.ApplicationAdd.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
