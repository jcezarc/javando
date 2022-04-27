from random import choice
import v1
import v2
from lista_nomes import LISTA_DE_NOMES

print(v1.nome_bebê(random, 'masculino', LISTA_DE_NOMES))
print(v1.nome_bebê(random, 'feminino', LISTA_DE_NOMES))
print(v1.nome_bebê(random, 'neutro', LISTA_DE_NOMES))
print('-'*30)
print(v2.nome_bebê(random, 'masculino', LISTA_DE_NOMES))
print(v2.nome_bebê(random, 'feminino', LISTA_DE_NOMES))
print(v2.nome_bebê(random, 'neutro', LISTA_DE_NOMES))
