n=int(input('Digite um número qualquer:'))     # Variável que guarda o número escolhido

if n % 2 == 0:              # Diz que, se o número escolhido (n) em uma divisão por 2 tiver o resto igual a 0, é um número par, então vai dar o seguinte print:
    print(f'O número digitado ({n}) é PAR!')

else:                       # Caso o resto não seja igual a 0, é um número ímpar.
    print(f'O número digitado ({n}) é ÍMPAR!')