from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from api.views import PostsView, PostDetailView, PostUpdateView, PostDeleteView, LikeView, PostCreateView


urlpatterns = [
    path("posts/", PostsView.as_view()),
    path("posts/<int:pk>", PostDetailView.as_view()),
    path("posts/create", PostCreateView.as_view()),
    path("posts/<int:pk>/update", PostUpdateView.as_view()),
    path("posts/<int:pk>/delete", PostDeleteView.as_view()),
    path('posts/<int:pk>/like', LikeView.as_view()),
    path('login/', obtain_auth_token, name='obtain_auth_token')
]