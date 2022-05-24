import json
from flask import request
from flask_restful import Resource

lista_habilidades = ['Python', 'Java', 'Flask', 'PHP', 'Django', 'C++']


class Lista_Habilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        try:
            nova_habilidade = json.loads(request.data)
            lista_habilidades.append(nova_habilidade)
            return {'status': 'sucesso', 'mensagem': 'Registro inserido com sucesso!'}
        except Exception as e:
            return {'status': 'erro', 'mensagem': 'Erro desconhecido'}


class Habilidades(Resource):
    def put(self, id):
        try:
            habilidade = json.loads(request.data)
            lista_habilidades[id] = habilidade
            return lista_habilidades
        except IndexError as e:
            return {'status': 'erro', 'mensagem': f'Não existe habilidade com id {id}'}
        except Exception as e:
            return {'status': 'erro', 'mensagem': 'Erro desconhecido'}

    def delete(self, id):
        try:
            lista_habilidades.pop(id)
            return {'status': 'sucesso', 'mensagem': 'Registro excluido com sucesso!'}
        except IndexError as e:
            return {'status': 'erro', 'mensagem': f'Não existe habilidade com id {id}'}
        except Exception as e:
            return {'status': 'erro', 'mensagem': 'Erro desconhecido'}
