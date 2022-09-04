import pytest 
from classes.Pedido import Pedido
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho

@pytest.mark.test_classe_pedido
def test_pedido():
    nome = 'sergio'
    cpf = '123456789'
    email = 'ramellajr@gmail.com'
    sergiao = PessoaFisica(nome,email,cpf)
    carrinho = Carrinho()
    pedido = Pedido(sergiao,carrinho)
    assert Pedido(sergiao,carrinho).__str__() == pedido.__str__()