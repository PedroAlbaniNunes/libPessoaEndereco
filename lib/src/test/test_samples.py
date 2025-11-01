import pytest
from model.models import Pessoa, Endereco

def test_create_pessoa():
    """
    Testa se dá pra criar a pessoa
    """
    pessoa = Pessoa(nome="Pedro Albani", idade="21", email="albanipedroprofissional@gmail.com")
    assert pessoa.nome == "Pedro Albani"
    assert pessoa.idade == "21"
    assert pessoa.email == "albanipedroprofissional@gmail.com"

def test_create_endereco():
    """
    Testa se dá pra criar o endereco
    """

    endereco = Endereco(logradouro="Telmo Torres", numero="01", cidade="Vila Velha")
    assert endereco.logradouro == "Telmo Torres"
    assert endereco.numero == "01"
    assert endereco.cidade == "Vila Velha"