from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from .serializer import UserSerializer, RegistrationSerializer

User = get_user_model()


class UserModelViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
        })
