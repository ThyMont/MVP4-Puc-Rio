from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
# from urllib.parse import unquote

# from sqlalchemy.exc import IntegrityError

# from model import *
# # from logger import logger
# from schemas.game_schema import GamePath, MatchSchema
# from schemas.error import ErrorSchema
# from service import *
from flask_cors import CORS

from schemas.form import StressForm
from service.checkstress import predict_stress

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

home_tag = Tag(name="Documentação",
               description="Seleção de documentação: Swagger, Redoc ou RapiDoc")


@app.get('/', tags=[home_tag])
@app.get('/home', tags=[home_tag])
@app.get('/index', tags=[home_tag])
def home():
    """
    Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/teststress')
def test_stress(form: StressForm):
    return predict_stress(form)
