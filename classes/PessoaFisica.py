#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
import re


class PessoaFisica:
    '''Esta classe implementa uma pessoa no contexto de uma compra em e-commerce.
    
    As propriedades email e cpf estão privadas para previnir o usuário da classe de 
    acessar e alterar diretamente a propriedade sem uma verificação.
    '''

    lista = []
    def __init__(self, nome, email, cpf):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.__enderecos = {}
        PessoaFisica.lista.append(self.nome.lower())

    # escolher o estilo de retorno

    def adicionar_endereco(self, apelido_endereco, end:Endereco):
        self.__enderecos[apelido_endereco] = f'Rua: {end.rua} /Estado: {end.estado} /Cidade: {end.cidade} /Numero: {end.numero} /Complemento: {end.complemento}/ Cep: {end.cep}'
        

    def remover_endereco(self,apelido_endereco):
        del self.__enderecos[apelido_endereco]

    def get_endereco(self, apelido_endereco):
        for apelidos in self.__enderecos.keys():
            if apelidos == apelido_endereco:
                return self.__enderecos[apelido_endereco]
        
    def listar_enderecos(self):
        return self.__enderecos
    
    def __str__(self):
        return f'nome: {self.nome} /email: {self.email} /cpf: {self.cpf} /enderecos: {self.__enderecos}'

    def busca_nome(string):
        nomes = []
        for pessoa in PessoaFisica.lista:
            if string.lower() == pessoa[:len(string)]:
                nomes.append(string)
        return nomes  
    