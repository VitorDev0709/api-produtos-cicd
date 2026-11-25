from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title='API de Cadastro de Produtos', description='Projeto de CI/CD com GitHub Actions', version='1.0.0')

class Produto(BaseModel):
    nome: str = Field(min_length=1)
    preco: float = Field(gt=0)
    quantidade: int = Field(ge=0)

produtos = {}
proximo_id = 1

@app.get('/')
def inicio():
    return {'mensagem': 'API de Produtos funcionando'}

@app.get('/produtos')
def listar_produtos():
    return list(produtos.values())

@app.get('/produtos/{id}')
def consultar_produto(id: int):
    if id not in produtos:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    return produtos[id]

@app.post('/produtos', status_code=201)
def cadastrar_produto(produto: Produto):
    global proximo_id
    novo = {'id': proximo_id, **produto.model_dump()}
    produtos[proximo_id] = novo
    proximo_id += 1
    return novo

@app.put('/produtos/{id}')
def atualizar_produto(id: int, produto: Produto):
    if id not in produtos:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    produtos[id] = {'id': id, **produto.model_dump()}
    return produtos[id]

@app.delete('/produtos/{id}')
def excluir_produto(id: int):
    if id not in produtos:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    del produtos[id]
    return {'mensagem': 'Produto excluído com sucesso'}
