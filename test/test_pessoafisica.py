import pytest 
from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco


@pytest.mark.test_classe_pessoafisica
def test_pessoa_fisica():
    nome = 'sergio'
    cpf = '123456789'
    email = 'ramellajr@gmail.com'
    sergiao = PessoaFisica(nome,email,cpf)  
    assert PessoaFisica(nome,email,cpf).__str__() == sergiao.__str__()

@pytest.mark.test_classe_pessoafisica
def test_adiciona_endereco():
    nome = 'sergio'
    cpf = '123456789'
    email = 'ramellajr@gmail.com'
    sergiao = PessoaFisica(nome,email,cpf)
    end = Endereco('04545010',93)
    sergiao.adicionar_endereco('casa',end)
    dici = sergiao.listar_enderecos()
    assert dici['casa'] == 'Rua: Rua Aleixo Garcia /Estado: SP /Cidade: São Paulo /Numero: 93 /Complemento: / Cep: 04545010'