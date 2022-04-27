# --------------------------------
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Text
) # <<-------- PRA QUE ISSO?!?!?!


def nome_bebê(método: Callable, gênero: Any, sugestões: Dict[str, List]) -> Text:
    #  ECA! ---------------------------^^
    return método(sugestões[gênero])
