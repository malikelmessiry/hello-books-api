from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from typing import Optional

class Author(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    cats: Mapped[Optional[list["Book"]]] = relationship(back_populates="author")b

    def to_dict(self):
        author_as_dict = {
            "id": self.id,
            "name": self.name
        }

        return author_as_dict
    
    @classmethod
    def from_dict(cls, author_data):
        new_author = cls(name=author_data["name"])
        return new_author