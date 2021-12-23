from django import http
from django.contrib.auth.models import User
from django.db.models import query
from .serializers import RegisterSerializer, UserSerializer
from rest_framework import generics, serializers
from rest_framework.response import Response

class RegisterUserAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
            }
        )
