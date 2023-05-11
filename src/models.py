import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    films = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    homeworld = Column(Integer, ForeignKey("planets.id"))
    mass = Column(Integer, nullable=False)
    skin_color = Column(String(250), nullable=False)
    species = Column(String(250), nullable=False)
    starships = Column(String(250), nullable=False)
    vehicles = Column(String(250), nullable=False)
    planet = relationship("Planets")

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=False)
    films = Column(String(250), nullable=False)
    gravity = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    residents = Column(String(250), nullable=False)
    roation_period = Column(Integer, nullable=False)
    surface_water = Column(Integer, nullable=False)
    terrain = Column(String(250), nullable=False)
    # starships = Column(String(250), nullable=False)
    # vehicles = Column(String(250), nullable=False

class Films(Base):
    __tablename__ = 'films'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    characters = Column(String(250))
    director = Column(String(250))
    episode_id = Column(Integer, nullable=False)
    opening_crawl = Column(String(250))
    planets = Column(String(250))
    producer = Column(String(250))
    release_date = Column(String(250))
    species = Column(String(250))
    starships = Column(String(250))
    title = Column(String(250))
    vehicles = Column(String(250))
    #person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(People)


class Cast(Base):
    __tablename__ ='cast'
    id = Column(Integer, primary_key=True)
    film_id = Column(Integer, ForeignKey("films.id"))
    film = relationship(Films, backref="cast")
    person_id=Column(Integer, ForeignKey("people.id"))
    person = relationship(People)




def to_dict(self):
    return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
