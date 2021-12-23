from .serializers import OTPSerializer, OTPexibeSerializer, VerificacaoCodigo, EmailSerializer
from rest_framework import generics, serializers
from django.urls import reverse_lazy
from rest_framework.response import Response
from ControleOTP.models import Codigo_Validacao

class OTP_API(generics.GenericAPIView):
    serializer_class = OTPSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
    
        return Response(
            {
                "OTP": OTPexibeSerializer(user, context=self.get_serializer_context()).data
            }
        )

class EmailAPI(generics.GenericAPIView):
    serializer_class = EmailSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "Data": "Confira seu E-mail"
        })

class ValidacaoAPI(generics.GenericAPIView):
    serializer_class = VerificacaoCodigo

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        ultima = len(Codigo_Validacao.objects.all())
        ok = Codigo_Validacao.objects.filter(id=ultima)[0]

        if str(ok) == "Funfou":
            return Response({
                "Situacao": "Pode cadastrar-se"
            })

        else:
            return Response({
                "Situacao": f"Não pode cadastrar-se"
            })