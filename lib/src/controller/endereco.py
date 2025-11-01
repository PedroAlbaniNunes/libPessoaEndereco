from controller.generic import create_crud_router, Hooks
from model.models import Endereco, Pessoa
from model.dto import CriarEndereco, AtualizarEndereco, LerEndereco
from fastapi import HTTPException
from sqlmodel import Session, select

class EnderecoHooks(Hooks[Endereco, CriarEndereco, AtualizarEndereco]):
    def pre_create(self, payload: CriarEndereco, session: Session) -> None:
        if payload.id_pessoa is not None:
            pessoa = session.get(Pessoa, payload.id_pessoa)
            if not Pessoa:
                raise HTTPException(400, "Não encontrado")
            
    def pre_update(self, payload: AtualizarEndereco, session: Session) -> None:
        if payload.id_pessoa is not None:
            pessoa = session.get(Pessoa, payload.id_pessoa)
            if not pessoa:
                raise HTTPException(400, "Não encontrado")

        
router = create_crud_router(
    model = Endereco,
    create_schema= CriarEndereco,
    update_schema= AtualizarEndereco,
    read_schema= LerEndereco,
    prefix= "/endereco",
    tags= ["endereco"],
    hooks=EnderecoHooks(),
)