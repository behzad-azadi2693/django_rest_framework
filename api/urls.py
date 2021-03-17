from django.urls import path, include
from .views_post import (
        PostList, PostDetail, PostDestroy,
        PostUpdate, PostCreate
    )
from .views_user import (
        UserDetail,UserCreate,UserLogin
    )
from .views_comment import (
        CommentList, CommentEditDetail
    )

app_name = 'api'

third_urlpatterns = [
    path('user-create/', UserCreate.as_view(), name='user-create'),
    path('user-detail/<username>/', UserDetail.as_view(),name='user-detail'),
    path('user-login/', UserLogin.as_view(), name='user-login'),
]

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
    path('',include(extra_urlpatterns)),
    path('',include(third_urlpatterns)),
]