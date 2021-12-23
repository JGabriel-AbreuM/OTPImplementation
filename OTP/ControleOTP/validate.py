from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validata_otp(valor):
    if valor == "" or None:
        raise ValidationError(_("Verifique seu E-mail"))