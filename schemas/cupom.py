from pydantic import BaseModel
from typing import Optional, List
from model.cupom import Cupom



class CupomSchema(BaseModel):
    """ Define como um novo cupom a ser inserida deve ser representado
    """
    id: int = 1
    nome: str = "Banana Prata"
    valor: float = 12.50


class CupomBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do cupom.
    """
    nome: str = "Teste"


class ListagemCuponsSchema(BaseModel):
    """ Define como uma listagem de cupons será retornada.
    """
    cupons:List[CupomSchema]


def apresenta_produtos(cupons: List[Cupom]):
    """ Retorna uma representação do cupom seguindo o schema definido em
        CupomViewSchema.
    """
    result = []
    for cupom in cupons:
        result.append({
            "id": cupom.id,
            "nome": cupom.nome,
            "valor": cupom.valor,
        })

    return {"Cupons": result}


class CupomViewSchema(BaseModel):
    """ Define como uma cupom será retornada: cupom.
    """
    id: int = 1
    nome: str = "Banana Prata"
    valor: float = 12.50



class CupomDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    message: str
    nome: str

def apresenta_produto(cupom: Cupom):
    """ Retorna uma representação do cupom seguindo o schema definido em
        CupomViewSchema.
    """
    return {
        "id": cupom.id,
        "nome": cupom.nome,
        "valor": cupom.valor
    }
