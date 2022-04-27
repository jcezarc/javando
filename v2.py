from random import choice

def nome_bebê(sobrenome: str, gênero, sugestões: dict) -> str:
    nome = choice(sugestões[gênero])
    return f'{nome} {sobrenome}'
