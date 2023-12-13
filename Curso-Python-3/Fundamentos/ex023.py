n = int(input('Digite um número:'))

u = n//1%10
d = n//10%10
c = n//100%10
m = n//1000%10

print(f'Analisando o número {n} temos que:\n'
      f'({u}) É UNIDADE\n'
      f'({d}) É DEZENA\n'
      f'({c}) É CENTENA\n'
      f'({m}) É MILHAR')