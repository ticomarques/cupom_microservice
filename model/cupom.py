from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base


class Cupom(Base):
    __tablename__ = 'cupom'

    id = Column("pk_cupom", Integer, primary_key=True)
    nome = Column(String(140))
    valor = Column(Float)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome:str, valor:float, data_insercao:Union[DateTime, None] = None):
        """
        Cria um cupom

        Arguments:
            nome: nome do produto para entrar na cupom.
            valor: valor do desconto.
            data_insercao: data de quando o cupom foi inserida no sistema

            exemplo de corpo de requisição (JSON):
            {
                nome: "CUPOM10%",
                valor: 0.9
            }

        """
        self.nome = nome
        self.valor = valor

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

