from django.db import models


class Localizar_CPF(models.Model):
    cpf = models.CharField(max_length=11)
    status = models.BooleanField(default=False)
