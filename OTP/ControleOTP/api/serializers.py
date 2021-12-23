import smtplib
import email.message
from random import randrange
from django.db.models.base import Model
from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from ControleOTP.models import ControleOTP, Email, Codigo_Validacao



class OTPSerializer(ModelSerializer):
    class Meta:
        model = ControleOTP
        fields = ["email"]

    
class EmailSerializer(ModelSerializer):
    class Meta:
        model = Email
        fields = ["email"]

    def create(self, validated_data):
        otp_num = ""
        for _ in range(6):
            otp_num += str(randrange(0, 10))
        
        body_email = f"""
        <div class="inner" style='background-color: white'><h3 id="text23" style='text-transform: uppercase; color: #FFFFFF;font-family: 'Sora', sans-serif;letter-spacing: 0.1rem; width: calc(100% + 0.1rem);font-size: 1em; line-height: 1.625; font-weight: 600;'>Código de Verificação</h3><h1 id="text24" style='color: white;font-family: 'Sora', sans-serif;letter-spacing: 0.025rem; width: calc(100% + 0.025rem);font-size: 4.375em;    line-height: 1.25; font-weight: 700;'>{otp_num}</h1><p id="text18" style='color: white; font-family: 'Inter',sans-serif; font-size: 1.375em; line-height: 1.75; font-weight: 400;'>Yoo, jás aqui o código de verificação para logar em minha API, bom proveito!</p><ul id="buttons01" class="buttons"><li></div>
        """
        msg = email.message.Message()
        msg["Subject"] = "Código de Verificão"
        msg["From"] = "testespython281@gmail.com"
        msg["To"] = validated_data["email"]
        password = "testespython1"
        msg.add_header("Content-Type", "text/html")
        msg.set_payload(body_email)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()

        s.login(msg["From"], password)
        s.sendmail(msg["From"], [msg["To"]], msg.as_string().encode('utf-8'))

        
        data = Email.objects.create(
            email=validated_data["email"]
        )
        
        ControleOTP.objects.create(
            email=data,
            codigo=otp_num
        )

        return data 
class VerificacaoCodigo(ModelSerializer):
    class Meta:
        model = ControleOTP
        fields = ["codigo"]

    def create(self, validated_data):
        ultima = len(Email.objects.all())

        codigo = ControleOTP.objects.filter(email=ultima)[0]

        if validated_data["codigo"] == codigo.codigo:
            funfou = Codigo_Validacao.objects.create(funfou = "Funfou")
            return funfou

        else:
            return Codigo_Validacao.objects.create(
                funfou="Não"
            )

class OTPexibeSerializer(ModelSerializer):
    class Meta:
        model = ControleOTP
        fields = ["id", "email", "codigo"]
