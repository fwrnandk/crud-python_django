from django.db import models

# Create your models here.

class cadastro(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField()
    sobrenome = models.TextField()
    idade = models.IntegerField()
