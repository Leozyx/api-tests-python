import random
import string


def generate_random_post():
    """Gera payload aleatório para criação de post"""

    # Gera uma string aleatória com 6 letras (maiúsculas e minúsculas)
    # usando random.choices e o conjunto string.ascii_letters
    title = "QA Test " + ''.join(random.choices(string.ascii_letters, k=6))

    # Gera corpo da mensagem com 12 letras aleatórias
    body = "Automated test body " + ''.join(random.choices(string.ascii_letters, k=12))

    # Gera um userId aleatório entre 1 e 10
    # (jsonplaceholder possui usuários nesse intervalo)
    user_id = random.randint(1, 10)

    # Retorna o payload no formato esperado pela API
    return {
        "title": title,
        "body": body,
        "userId": user_id
    }
