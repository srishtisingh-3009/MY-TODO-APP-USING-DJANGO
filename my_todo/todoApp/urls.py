from django.urls import path
from todoApp import views
urlpatterns=[
path('',views.index,name='first'),
path('update_task/<str:pk>/',views.updateTask,name='update_task'),
path('delete/<str:pk>/',views.deleteTask,name='delete'),



]
