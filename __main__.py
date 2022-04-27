from random import choice
import v1
import v2
from lista_nomes import LISTA_DE_NOMES

print(v1.nome_bebê(choice, 'masculino', LISTA_DE_NOMES))
print(v1.nome_bebê(choice, 'feminino', LISTA_DE_NOMES))
print(v1.nome_bebê(choice, 'neutro', LISTA_DE_NOMES))
print('-'*30)
print(v2.nome_bebê(choice, 'masculino', LISTA_DE_NOMES))
print(v2.nome_bebê(choice, 'feminino', LISTA_DE_NOMES))
print(v2.nome_bebê(choice, 'neutro', LISTA_DE_NOMES))
