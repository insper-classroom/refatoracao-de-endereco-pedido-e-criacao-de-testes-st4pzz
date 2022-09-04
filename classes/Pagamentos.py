from classes.Pedido import Pedido

class Pagamento:
    def __init__(self,pedido:Pedido):
        self.pedido = pedido 
        
        
    def processa_pagamento(self):
        self.pedido.status = Pedido.EM_ABERTO

    # Função dummy que sempre dá o pagamento como aprovado
    def pagamento_aprovado(self):
        self.pedido.status = Pedido.PAGO

    def __str__(self):
        return f'pedido: {self.pedido}'