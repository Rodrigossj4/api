from flask import Flask
from flask_restx import Resource
from src.Server.Instance import server


app,api =  server.app, server.api

secao_db = [
    {'id':1,'nome':'teste'},
    {'id':1,'nome':'teste'}
]

@api.route('/Secao')
class secao(Resource):
    def get(self,):
        return secao_db