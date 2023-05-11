import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
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
    species = Column(String(250),ForeignKey("species.id"))
    starships = Column(String(250))
    vehicles = Column(String(250), nullable=False)
    planet = relationship("Planets")
    specie = relationship("Species")

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

class Starships(Base):
    __tablename__ = 'starships'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    mglt = Column(String(250))
    cargo_capacity = Column(Integer)
    consumables = Column(String (20), nullable=False)
    cost_in_credits = Column(Integer)
    crew = Column(Integer)
    hyperdrive_rating = Column(Float)
    length = Column(Integer)
    manufacturer = Column(String(250))
    max_atmosphering_speed = Column(String(250))
    model = Column(String(250))
    name = Column(String(250))
    passengers = Column(Integer)
    films = Column(String(50))
    pilots = Column(String(50))
    starship_class = Column(String(250))
    #person_id = Column(Integer, ForeignKey('person.id'))
 
   
class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    cargo_capacity = Column(Integer)
    consumables = Column(String (20), nullable=False)
    cost_in_credits = Column(Integer)
    crew = Column(Integer)
    length = Column(Integer)
    manufacturer = Column(String(250))
    max_atmosphering_speed = Column(String(250))
    model = Column(String(250))
    name = Column(String(250))
    passengers = Column(Integer)
    films = Column(String(50))
    pilots = Column(String(50))
    vehicle_class = Column(String(250))
    #person_id = Column(Integer, ForeignKey('person.id'))

class Species(Base):
    __tablename__ = 'species'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    average_height = Column(Float)
    consumables = Column(String (20), nullable=False)
    average_lifespan = Column(Integer)
    classification = Column(String(50))
    designation = Column(String(50))
    eye_colors = Column(String(250))
    hair_colors = Column(String(250))
    homeworld = Column(String(250))
    name = Column(String(250))
    language = Column(Integer)
    people = Column(String(50))
    films = Column(String(50))
    skin_colors = Column(String(250))
    #person_id = Column(Integer, ForeignKey('person.id'))

class Cast(Base):
    __tablename__ ='cast'
    id = Column(Integer, primary_key=True)
    film_id = Column(Integer, ForeignKey("films.id"))
    film = relationship(Films, backref="cast")
    person_id=Column(Integer, ForeignKey("people.id"))
    person = relationship(People)

class StarshipCrew(Base):
    __tablename__ ='starship_crew'
    id = Column(Integer, primary_key = True)
    starship_id = Column(Integer, ForeignKey("starships.id"))
    starship = relationship(Starships)
    person_id=Column(Integer, ForeignKey("people.id"))
    person = relationship(People)

class VehicleCrew(Base):
    __tablename__ ='vehicle_crew'
    id = Column(Integer, primary_key = True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    vehicle = relationship(Vehicles)
    person_id=Column(Integer, ForeignKey("people.id"))
    person = relationship(People)

class FilmSet(Base):
    __tablename__ ='film_set'
    id = Column(Integer, primary_key = True)
    film_id = Column(Integer, ForeignKey("films.id"))
    film = relationship(Films)
    planet_id=Column(Integer, ForeignKey("planets.id"))
    planet = relationship(Planets)

class SpeciesCast(Base):
    __tablename__ ='species_cast'
    id = Column(Integer, primary_key = True)
    film_id = Column(Integer, ForeignKey("films.id"))
    film = relationship(Films)
    specie_id=Column(Integer, ForeignKey("species.id"))
    specie = relationship(Species)

class StarshipsCast(Base):
    __tablename__ ='starships_cast'
    id = Column(Integer, primary_key = True)
    film_id = Column(Integer, ForeignKey("films.id"))
    film = relationship(Films)
    starship_id=Column(Integer, ForeignKey("starships.id"))
    starship = relationship(Starships)

class VehiclesCast(Base):
    __tablename__ ='vehicles_cast'
    id = Column(Integer, primary_key = True)
    film_id = Column(Integer, ForeignKey("films.id"))
    film = relationship(Films)
    vehicle_id=Column(Integer, ForeignKey("vehicles.id"))
    vehicle = relationship(Vehicles)

def to_dict(self):
    return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
