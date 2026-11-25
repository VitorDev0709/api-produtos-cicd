# API de Cadastro de Produtos

Projeto final de DevOps e Entregas Contínuas: Python + FastAPI + pytest + GitHub Actions + GitHub Pages.

## Execução no Windows

Abra a pasta no VS Code e execute no terminal PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest -v
.\.venv\Scripts\python.exe -m build
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

Acesse http://127.0.0.1:8000/docs para testar a API. Dados em memória são perdidos ao reiniciar.

## Entrega

O Pages publica a documentação Swagger estática e os pacotes de distribuição; não executa o servidor Python. Confirme a aceitação dessa entrega com o professor.

## GitHub

Consulte GUIA.md para configuração do repositório, proteção da main e demonstração.

## Integrantes

Preencher com os nomes dos integrantes.
