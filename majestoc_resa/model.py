from . import db
from sqlalchemy import Integer, Column, String, ForeignKey, DateTime
from starter import app
from datetime import date


app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///resa.db')
#engine = create_engine('sqlite:///resa.db')


class Film(db.Model):
    """Modele d'un film avec son nom et sa durée"""
    id_film = Column(Integer, nullable=False, unique=False, primary_key=True)
    nom_film = Column(String(30), nullable=False, unique=False)
    nombre_place = Column(Integer, nullable=False, unique=True)
    duree_film = Column(Integer, nullable=False, unique=False)


class Seance(db.Model):
    """Item du planning des séances"""
    id_seance = Column(Integer, nullable=False, unique=True, primary_key=True)
    film = Column(String, ForeignKey("Film.nom_film"), unique=False, nullable=False)
    date_debut = Column(String(10), nullable=False, unique=False)
    date_fin = Column(String(10), nullable=False, unique=False)
    duree_seance = Column(Integer, nullable=False, unique=False, date)


class Salle(db.Model):
    """Item du planning des salles"""
    id_cinema = Column(Integer, nullable=False, unique=True, primary_key=True)
    cinema = Column(String(15), nullable=False, unique=True)
    numero_salle = Column(Integer, nullable=False, unique=False)
    capacite_salle = Column(Integer, nullable=False, unique=False)
    numero_siege = Column(Integer, nullable=False, unique=False)


class Resa(db.Model):
    id_client = Column(Integer, nullable=False, unique=True, primary_key=True)
    nom_client = Column(String(30), nullable=False, unique=False)
    prenom_client = Column(String(30), nullable=False, unique=False)
    siege_reserver = Column(Integer, ForeignKey("Salle.numero_siege"), nullable=False, unique=False)
    seance_resa = Column(Integer, ForeignKey("Seance.id_seance"), nullable=False, unique=False)
    date_resa = Column(DateTime, nullable=False)


# Est-ce qu'il faut un compte ?
# class User(db.Model):
#     """Il faut un compte afin de pouvoir réserver une place de cinéma"""
#     pass
