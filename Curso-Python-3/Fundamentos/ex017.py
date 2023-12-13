from math import hypot

'''co=float(input('Qual a medida do cateto oposto?'))
ca=float(input('Qual a medida do cateto adjacente?'))
print(f'O triângulo de A={(co*ca)/2:.2f}², tem uma hipotenusa de {((co**2)+(ca**2))**(1/2):.2f}')'''

co=float(input('Digite o comprimento do cateto oposto:'))
ca=float(input('Digite o comprimento do cateto adjacente:'))
print(f'A hipotenusa é igual a {hypot(co,ca):.2f}!')