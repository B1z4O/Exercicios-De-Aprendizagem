'''
    Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.

    Write a program that asks for an employee's salary and calculates the amount of his raise.
For salaries above R$1,250.00, calculate an increase of 10%.
For those inferior or equal, the increase is 15%.
'''

s=float(input('Qual é o salário do funcionário? R$'))
if s > 1250:
    print(f'O salário passará a ser {s+(s*(10/100)):.2f}')
else:
    print(f'O salário passará a ser {s+(s*(15/100)):.2f}')