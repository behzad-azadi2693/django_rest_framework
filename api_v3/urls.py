from django.urls import path
from .views_post import post_list, post_detail


app_name = 'app_v3'

urlpatterns = [
    path('post/list/', post_list, name='post-list'),
    path('post/detail/<int:pk>/', post_detail, name='post-detail'),
]
