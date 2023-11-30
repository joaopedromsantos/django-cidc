from django.db import models

# Create your models here.


class Pais(models.Model):
    nome = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.nome


class Estado(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT, null=True, blank=False)
    nome = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, null=True, blank=False)
    nome = models.CharField(max_length=100, unique=True)
    capital = models.BooleanField(default=False)
    descricao = models.TextField(verbose_name='Descrição', blank=True, null=True)

    def __str__(self):
        return self.nome
