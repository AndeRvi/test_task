from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from users.serializer import UserSerializer, ProfileSerializer
from users.models import Profile


class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class PostsListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, **kwargs):

        try:
            queryset = Profile.objects.get(user__id=pk)
        except Profile.DoesNotExist:
            return Response(
                {
                    'detail': 'User does not exists'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        realty = ProfileSerializer(queryset)

        return Response(realty.data)

