from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('api/create',views.TaskView.as_view(),name='taskview')
]