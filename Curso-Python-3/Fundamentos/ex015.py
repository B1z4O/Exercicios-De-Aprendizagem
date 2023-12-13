d=int(input('Quantos dias ficou com o carro?'))
km=float(input('Quantos Km andou com o carro?'))
pg=(d*60)+(km*0.15)
print(f'O valor do aluguel do carro ficou R${pg:.2f}!')