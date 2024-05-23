#!/usr/bin/python3
"""DBStorage engine"""
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from models.state import State
from models.city import City
from models.place import Place
from models.user import User
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.place import Place
from models.user import User
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """Definition of the DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization of the DBStorage class"""
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary"""
        my_dict = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for element in query:
                key = "{}.{}".format(type(element).__name__, element.id)
                my_dict[key] = element
        else:
            listing = [State, City, User, Place, Review, Amenity]
            for prop in listing:
                query = self.__session.query(prop)
                for element in query:
                    key = "{}.{}".format(type(element).__name__, element.id)
                    my_dict[key] = element
        return (my_dict)

    def new(self, obj):
        """Adds the object to the current session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current session if obj is not None"""
        if obj:
            self.session.delete(obj)

    def reload(self):
        """Creates all tables in the database and the current session"""
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()

    def close(self):
        """Closes the current session"""
        self.__session.close()
