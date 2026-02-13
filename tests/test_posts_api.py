import requests
import pytest
from utils.data_generator import generate_random_post

# URL base do endpoint que será testado
BASE_URL = "https://jsonplaceholder.typicode.com/posts"


@pytest.fixture
def session():
    """Sessão HTTP reutilizável"""

    # Cria uma sessão HTTP reutilizável.
    # Isso melhora performance e organização,
    # pois mantém configurações e conexões abertas.
    return requests.Session()


def test_get_posts(session):
    """Valida endpoint GET /posts"""

    # Realiza requisição GET para listar posts
    response = session.get(BASE_URL)

    # Valida se o status HTTP é 200 (sucesso)
    assert response.status_code == 200, "GET /posts falhou"

    # Converte resposta para JSON (lista de posts)
    data = response.json()

    # Valida se a resposta é uma lista
    assert isinstance(data, list), "Resposta não é uma lista"

    # Garante que não veio vazia
    assert len(data) > 0, "Lista vazia"

    # Pega o primeiro post para validar estrutura
    post = data[0]

    # Valida se os campos obrigatórios existem
    assert "id" in post
    assert "title" in post
    assert "body" in post
    assert "userId" in post


def test_create_post(session):
    """Valida endpoint POST /posts"""

    # Gera payload dinâmico usando função utilitária
    # Boa prática para evitar dados fixos
    payload = generate_random_post()

    # Envia requisição POST com corpo em JSON
    response = session.post(BASE_URL, json=payload)

    # Valida se status é 200 ou 201 (API fake aceita ambos)
    assert response.status_code in [200, 201], "POST falhou"

    # Converte resposta para JSON
    data = response.json()

    # =============================
    # Validação de contrato da API
    # =============================

    # Verifica se os dados enviados retornaram corretamente
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

    # =============================
    # Validação do ID gerado
    # =============================

    # Confirma que a API retornou um ID
    assert "id" in data, "ID não retornado"

    # Confirma que o ID é do tipo inteiro
    assert isinstance(data["id"], int), "ID não é inteiro"

# ==================================
# TESTES NEGATIVOS (robustez da API)
# ==================================

def test_get_invalid_endpoint(session):
    """Deve retornar 404 ao acessar recurso inexistente"""

    # Faz requisição para um ID extremamente alto
    # que não existe na API
    response = session.get(f"{BASE_URL}/999999")

    # Valida que a API responde corretamente com 404 (Not Found)
    # Isso confirma que o endpoint trata recursos inexistentes
    assert response.status_code == 404

def test_post_with_invalid_payload(session):
    """POST com dados inválidos deve ser tratado pela API"""

    # Cria payload com tipos incorretos
    invalid_payload = {
        "title": None,      # inválido
        "body": 12345,      # tipo errado
        "userId": "abc"     # tipo errado
    }

    # Envia requisição com payload inválido
    response = session.post(BASE_URL, json=invalid_payload)

    # JSONPlaceholder é uma API mock e aceita quase tudo.
    # Em uma API real, o esperado seria 400 (Bad Request).
    # Aqui aceitamos 200/201 por ser fake.
    assert response.status_code in [200, 201, 400]

    # Converte resposta
    data = response.json()

    # Mesmo com erro, API deve retornar JSON válido
    assert isinstance(data, dict)

    # API fake sempre gera ID, então validamos isso
    assert "id" in data


def test_method_not_allowed(session):
    """DELETE sem ID específico deve retornar erro ou comportamento inesperado"""

    # Envia DELETE sem especificar ID
    response = session.delete(BASE_URL)

    # Como a API é mock, pode retornar 200 ou 404.
    # Em uma API real, o ideal seria 405 (Method Not Allowed).
    assert response.status_code in [200, 404]
