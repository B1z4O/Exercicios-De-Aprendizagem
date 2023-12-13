a=input('Olá, digite algo:')

print('É do tipo primitivo', (type(a)))
print('É todo escrito em maiúsculo?', (a.isupper()))
print('É todo escrito em minúsculo?', (a.islower()))
print('É apenas alfabético?', (a.isalpha()))
print('É apenas numérico?', (a.isnumeric()))
print('É alfanumérico?', (a.isalnum()))
print('É um espaço em branco?', (a.isspace()))