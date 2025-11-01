from controller.generic import create_crud_router, Hooks
from model.models import Pessoa, Endereco 
from model.dto import CriarPessoa, AtualizarPessoa, LerPessoa
from sqlmodel import Session, select
from fastapi import HTTPException

class PessoaHooks(Hooks[Pessoa, CriarPessoa, AtualizarPessoa]):
    def pre_create(self, payload: CriarPessoa, session: Session) -> None:
        if payload.endereco_id is not None and payload.endereco_id != 0:
            if not session.get(Endereco, payload.endereco_id):
                raise HTTPException(400, "Endereco_id inválido")

    def pre_update(self, payload: AtualizarPessoa, session: Session, obj: Pessoa) -> None:
        if payload.endereco_id is not None:
            if payload.endereco_id != 0 and not session.get(Endereco, payload.endereco_id):
                raise HTTPException(400, "Endereco_id inválido")
            

router = create_crud_router(
    model = Pessoa,
    create_schema= CriarPessoa,
    update_schema= AtualizarPessoa,
    read_schema= LerPessoa,
    prefix= "/pessoa",
    tags= ["pessoa"],
    hooks= PessoaHooks(),
)