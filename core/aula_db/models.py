from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __(self):
        return self.nome