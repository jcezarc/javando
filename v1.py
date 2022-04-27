from random import choice
# --------------------------------
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Text
) # <<-------- PRA QUE ISSO?!?!?!


def nome_bebê(sobrenome: Text, gênero: Any, sugestões: Dict) -> Text:
    #  ECA! ---------------------------^^
    nome = choice(sugestões[gênero])
    return f'{nome} {sobrenome}'
