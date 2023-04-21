from django.urls import path

from accounts.views import like_view
from posts.views.base import IndexView
from posts.views.posts import PostCreateView, PostDetailView


urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("post/add/", PostCreateView.as_view(), name="post_add"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post_detail"),
    path('posts/<int:post_pk>/like/', like_view, name='like_view'),
]
