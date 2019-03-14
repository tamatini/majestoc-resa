# -*- coding: utf-8 -*
from flask_restplus import Resource, Namespace
from majestoc_resa.model import Film

api = Namespace('films', description='Les films')

LIST_FILMS = [
    {'nom': 'Star Wars Un Nouvel Espoir', 'duree': 120},
    {'nom': "Star Wars l'empire contre attaque", 'duree': 140}]


@api.route('/')
class FilmServiceList(Resource):
    def get(self):
        """Return film list"""
        return [{'nom_film': c.nom_film} for c in Film.query.all()]

    def post(self):
        """add new film"""


@api.route('/<string:film_id>')
class FilmService(Resource):
    def get(self, film_id):
        return [{'nom': c.nom_film, 'sypnosis': c.sypnosis} for c in Film.query.filter_by(nom_film=film_id)]


    def put(self, id):
        """modifier les détails de chaques film"""

