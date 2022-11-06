from abc import *
from typing import Any
from sqlalchemy import Table
from sqlalchemy.orm import Session


class BaseRepository(ABC):
    def __init__(self, db: Session, table: Table) -> None:
        self.db = db
        self.table = table

    def create(self, data: Any):
        entity = self.db.query(self.table).add_entity(data)
        self.db.commit()
        return entity

    def find_all(self):
        entities = self.db.query(self.table).all()
        return entities

    def find_one(self, id: int):
        entity = self.db.query(self.table).filter_by(self.table.id == id)
        return entity

    def update(self, id: int, data: Any):
        entity = self.db.query(self.table).filter_by(self.table.id == id).update(data)
        return entity

    def delete(self, id: int):
        entity = self.db.query(self.table).filter_by(self.table.id == id)
        self.db.query(self.table).delete(entity)
        self.db.commit()
        return entity
