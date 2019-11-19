
__author__      = "José Elias"
__copyright__   = "Elias Gomes @ 2019"
__contact__     = "eliaspbareia@gmail.com"
__license__     = "MIT"
__version__     = "01.000"
from peewee import SQL

class Dataset:

    @staticmethod
    def selectbyid(model, id):
        return model.select().where(model.id == id)

    @staticmethod
    def search(model, field, text):
        return model.select().where(model.nomeperson.contains(text))


    @staticmethod
    def select(model):
        """
        Faz a seleção de todos os registros do BD e retorna os mesmos
        """
        return model.select()

    @staticmethod
    def update(model, registros):
        """
        :param model: contém o modelo de dados de onde serão excluídas as colunas
        :param registros: contém todos os registros a serem atualizadaos no bd
        :return: retorno 0:False 1:True ou erros
        """
        id = registros['id']
        del registros['id']
        try:
            row = model.update(registros).where(model.id == id)
        except Exception as e:
            return e
        else:
            return row.execute()


    @staticmethod
    def insert(model, registros):
        """
        :param model: o modelo do banco de dados
        :param registros: uma lista de registros a serem inseridos
        :return: retorna o valor do index do registro inserido
        """
        try:
           retorno = model.create(**registros)
        except Exception as e:
            return e

        else:
            return retorno


    @staticmethod
    def delete(model, id):
        """
        :param model: o modelo do banco de dados
        :param id: o index da linha a ser deletada
        :return: retorna 1:True, 0: False
        """
        retorno = model.delete().where(model.id == id)
        return retorno.execute()
