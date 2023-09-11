import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__="user"
    id =Column(Integer, primary_key=True)
    username =Column(String(40), nullable=False)
    firstname =Column(String(50), nullable=False)
    lastname =Column(String(50), nullable=False)
    email =Column(String(100), nullable=False)
    password = Column(String(100),nullable=False)
    
    def to_dict(self):
        return {}

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(String(50), nullable=False)
    mass = Column(String(50), nullable=False)
    hair_color = Column(String(50), nullable=False)
    skin_color = Column(String(50), nullable=False)
    eye_color = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)
    birth_year = Column(String(50), nullable=False)

    def to_dict(self):
        return {}

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    diameter = Column(String(80), nullable=False)
    rotation_period = Column(String(80), nullable=False)
    orbital_period = Column(String(80), nullable=False)
    gravity = Column(String(80), nullable=False)
    population = Column(String(80), nullable=False)
    climate = Column(String(80), nullable=False)
    terrain = Column(String(80), nullable=False)
    surface_water = Column(String(80), nullable=False)
    orbital_period =Column(String(250), nullable=True)
    
    def to_dict(self):
        return {}



class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True, autoincrement=True)

    id_user = Column(Integer,ForeignKey("user.id"),nullable=True)
    user = relationship(User)

    id_vehicles = Column(Integer,ForeignKey("person.id"),nullable=True)
    vehicles = relationship(Person) 
    
    id_characters = Column(Integer,ForeignKey("planet.id"),nullable=True)
    characters = relationship(Planet)

    def to_dict(self):
        return {}
    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
