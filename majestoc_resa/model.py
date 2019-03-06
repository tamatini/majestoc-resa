from majestoc_resa import db


class Film(db.Model):
    """Modele d'un film avec son nom et sa durée"""
    id_film = db.Column(db.Integer, nullable=False, unique=False, primary_key=True)
    nom_film = db.Column(db.String(30), nullable=False, unique=False)
    nombre_place = db.Column(db.Integer, nullable=False, unique=True)
    duree_film = db.Column(db.Integer, nullable=False, unique=False)


class Seance(db.Model):
    """Item du planning des séances"""
    id_seance = db.Column(db.Integer, nullable=False, unique=True, primary_key=True)
    film = db.Column(db.String, db.ForeignKey("film.nom_film"), unique=False, nullable=False)
    date_debut = db.Column(db.String(10), nullable=False, unique=False)
    date_fin = db.Column(db.String(10), nullable=False, unique=False)
    duree_seance = db.Column(db.Integer, nullable=False, unique=False)


class Salle(db.Model):
    """Item du planning des salles"""
    id_cinema = db.Column(db.Integer, nullable=False, unique=True, primary_key=True)
    cinema = db.Column(db.String(15), nullable=False, unique=True)
    numero_salle = db.Column(db.Integer, nullable=False, unique=False)
    capacite_salle = db.Column(db.Integer, nullable=False, unique=False)
    numero_siege = db.Column(db.Integer, nullable=False, unique=False)


class Resa(db.Model):
    id_client = db.Column(db.Integer, nullable=False, unique=True, primary_key=True)
    nom_client = db.Column(db.String(30), nullable=False, unique=False)
    prenom_client = db.Column(db.String(30), nullable=False, unique=False)
    siege_reserver = db.Column(db.Integer, db.ForeignKey("salle.numero_siege"), nullable=False, unique=False)
    seance_resa = db.Column(db.Integer, db.ForeignKey("seance.id_seance"), nullable=False, unique=False)
    date_resa = db.Column(db.DateTime, nullable=False)


# Est-ce qu'il faut un compte ?
# class User(db.Model):
#     """Il faut un compte afin de pouvoir réserver une place de cinéma"""
#     pass
