from django.urls import path
from .views import projectList, fullView


urlpatterns = [
    path('', projectList, name='index'),
    path('<int:pk>/', fullView, name='full_view'),
]