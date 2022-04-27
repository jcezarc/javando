def nome_bebê(método: callable, gênero, sugestões: dict) -> str:
    return método(sugestões[gênero])
