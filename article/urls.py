from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('post/delete_/<int:id>/', views.delete_, name='delete_'),
]