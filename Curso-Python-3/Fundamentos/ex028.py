from random import randint       # importação do método 'radint' da tabela 'random' (que escolhe algo aleatóriamente).
from time import sleep           # outro importação, método sleep (faz o computador "dormir" alguns segundos antes de printar uma string).

print(f'{'-==-' * 14} \nVou pensar em um número entre 0 e 5. Tente adivinhar!\n{'-==-' * 14}')      # Uma string comum, '{'-==-' * 10}' não é necessário, é apenas uma decoração para o console).
n=int(input('Em que número eu pensei?'))                               # Variável para escolher um número de 0 a 5.
a=randint(0, 5)                                  # Aqui utilizamos nosso método 'radint' para sortear um número(inteiro) entre 0 e 5.
print('(PROCESSANDO..)')                                 # Mais um item desnecessário, apenas para um charme do código no console.
sleep(2)                                      # Aqui utilizamos o sleep, para complementar o charme do código acima.

if a == n:                                                 # Aqui uma condição, diz que se nosso número aleatório (sorteado no 'radint') for igual ao número escolhido (variável 'n') dá o seguinte print:
    print(f'{'-==-' * 14}\nDroga eu perdi! Eu pensei no número {a}\n{'-==-' * 14}')

else:                                                      # Caso o os números nas variáveis 'a' (sorteado) e 'n' (escolhido) sejam diferentes, o programa dá o seguinte print:
    print(f'{'-==-' * 14}\nHahaha ganhei! Pensei no número {a} e não no {n}!\n{'-==-' * 14}')
