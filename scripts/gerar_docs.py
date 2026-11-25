import json
import shutil
from pathlib import Path
from fastapi.openapi.docs import get_swagger_ui_html
from app.main import app

site = Path('site')
site.mkdir(exist_ok=True)
(site / 'openapi.json').write_text(json.dumps(app.openapi(), ensure_ascii=False, indent=2), encoding='utf-8')
html = get_swagger_ui_html(openapi_url='./openapi.json', title=app.title, swagger_ui_parameters={'supportedSubmitMethods': []}).body.decode('utf-8')
aviso = '''<div style="background:#e8f0fe;padding:20px;font-family:Arial">
<h2>API de Cadastro de Produtos</h2><p>Documentação publicada automaticamente via CI/CD.</p>
<p>Esta página é estática. Execute o servidor FastAPI localmente para testar requisições.</p>
<a href="./pacotes.html">Baixar aplicação</a></div>'''
(site / 'index.html').write_text(html.replace('<body>', '<body>' + aviso), encoding='utf-8')
destino = site / 'downloads'
destino.mkdir(exist_ok=True)
links = []
for arquivo in sorted(Path('dist').iterdir()):
    if arquivo.is_file():
        shutil.copy2(arquivo, destino / arquivo.name)
        links.append(f'<li><a href="downloads/{arquivo.name}">{arquivo.name}</a></li>')
(site / 'pacotes.html').write_text('<!doctype html><html lang="pt-BR"><meta charset="utf-8"><title>Downloads</title><h1>Downloads da aplicação</h1><ul>' + ''.join(links) + '</ul><p>Instale o arquivo .whl com python -m pip install NOME_DO_ARQUIVO.whl e execute python -m uvicorn app.main:app.</p><a href="index.html">Voltar</a></html>', encoding='utf-8')
(site / '.nojekyll').touch()
print('Documentação gerada com sucesso!')
