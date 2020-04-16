from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status

from posts.serializers import PostSerializer, LikeSerializer
from posts.models import Post, Like
from drf_yasg.utils import swagger_auto_schema


class PostsListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        queryset = Post.objects.filter(author=self.request.user)
        realty = PostSerializer(queryset, many=True)

        return Response(realty.data)

    @swagger_auto_schema(request_body=PostSerializer)
    def post(self, request, format=None):

        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.save()
            post.author = self.request.user
            post.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUES)


class PostApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, **kwargs):

        try:
            queryset = Post.objects.get(id=pk, author=self.request.user)
        except Post.DoesNotExist:
            return Response(
                {
                    'detail': 'Post does not exists'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        realty = PostSerializer(queryset)

        return Response(realty.data)

    @swagger_auto_schema(request_body=PostSerializer)
    def put(self, request, pk, format=None):

        try:
            realty = Post.objects.get(
                id=pk, user=self.request.user
            )
        except Post.DoesNotExist:
            return Response(
                {
                    'detail': 'Post does not exists'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PostSerializer(realty, data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, post_id, **kwargs):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response(
                {
                    'detail': 'Post does not exists'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            queryset = Like.objects.get(
                post__id=post_id,
                author=self.request.user
            )
        except Like.DoesNotExist:
            return Response(
                {
                    'detail': 'Like does not exists'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        like = LikeSerializer(queryset)

        return Response(like.data)

    @swagger_auto_schema(request_body=LikeSerializer)
    def put(self, request, post_id, format=None):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response(
                {
                    'detail': 'Post does not exists'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            like = Like.objects.get(
                post=post, author=self.request.user
            )
        except Like.DoesNotExist:
            return Response(
                {
                    'detail': 'Like does not exists'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = LikeSerializer(like, data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=LikeSerializer)
    def post(self, request, post_id,  format=None):
        serializer = LikeSerializer(data=request.data)
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response(
                {
                    'detail': 'Post does not exists'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if serializer.is_valid():
            try:
                _ = Like.objects.get(
                    post__id=post_id,
                    author=self.request.user
                )
                return Response(
                    {
                        'detail': 'Like already exists'
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            except Like.DoesNotExist:
                like = serializer.save()
                like.author = self.request.user
                like.post = post
                like.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUES)


class LikeStatsApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, **kwargs):
        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')
        if date_from and date_to:
            queryset = Like.objects.filter(
                created_at__gt=date_from,
                created_at__lt=date_to
            )
        else:
            queryset = Like.objects.all()

        return Response(
            {
                'count': queryset.count(),
                'like': queryset.filter(response=True).count(),
                'unlike': queryset.filter(response=False).count(),
            },
            status=status.HTTP_400_BAD_REQUEST
        )
