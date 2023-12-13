from time import  sleep
print(f'\033[1;33m{'-==-'*15}\nANALISADOR DE TRIÂNGULOS\n{('-==-')*15}')
sleep(2)
r1=int(input('Digite o comprimento da 1º reta:'))
r2=int(input('Comprimento da 2º reta:'))
r3=int(input('Comprimento da 3º reta:'))
print(('-==-')*15)
sleep(2)

if (r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2):
    print('Sim é possível criar um triângulo com estas retas!')
else:
    print('Não é possível criar um triângulo com estas retas!!')