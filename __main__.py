import v1
import v2
from lista_nomes import LISTA_DE_NOMES


for i, func in enumerate([v1.nome_bebê, v2.nome_bebê], 1):
    print(f'v{i}'.center(50, '='))
    for gênero in ['masculino', 'feminino', 'neutro']:
        print(gênero.center(30,'-'))
        print(
            func('da Silva', gênero, LISTA_DE_NOMES)
        )
