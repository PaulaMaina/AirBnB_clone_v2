#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="states")

    def __init__(self, *args, **kwargs):
        """Initializes the state class"""
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        cities_all = models.storage.all(City)
        city_list = []
        for city in cities_all.values():
            if city.state_id == self.id:
                city_list.append(city)
            return (city_list)
