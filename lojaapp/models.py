from random import choices
from django.db import models
from django.contrib.auth.models import User



class Cliente(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200,null=True,blank=True)
    data_on = models.DateField(auto_now_add=True)

    def __str__(self):
            return self.nome




class Categoria(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.titulo



class Produto(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="produtos")
    preco_mercado = models.PositiveIntegerField()
    venda = models.PositiveIntegerField()
    descricao = models.TextField()
    garantia = models.CharField(max_length=300,null=True, blank=True)
    return_devolucao = models.CharField(max_length=300, null=True, blank=True)
    visualizacao = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titulo



class Carro(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.SET_NULL,null=True,blank=True)
    total = models.PositiveIntegerField(default=0)
    data_create = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Carro" + str(self.id)


class CarroProduto(models.Model):
    carro = models.ForeignKey(Carro,on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto,on_delete=models.CASCADE)
    avaliacao = models.PositiveIntegerField()
    quantidade = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()
   
    def __str__(self):
        return "Carro:" + str(self.carro.id) + "CarroProduto:" + str(self.id)

PEDIDO_STATUS=(
    ("Pedido Recebido","Pedido recebido"),
    ("Pedido Processsado","Pedido Processado"),
    ("Pedido a Caminho","Pedido a Caminho"),
    ("Pedido Completo", "Pedido Completo"),
    ("Pedido Cancelado","Pedido Cancelado")

)

class Pedido_order(models.Model):
    carro = models.OneToOneField(Carro, on_delete=models.CASCADE)
    ordenando_por = models.CharField(max_length=200)
    endereco_envio = models.CharField(max_length=200)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(null=True, blank=True)
    endereco_envio = models.CharField(max_length=200)
    subtotal = models.PositiveIntegerField()
    disconto = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    pedido_status = models.CharField(max_length=50, choices=PEDIDO_STATUS)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Pedido_order:" + str(self.id)




