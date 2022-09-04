#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho




class Pedido:
    def __init__(self,pessoa:PessoaFisica,carrinho:Carrinho,status='',endereco_faturamento='',endereco_entrega=''):
        self.status = status
        self.endereco_faturamento = endereco_faturamento
        self.endereco_entrega = endereco_entrega
        self.pessoa = pessoa
        self.carrinho = carrinho

    EM_ABERTO = 'EM ABERTO'
    PAGO = 'PAGO'

    def __str__(self):
        return f'pessoa: {self.pessoa.nome} /status: {self.status} /endereço de entrega: {self.endereco_entrega} /endereço de faturamento: {self.endereco_faturamento} /carrinho: {self.carrinho.retorna_itens()}'
    