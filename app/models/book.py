from __future__ import annotations
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from ..db import db
from typing import Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from .author import Author

# from ..models.author import Author

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    author_id: Mapped[Optional[int]] = mapped_column(ForeignKey("author.id"))
    author: Mapped[Optional["Author"]] = relationship("Author", back_populates="books")
    genres: Mapped[list["Book"]] = relationship(secondary="book_genre", back_populates="books")

    @classmethod
    def from_dict(cls, book_data):
        new_book = Book(title=book_data["title"],
                        description=book_data["description"],
                        author_id=book_data.get("author_id", None),
                        genres=book_data.get("genres, None"))
        return new_book

    def to_dict(self):
        book_as_dict = {}
        book_as_dict["id"] = self.id
        book_as_dict["title"] = self.title
        book_as_dict["description"] = self.description
        book_as_dict["author"] = self.author.name if self.author_id else None

        if self.genres:
            book_as_dict["genres"] = [genre.name for genre in self.genres]
            
        return book_as_dict
    

