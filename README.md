# Cardapio Digital - Flask

Aplicacao web de cardapio digital para pizzaria, construida com Flask seguindo uma arquitetura modular baseada em features.

## Tech Stack

- **Python 3** + **Flask**
- **Flask-SQLAlchemy** (SQLite)
- **Flask-Login** (autenticacao)
- **Flask-WTF** (formularios com validacao)
- **Bootstrap 5.3.8** (frontend)

## Como Iniciar

```bash
# 1. Criar e ativar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Rodar a aplicacao
python run.py
```

A aplicacao roda em `http://127.0.0.1:5000`. O banco de dados SQLite e criado automaticamente em `instance/app.db` na primeira execucao.

## Arquitetura

O projeto usa o **Application Factory Pattern** do Flask com **Blueprints organizados por feature**.

### Estrutura de Pastas

```
Cardapio-Digital---Flask/
├── run.py                  # Entrypoint da aplicacao
├── requirements.txt
├── app/
│   ├── __init__.py         # Application Factory (create_app)
│   ├── config.py           # Configuracoes (SECRET_KEY, DB)
│   ├── extensions.py       # Instancias compartilhadas (db, login_manager)
│   │
│   ├── shared/             # Layout global
│   ├── home/               # Pagina inicial
│   ├── auth/               # Login, logout, cadastro
│   ├── pizzas/             # Cardapio de pizzas (5 sub-paginas)
│   ├── drinks/             # Bebidas
│   ├── promotion/          # Promocoes
│   ├── score/              # Pontuacao
│   ├── categories/         # CRUD de categorias
│   └── dashboard/          # Painel (area protegida)
│
├── mocks/
│   └── images/             # Imagens temporarias (serao substituidas por API)
│
└── instance/
    └── app.db              # Banco SQLite (auto-gerado)
```

### Como Funciona um Blueprint (Feature)

Cada feature segue o mesmo padrao:

```
app/<feature>/
├── __init__.py              # Define o Blueprint
├── routes.py                # Rotas/endpoints
├── models.py                # Modelos do banco (quando necessario)
├── forms.py                 # Formularios WTForms (quando necessario)
└── templates/<feature>/
    ├── pagina.html          # Template Jinja2
    └── pagina.css           # CSS da pagina (mesmo nome do HTML)
```

**HTML e CSS ficam juntos** na mesma pasta com o mesmo nome. Isso facilita a manutencao — para alterar uma pagina, voce mexe em apenas uma pasta.

### Application Factory

O `app/__init__.py` contem a funcao `create_app()` que:

1. Cria a instancia Flask
2. Carrega as configuracoes (`Config`)
3. Inicializa as extensoes (`db`, `login_manager`)
4. Registra todos os Blueprints com seus prefixos de URL
5. Cria as tabelas do banco (`db.create_all()`)

### Como o CSS Funciona

O projeto usa um sistema de CSS em duas camadas:

1. **CSS Global** (`app/shared/templates/shared/base.css`) — Estilos compartilhados: fundo, navbar, footer, tipografia. Carregado automaticamente pelo `base.html`.

2. **CSS por Pagina** — Cada pagina tem seu proprio arquivo CSS, carregado pelo bloco `{% block extra_css %}`:

```html
{% extends "shared/base.html" %}

{% block extra_css %}
<link rel="stylesheet" href="{{ url_for('pizzas.static', filename='pizzas/traditional.css') }}">
{% endblock %}
```

### Rotas

| URL | Descricao |
|-----|-----------|
| `/` | Pagina inicial com combos |
| `/auth/login` | Login |
| `/auth/logout` | Logout |
| `/auth/register` | Cadastro de usuario |
| `/pizzas/` | Listagem de pizzas |
| `/pizzas/traditional` | Pizzas tradicionais |
| `/pizzas/artisan` | Pizzas artesanais |
| `/pizzas/half` | Pizzas metade-metade |
| `/pizzas/sweet` | Pizzas doces |
| `/drinks/` | Bebidas |
| `/promotion/` | Promocoes |
| `/score/` | Pontuacao |
| `/categories/` | Gerenciar categorias |
| `/dashboard/` | Painel do usuario (requer login) |

### Modelos do Banco

- **User** (`app/auth/models.py`) — Usuarios com email, senha (hash), telefone, endereco
- **Category** (`app/categories/models.py`) — Categorias com tipo (Pizzas/Bebidas)
- **PizzaDoce** (`app/pizzas/models.py`) — Pizzas doces com preco, descricao, imagem e categoria

### Imagens (Mocks)

As imagens ficam em `mocks/images/` e sao servidas como arquivos estaticos do Flask. Essa pasta e temporaria — no futuro, as imagens virao de uma API e a pasta `mocks/` sera removida.

## Como Adicionar Uma Nova Feature

1. Criar a pasta `app/<feature>/`
2. Criar `__init__.py` com o Blueprint:
```python
from flask import Blueprint
import os

template_dir = os.path.join(os.path.dirname(__file__), 'templates')

feature_bp = Blueprint(
    'feature', __name__,
    template_folder=template_dir,
    static_folder=template_dir,
    static_url_path='/feature/static'
)

from . import routes
```
3. Criar `routes.py`, `templates/<feature>/pagina.html` e `pagina.css`
4. Registrar o Blueprint em `app/__init__.py`:
```python
from .feature import feature_bp
app.register_blueprint(feature_bp, url_prefix='/feature')
```
