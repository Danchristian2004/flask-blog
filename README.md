# Flask Blog

Um projeto simples de blog desenvolvido com Flask, HTML, CSS e Jinja2.

## Funcionalidades

- Listagem de posts na página inicial
- Página individual para cada post
- Rotas dinâmicas utilizando Flask
- Templates com Jinja2
- Estilização com CSS
- Consumo de API externa (npoint.io) para buscar os posts

## Tecnologias Utilizadas

- Python
- Flask
- HTML5
- CSS3
- Jinja2
- Requests

## Estrutura do Projeto

```text
flask-blog/
│
├── static/
│   └── css/
│       └── styles.css
│
├── templates/
│   ├── index.html
│   └── post.html
│
├── main.py
├── post.py
├── requirements.txt
└── README.md
```

## Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/flask-blog.git
```

Entre na pasta:

```bash
cd flask-blog
```

Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
python main.py
```

Acesse:

```text
http://127.0.0.1:5000
```

## Como funciona

- `post.py` busca os posts de uma API externa e os transforma em objetos `Post`.
- `main.py` define as rotas:
  - `/` lista todos os posts.
  - `/post/<int:index>` exibe o post correspondente ao id informado.
- Os templates em `templates/` usam Jinja2 para renderizar os dados dinamicamente.

## Aprendizados

Este projeto foi desenvolvido para praticar:

- Flask
- Rotas dinâmicas
- Templates Jinja2
- Consumo de APIs com `requests`
- Organização de projetos web em Python

## Autor

Danchristian Viecili
