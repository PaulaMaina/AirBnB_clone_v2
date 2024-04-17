#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import shlex


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="states")

    @property
    def cities(self):
        states_all = models.storage.all()
        state_list = []
        city_list = []
        for key in all_models:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                state_list.append(states_all[key])
        for elem in state_list:
            if (elem.state_id == self.id):
                city_list.append(elem)

        return (city_list)
