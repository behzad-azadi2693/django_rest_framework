from django.urls import path
from .views import (
    PostList, PostDetail, PostDestroy,
    PostUpdate, PostCreate, 
)
app_name = 'api'

urlpatterns = [
    path('post-list/',PostList.as_view(),name='post-list'),
    path('post-detail/<slug>/', PostDetail.as_view(), name='post-detail'),
    path('post-update/<int:pk>/', PostUpdate.as_view(),name='post-update'),
    path('post-destroy/<abc>/', PostDestroy.as_view(), name='post-destroy'),
    path('post-create/', PostCreate.as_view(), name='post-create'),
]