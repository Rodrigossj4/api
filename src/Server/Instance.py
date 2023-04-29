from flask import Flask , jsonify, request
from flask_restx import Api, Resource


class Server():
    def __init__(self,):
     self.app = Flask(__name__)
     self.api = Api(self.app,
                    version='1.0',
                    title='Cadastro Produtos e Fornecedores',
                    description='Cadastro Produtos e Fornecedores',
                    doc='/docs')
     
     def run(self):
         self.app.run(
             debug = True
         )
         

server = Server()
