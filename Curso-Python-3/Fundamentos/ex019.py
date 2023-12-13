from random import choice
a1=input('Digite o nome do primeiro aluno:')
a2=input('Do segundo:')
a3=input('Terceiro:')
a4=input('Quarto e último:')
lista=[a1,a2,a3,a4]
print(f'O aluno escolhido foi {choice(lista)}!')