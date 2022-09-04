import pytest 
from classes.Carrinho import Carrinho
from classes.Produto import Produto

@pytest.mark.test_classe_carrinho
def test_carrinho():
    carrinho = Carrinho()
    assert Carrinho().__str__() == carrinho.__str__()

@pytest.mark.test_classe_carrinho
def test_adiciona_produto():
    carrinho = Carrinho()
    produto = Produto(12,'Camiseta')
    carrinho.adicionar_item(produto,2)
    dici = carrinho.__str__()
    assert dici[12] == 2

@pytest.mark.test_classe_carrinho
def test_remove_produto():
    carrinho = Carrinho()
    produto = Produto(12,'Camiseta')
    carrinho.adicionar_item(produto,2)
    carrinho.remover_item(produto,1)
    dici = carrinho.__str__()
    assert dici[12] == 1