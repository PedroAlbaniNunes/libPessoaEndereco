from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


#------------------Pessoa-------------------
class PessoaBase(SQLModel):
    nome: str = Field(min_length=2, max_length=120)
    idade: Optional[int] = Field(default=None, ge=0, le=200)
    email: Optional[str] = Field(max_length=120, unique=True)

class Pessoa(PessoaBase, table = True):
    id: Optional[int] = Field(default = None, primary_key = True, index = True)
    enderecos: List["Endereco"] = Relationship(back_populates = "morador")

#-------------------Endereço----------------
class EnderecoBase(SQLModel):
    logradouro: Optional[str] = Field(min_length = 2, max_length = 200)
    numero: Optional[str] = Field(min_length = 1, max_length = 5)
    estado: Optional[str] = Field(min_length = 2, max_length = 2)
    cidade: Optional[str] = Field(min_length = 2, max_length = 120)

class Endereco(EnderecoBase, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    id_pessoa: Optional[int] = Field(default=None, foreign_key="pessoa.id")
    morador: Optional[Pessoa] = Relationship(back_populates = "enderecos")    