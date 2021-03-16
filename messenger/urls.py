from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import StartMessaging

urlpatterns = [
    path('', StartMessaging.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)