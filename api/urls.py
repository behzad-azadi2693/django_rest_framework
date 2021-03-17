from django.urls import path, include
from .views_post import (
        PostList, PostDetail, PostDestroy,
        PostUpdate, PostCreate, UserDetail
    )
from .views_comment import (
        CommentList, CommentEditDetail
    )

app_name = 'api'


extra_urlpatterns = [
    path('comment-list/',CommentList.as_view(),name='comment-list'),
    path('comment-detail/<int:id>/', CommentEditDetail.as_view(), name='comment-detail'),
]

urlpatterns = [
    path('post-list/',PostList.as_view(),name='post-list'),
    path('post-detail/<slug>/', PostDetail.as_view(), name='post-detail'),
    path('post-update/<int:pk>/', PostUpdate.as_view(),name='post-update'),
    path('post-destroy/<abc>/', PostDestroy.as_view(), name='post-destroy'),
    path('post-create/', PostCreate.as_view(), name='post-create'),
    path('user-detail/<username>/', UserDetail.as_view(),name='user-detail'),
    path('',include(extra_urlpatterns)),
]