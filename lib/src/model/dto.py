from model.models import PessoaBase, EnderecoBase
from typing import  List, Optional
from sqlmodel import Field



class CriarPessoa(PessoaBase):
    pass

class AtualizarPessoa(PessoaBase):
    nome: Optional[str] = Field(min_length=2, max_length=120)
    dt_nasc: Optional[str] = Field(min_length=8, max_length=8)
    email: Optional[str] = Field(min_length=10, max_length= 120)

class LerPessoa(PessoaBase):
    id: int

class Pessoa_Endereco(LerPessoa):
    enderecos: List["CriarEndereco"] = []

class CriarEndereco(EnderecoBase):
    id_pessoa: int = Field(foreign_key="pessoa.id")

class AtualizarEndereco(EnderecoBase):
    logradouro: Optional[str] = Field(min_length = 2, max_length = 200)
    numero: Optional[str] = Field(min_length = 1, max_length = 5)
    estado: Optional[str] = Field(min_length = 2, max_length = 2)
    cidade: Optional[str] = Field(min_length = 2, max_length = 120)
    id_pessoa: Optional[int] = None

class LerEndereco(EnderecoBase):
    id: int
    morador: Optional[int] = None