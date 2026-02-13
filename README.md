🧪 API Tests – JSONPlaceholder

Automação de testes de API utilizando Python + Pytest + Requests

📌 Sobre o Projeto

Este projeto contém testes automatizados para a API pública JSONPlaceholder, validando:

Endpoints GET

Endpoints POST

Cenários positivos

Cenários negativos

Validação de estrutura da resposta

Geração dinâmica de payload

O objetivo é praticar boas práticas de API Testing, organização de código e estrutura de projeto.

🚀 Tecnologias Utilizadas

Python 3.9+

Pytest

Requests

JSONPlaceholder API

🗂 Estrutura do Projeto
API-TESTS_PYTHON
│
├── tests/
│   ├── __init__.py
│   └── test_posts_api.py
│
├── utils/
│   ├── __init__.py
│   └── data_generator.py
│
├── venv/
├── requirements.txt
└── README.md


🔧 Instalação

1️⃣ Clonar o repositório
git clone <https://github.com/Leozyx/api-tests-python.git>

cd API-TESTS_PYTHON

2️⃣ Criar ambiente virtual (recomendado)
python -m venv venv


Ativar ambiente virtual:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate


3️⃣ Instalar dependências
pip install -r requirements.txt


▶️ Executando os Testes

Rodar todos os testes:

pytest

Rodar com saída detalhada:

pytest -v

🧪 Testes Implementados
✅ Testes Positivos

GET /posts

Status 200

Retorno em lista

Lista não vazia

Validação de campos obrigatórios

POST /posts

Status 200/201

Retorno dos dados enviados

Geração de ID

Validação de tipo do ID

❌ Testes Negativos

GET com recurso inexistente (404)

POST com payload inválido

DELETE sem ID específico

Observação: A API JSONPlaceholder é mock e aceita praticamente qualquer payload.
Em APIs reais, seriam esperados retornos mais restritivos (ex: 400, 405).

🎯 Boas Práticas Aplicadas

Uso de pytest fixtures

Separação de responsabilidade (testes vs geração de dados)

Geração de dados dinâmicos

Validação estrutural da resposta

Organização modular do projeto

🌐 API Utilizada

https://jsonplaceholder.typicode.com
