#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------



class Produto:
    lista_produtos = []

    def __init__(self, id_produto, nome):
        self.__id = id_produto
        self.__nome = nome
        Produto.lista_produtos.append(self.__nome.lower())
        

    def set_id(self, id_novo):
        self.__id = id_novo

    # def get_id(self):
    #     return self.id

    # def set_nome(self, nome_novo):
    #     self.nome = nome_novo
    
    def get_id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,novo_nome):
        self.__nome = novo_nome
      

    @nome.getter
    def nome(self):
        return self.__nome

    def busca_nome(string):
        produtos = []
        for nome in Produto.lista_produtos:
            if string.lower() == nome[:len(string)]:
                produtos.append(nome)
        return produtos

    def __str__(self):
        return f'id: {self.__id} /nome: {self.__nome} '