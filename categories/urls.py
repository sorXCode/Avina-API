from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CategoryList, CategoryDetail, CategoryCreate

urlpatterns = [
    path('', CategoryList.as_view()),
    path('', CategoryCreate.as_view()),
    path('<int:pk>/', CategoryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)