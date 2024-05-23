from django.db import models
from django.contrib.auth.hashers import make_password
from django.conf import settings

class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    celular = models.CharField(max_length=14)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.id and not settings.DEBUG:  # Se for um novo usuário e não estiver em modo de debug
            self.senha = make_password(self.senha)  # Criptografa a senha
        super().save(*args, **kwargs)

class Item(models.Model):
    codigo_item = models.CharField(max_length=30)
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    itens = models.ManyToManyField(Item)
    data_pedido = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return f"Pedido {self.id} por {self.usuario.nome}"
    
