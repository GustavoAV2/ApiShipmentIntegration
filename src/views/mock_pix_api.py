from uuid import uuid4
from src.views.api import app
from fastapi import Header, HTTPException, Body


def _verify_token(token: str):
    # Aqui você pode implementar a lógica de validação do token
    # por exemplo, verificar se o token é válido no seu sistema de autenticação
    valid_tokens = ["TOKEN1", "TOKEN2"]  # Tokens válidos

    if token not in valid_tokens:
        raise HTTPException(status_code=401, detail="Token inválido")
    return True


@app.route('oauth/token')
def request_token(payload=Body(...)):
    if payload:
        return uuid4()
    return {"message": "Credenciais invalidas!"}


@app.get("/cob")
def request_post_billing(authorization: str = Header(...), payload=Body(...)):
    try:
        if _verify_token(authorization):
            return open('../../example_data/response_cob.json', 'r')
    except HTTPException as e:
        raise e
