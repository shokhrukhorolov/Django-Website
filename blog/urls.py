# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.post_list, name='post_list'),
# ]


""" Here I am setting up Auth """

from django.urls import path
from .views import post_list

urlpatterns = [
    path('', post_list, name='post_list'),
]
