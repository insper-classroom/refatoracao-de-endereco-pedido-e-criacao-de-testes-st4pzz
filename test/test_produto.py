import pytest 
from classes.Produto import Produto


@pytest.mark.test_classe_produto
def test_produto():
    _id = 12
    nome = 'Camiseta'
    teste = Produto(_id, nome).__str__()
    assert Produto(12,'Camiseta').__str__() == teste

@pytest.mark.test_classe_produto
def test_busca_nome():
    _id = 12
    nome = 'Camiseta'
    teste = Produto(_id, nome)
    produtos = Produto.busca_nome('Camiseta')
    assert Produto.busca_nome('Camiseta').__str__() == produtos.__str__()