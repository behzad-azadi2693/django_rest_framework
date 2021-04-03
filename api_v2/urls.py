from django.urls import path, include
from .views_post import PostList, PostUpdate, PostDelete, PostCreate, PostDetail
from .views_user import UserList, UserCreate, UserDelete, UserUpdate, UserDetail
from .views_comment import CommentCreate, CommentDelete, CommentDetail, CommentList, CommentUpdate

app_name='api_v2'

comment_url = [
    path('list/', CommentList.as_view(), name='cmt-list'),
    path('create/', CommentCreate.as_view(), name='cmt-creaate'),
    path('delete/<pk>/', CommentDelete.as_view(), name='cmt-delete'),
    path('detail/<pk>/', CommentDetail.as_view(), name='cmt-detail'),
    path('update/<pk>/', CommentUpdate.as_view(), name='cmt-update'),
]

user_url = [
    path('list/', UserList.as_view(), name='user-list'),
    path('create/',UserCreate.as_view(), name='user-creaate'),
    path('delete/<str:username>/', UserDelete.as_view(), name='user-delete'),
    path('detail/<username>/', UserDetail.as_view(), name='user-detail'),
    path('update/<str:username>/', UserUpdate.as_view(), name='user-update'),
]


urlpatterns = [
    path('post/list/', PostList.as_view(), name='post-list'),
    path('post/create/', PostCreate.as_view(), name='post-create'),
    path('post/delete/<int:pk>/', PostDelete.as_view(), name='post-delete'),
    path('post/detail/<slug>/', PostDetail.as_view(), name='post-detail'),
    path('post/update/<int:pk>/', PostUpdate.as_view(), name='post-update'),
    path('user/', include(user_url)),
    path('comment/', include(comment_url)),
]