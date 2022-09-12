from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.dialects.postgresql import ARRAY

from database import Base


class MakeToModelsMap(Base):
    __tablename__ = 'make_to_models_map'

    make = Column(String(273),primary_key=True)
    model_list = Column(ARRAY(String(256)))

    def __init__(self, make, model_list):

        self.make = make
        self.model_list = model_list

    def __repr__(self):
        return '<User %r>' % self.make

    def to_dict(self):
        return {

            "make": self.make,
            "model_list": self.model_list,

        }
