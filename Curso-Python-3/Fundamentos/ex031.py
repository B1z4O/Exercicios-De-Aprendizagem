# O Valor da viagem é de R$0.50 para cada km de distância, a partir de 200km se ganha um desconto e o valor passa a ser de R$0.45 por km.

v=float(input('Qual é a distância de viagem?'))

if v <= 200:
    print(f'O valor da viagem custará R${v * 0.50:.2f}!')

else:
    print(f'Para viagens acima de R$200.00 temos desconto! Sua viagem custará R${v * 0.45:.2f}!')