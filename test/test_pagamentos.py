import pytest 
from classes.Pagamentos import Pagamento
from classes.Pedido import Pedido
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho


@pytest.mark.test_classe_pagamento
def test_pagamento():
    pessoa1 = PessoaFisica('sergio','ramellajr@gmail.com','123456789')
    carrinho = Carrinho()
    pedido = Pedido(pessoa1, carrinho)
    pagamento = Pagamento(pedido)
    assert Pagamento(pedido).__str__() == pagamento.__str__()

@pytest.mark.test_classe_pagamento
def test_processa_pagamento():
    pessoa1 = PessoaFisica('sergio','ramellajr@gmail.com','123456789')
    carrinho = Carrinho()
    pedido = Pedido(pessoa1, carrinho)
    pagamento = Pagamento(pedido)
    pagamento.processa_pagamento()
    assert pedido.status == Pedido.EM_ABERTO

@pytest.mark.test_classe_pagamento
def test_pagamento_aprovado():
    pessoa1 = PessoaFisica('sergio','ramellajr@gmail.com','123456789')
    carrinho = Carrinho()
    pedido = Pedido(pessoa1, carrinho)
    pagamento = Pagamento(pedido)
    pagamento.pagamento_aprovado()
    assert pedido.status == Pedido.PAGO


