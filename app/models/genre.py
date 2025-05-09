from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db


class Genre(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
    
    @classmethod
    def from_dict(cls, genre_data):
        new_genre = cls(name=genre_data["name"])

        return new_genre