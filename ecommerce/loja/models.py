from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    telefone = models.CharField(max_length=200, null=True, blank=True)
    id_sessao = models.CharField(max_length=200, null=True, blank=True)
    usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.email if self.email else "Sem Email"

class Categoria(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True)
    slug = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome if self.nome else "Sem Nome"

class Tipo(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True)
    slug = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.nome if self.nome else "Sem Nome"

class Produto(models.Model):
    imagem = models.ImageField(null=True, blank=True)
    nome = models.CharField(max_length=200, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.SET_NULL)
    tipo = models.ForeignKey(Tipo, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        categoria_nome = self.categoria.nome if self.categoria else "Sem Categoria"
        tipo_nome = self.tipo.nome if self.tipo else "Sem Tipo"
        return f"Nome: {self.nome}, Categoria: {categoria_nome}, Tipo: {tipo_nome}, Preço: {self.preco}"
    
    def total_vendas(self):
        itens = ItensPedido.objects.filter(pedido__finalizado=True, item_estoque__produto=self.id)
        total = sum([item.quantidade for item in itens])
        return total

class Cor(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True)
    codigo = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome if self.nome else "Sem Nome"

class ItemEstoque(models.Model):
    produto = models.ForeignKey(Produto, null=True, blank=True, on_delete=models.SET_NULL)
    cor = models.ForeignKey(Cor, null=True, blank=True, on_delete=models.SET_NULL)
    tamanho = models.CharField(max_length=200, null=True, blank=True)
    quantidade = models.IntegerField(default=0)

    def __str__(self) -> str:
        produto_nome = self.produto.nome if self.produto else "Sem Produto"
        cor_nome = self.cor.nome if self.cor else "Sem Cor"
        return f"{produto_nome}, Tamanho: {self.tamanho}, Cor: {cor_nome}"

class Endereco(models.Model):
    rua = models.CharField(max_length=400, null=True, blank=True)
    numero = models.IntegerField(default=0)
    complemento = models.CharField(max_length=200, null=True, blank=True)
    cep = models.CharField(max_length=200, null=True, blank=True)
    cidade = models.CharField(max_length=200, null=True, blank=True)
    estado = models.CharField(max_length=200, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        cliente_nome = self.cliente.nome if self.cliente else "Sem Cliente"
        return f"{cliente_nome} - {self.rua} - {self.cidade}-{self.estado} - {self.cep}"

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL)
    finalizado = models.BooleanField(default=False)
    codigo_transacao = models.CharField(max_length=200, null=True, blank=True)
    endereco = models.ForeignKey(Endereco, null=True, blank=True, on_delete=models.SET_NULL)
    data_finalizacao = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        cliente_email = self.cliente.email if self.cliente else "Sem Cliente"
        return f"Cliente: {cliente_email} - id_pedido: {self.id} - Finalizado: {self.finalizado}"
    
    @property
    def quantidade_total(self):
        itens_pedido = ItensPedido.objects.filter(pedido__id=self.id)
        quantidade = sum([item.quantidade for item in itens_pedido])
        return quantidade
    
    @property
    def preco_total(self):
        itens_pedido = ItensPedido.objects.filter(pedido__id=self.id)
        preco = sum([item.preco_total for item in itens_pedido])
        return preco
    
    @property
    def itens(self):
        itens_pedido = ItensPedido.objects.filter(pedido__id=self.id)
        return itens_pedido
    

class ItensPedido(models.Model):
    item_estoque = models.ForeignKey(ItemEstoque, null=True, blank=True, on_delete=models.SET_NULL)
    quantidade = models.IntegerField(default=0)
    pedido = models.ForeignKey(Pedido, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        pedido_id = self.pedido.id if self.pedido else "Sem Pedido"
        produto_nome = self.item_estoque.produto.nome if self.item_estoque and self.item_estoque.produto else "Sem Produto"
        cor_nome = self.item_estoque.cor.nome if self.item_estoque and self.item_estoque.cor else "Sem Cor"
        tamanho = self.item_estoque.tamanho if self.item_estoque else "Sem Tamanho"
        return f"Id pedido: {pedido_id} - Produto: {produto_nome}, {tamanho}, {cor_nome}"
    
    @property
    def preco_total(self):
        return self.quantidade * self.item_estoque.produto.preco if self.item_estoque and self.item_estoque.produto else 0

class Banner(models.Model):
    imagem = models.ImageField(null=True, blank=True)
    link_destino = models.CharField(max_length=400, null=True, blank=True)
    ativo = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.link_destino} - Ativo: {self.ativo}"
    
class Pagamento(models.Model):
    id_pagamento = models.CharField(max_length=400)
    pedido = models.ForeignKey(Pedido, null=True, blank=True, on_delete=models.SET_NULL)
    aprovado = models.BooleanField(default=False)
