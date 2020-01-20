from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from src.db.mixins.timestamp import Timestamps
from src.db.models.base import BaseModel


class Sentence(BaseModel, Timestamps):
    __tablename__ = 'sentences'

    id = Column(Integer, primary_key=True)
    text_id = Column(Integer, ForeignKey('texts.id'))
    sentence = Column(String, nullable=False)

    text = relationship('Text', back_populates='sentences')
