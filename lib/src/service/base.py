from typing import Generic, TypeVar, List, Any, Optional
from sqlmodel import Session, SQLModel, select
from repository.base import Repository, ModelT, CreateT, UpdateT
from model.models import PessoaBase

class Service(Generic[ModelT, CreateT, UpdateT]):
    def __init__(self, repo: Repository[ModelT, CreateT, UpdateT]):
        self.repo = repo

    def get(self, session: Session, id: Any) -> Optional[ModelT]:
        return self.repo.get(session, id)

    def list(self, session: Session, offset: int = 0, limit: int = 100) -> List[ModelT]:
        return self.repo.list(session, offset, limit)

    def create(self, session: Session, data: CreateT) -> ModelT:
        if data.nome not in data:
            return self.repo.create(session, data)
        if "@" not in data.email:
            raise ValueError("Email inválido")
        existe = self.repo.get_by_email(session, data.email)
        if existe:
            raise ValueError("Email já cadastrado")
        return self.repo.create(session, data)

    def get_by_email(self, session: Session, email: str) -> Optional[PessoaBase]:
        stmt = select(self.repo.model).where(self.repo.model.email == email)
        return session.exec(stmt).first()

    def update(self, session: Session, id: Any, data: UpdateT) -> ModelT:
        obj = self.repo.get(session, id)
        if not obj:
            raise ValueError("Not found")
        return self.repo.update(session, obj, data)

    def delete(self, session: Session, id: Any) -> None:
        obj = self.repo.get(session, id)
        if not obj:
            raise ValueError("Not found")
        return self.repo.delete(session, obj)