from rest_framework import status
from rest_framework.permissions import IsAuthenticated, BasePermission, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import PostSerializer
from posts.models.posts import Post


class IsCreator(BasePermission):
    def has_permission(self, request, view):
        if request.method is 'PUT' or 'DELETE':
            post = Post.objects.get(pk=view.kwargs['pk'])
            return post.author == request.user
        else:
            return True


class PostCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data.copy()
        serializer = PostSerializer(data=data)
        data['author'] = request.user.id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().exclude(is_deleted=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, *args, **kwargs):
        post = Post.objects.all().exclude(is_deleted=True)
        serializer = PostSerializer(post[kwargs['pk']-1], many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostUpdateView(APIView):
    permission_classes = [IsCreator]

    def put(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post, data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDeleteView(APIView):
    permission_classes = [IsCreator]

    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(f"Удален пост: {post.id}", status=status.HTTP_204_NO_CONTENT)


class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        user = request.user
        if user in post.user_likes.all():
            post.likes_count -= 1
            post.user_likes.remove(user)
            post.save()
            return Response({'detail': 'Лайк успешно убран с поста'})
        else:
            post.likes_count += 1
            post.user_likes.add(user)
            post.save()
            return Response({'detail': 'Лайк успешно добавлен на пост'})