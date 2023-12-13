v=float(input('Qual é a velocidade atual do carro?'))              # Está variável irá guardar a velocidade do carro.

if v <= 80.0:                                                   # Nesta condição temos, se a velocidade (v) for menor (<) ou igual (=) a 80km/h ele irá printar:
    print('Muito bem! Dirija com segurança!')

else:                                                         # Caso a velocidade (v) seja maior que 80km/h, ele irá pagar uma multa de R$7.00 por km excedido.
    print(f'Você foi multado! Sua multa será no valor de R${(v - 80) * 7:.2f}!')            # (v - 80) * 7 == a velocidade atual menos os 80km permitidos, para assim multiplicar os km restantes por 7.