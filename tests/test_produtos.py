import pytest
from fastapi.testclient import TestClient
from app import main

client = TestClient(main.app)

@pytest.fixture(autouse=True)
def limpar_dados():
    main.produtos.clear()
    main.proximo_id = 1

def criar_produto():
    return client.post('/produtos', json={'nome': 'Mouse', 'preco': 50.0, 'quantidade': 10})

def test_inicio():
    resposta = client.get('/')
    assert resposta.status_code == 200
    assert resposta.json()['mensagem'] == 'API de Produtos funcionando'

def test_cadastrar_produto():
    resposta = criar_produto()
    assert resposta.status_code == 201
    assert resposta.json()['nome'] == 'Mouse'
    assert resposta.json()['preco'] == 50.0

def test_listar_produtos():
    criar_produto()
    resposta = client.get('/produtos')
    assert resposta.status_code == 200
    assert len(resposta.json()) == 1

def test_consultar_produto_inexistente():
    assert client.get('/produtos/999').status_code == 404

def test_atualizar_produto():
    criar_produto()
    resposta = client.put('/produtos/1', json={'nome': 'Teclado', 'preco': 100.0, 'quantidade': 5})
    assert resposta.status_code == 200
    assert resposta.json()['nome'] == 'Teclado'

def test_excluir_produto():
    criar_produto()
    assert client.delete('/produtos/1').status_code == 200
    assert client.get('/produtos/1').status_code == 404

def test_preco_invalido():
    resposta = client.post('/produtos', json={'nome': 'Monitor', 'preco': -100.0, 'quantidade': 5})
    assert resposta.status_code == 422
