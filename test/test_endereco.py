import pytest 
from classes.Endereco import Endereco
import requests

@pytest.mark.test_classe_endereco
def test_cep():
    cep = '04545010'
    numero = 93
    teste = Endereco(cep, numero).__str__()
    assert Endereco('04545010',93).__str__() == teste

@pytest.mark.test_classe_endereco
def test_consulta_cep_string():
    cep = '04545010'
    endereco = Endereco(cep, 93)
    assert True == endereco.cep.isdigit()

@pytest.mark.test_classe_endereco
def test_consulta_cep_int():
    cep = 4545010
    endereco = Endereco(cep, 93)
    
    assert True == endereco.cep.isdigit()

@pytest.mark.test_classe_endereco
def test_verifica_cep_inexistente():
    cep = '00000000'
    assert True == Endereco.consultar_cep(cep)

@pytest.mark.test_classe_endereco
def test_len_cep():
    cep = '04545010'
    assert 8 == len(cep)

@pytest.mark.test_classe_endereco
@pytest.mark.sem_internet
def test_sem_conexao_internet():
    cep = '04545010'
    with pytest.raises(requests.exceptions.ConnectionError):
        Endereco.consultar_cep(cep)


