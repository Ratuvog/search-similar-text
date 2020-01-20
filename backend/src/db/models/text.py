from sqlalchemy import Column, Integer, PickleType, String
from sqlalchemy.orm import relationship

from src.db.mixins.timestamp import Timestamps
from src.db.models.base import BaseModel


class Text(BaseModel, Timestamps):
    __tablename__ = 'texts'

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    vector = Column(PickleType, nullable=False)

    sentences = relationship(
        'Sentence',
        cascade='all, delete, delete-orphan',
        back_populates='text'
    )
