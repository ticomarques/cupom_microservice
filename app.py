from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, request, jsonify
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Cupom
from logger import logger
from schemas import *
from flask_cors import CORS

from schemas.cupom import CupomDelSchema

info = Info(title="Cupom", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
cupom_tag = Tag(name="Cupom", description="CRUD de CUPOM")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/cupom', tags=[cupom_tag],
          responses={"200": CupomViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_produto(form: CupomSchema):
    """Adiciona um cupom 

    Retorna uma representação de cupom.
    {
        "nome": "TIAGO10",
        "valor": 0.9
    }

    """
    cupom = Cupom(
        nome = request.json['nome'],
        valor = request.json['valor'])
    logger.debug(f"Adicionando produto de nome: '{cupom.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando um cupom
        session.add(cupom)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado cupom de nome: '{cupom.nome}'")
        return apresenta_produto(cupom), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Cupom de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar cupom '{cupom.nome}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar cupom '{cupom.nome}', {error_msg}")
        return {"message": error_msg}, 400


@app.get('/cupom', tags=[cupom_tag],
         responses={"200": ListagemCuponsSchema, "404": ErrorSchema})
def get_produtos():
    """Faz a busca por todas os cupons cadastradas

    Retorna uma representação da listagem de cupons.
    """
    logger.debug(f"Coletando cupons")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    cupons = session.query(Cupom).all()

    if not cupons:
        # se não há cupons cadastrados
        return {"cupons": []}, 200
    else:
        logger.debug(f"%d Cupons econtradas" % len(cupons))
        # retorna a representação de produto
        print(cupons)
        return apresenta_produtos(cupons), 200


@app.get('/cupom', tags=[cupom_tag],
         responses={"200": CupomViewSchema, "404": ErrorSchema})
def get_produto(query: CupomBuscaSchema):
    """Faz a busca por um Cupom a partir do id de um CUPOM

    Retorna uma representação das Cupom e lances associados.
    """
    cupom_id = query.nome
    logger.debug(f"Coletando dados sobre produto #{cupom_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    cupom = session.query(Cupom).filter(Cupom.nome == cupom_id).first()

    if not cupom:
        # se o cupom não foi encontrado
        error_msg = "Cupom não encontrada na base :/"
        logger.warning(f"Erro ao buscar produto '{cupom_id}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Produto econtrado: '{cupom.nome}'")
        # retorna a representação da cupom
        return apresenta_produto(cupom), 200


@app.delete('/cupom', tags=[cupom_tag],
            responses={"200": CupomDelSchema, "404": ErrorSchema})
def del_produto(query: CupomBuscaSchema):
    """Deleta um cupom a partir do nome de cupom

    Retorna uma mensagem de confirmação da remoção.
    """
    cupom_nome = unquote(unquote(query.nome))
    logger.debug(f"Deletando dados sobre produto #{cupom_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Cupom).filter(Cupom.nome == cupom_nome).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado produto #{cupom_nome}")
        return {"message": "Produto removido", "id": cupom_nome}
    else:
        # se o produto não foi encontrado
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao deletar produto #'{cupom_nome}', {error_msg}")
        return {"message": error_msg}, 404

