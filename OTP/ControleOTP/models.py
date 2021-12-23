from django.db import models
from django.db.models.base import Model

class Email(models.Model):
    email = models.EmailField()

class Codigo_Validacao(models.Model):
    funfou = models.CharField(max_length=10)

    def __str__(self):
        return self.funfou

# Create your models here.
class ControleOTP(models.Model):
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=6)
