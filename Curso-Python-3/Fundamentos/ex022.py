n = input('Digite o nome:')
n = n.strip()
print('O nome fica:\n'
      f'Em maiúsculo: {n.upper()}\n'
      f'Em minúsculo: {n.lower()}\n'
      f'Em forma de título: {n.title()}\n'
      f'E com apenas a primeira letra maiúscula: {n.capitalize()}')

print('\nAlém de que, se tratando de vogais, possui:\n'
      f'({n.lower().count('a')}) letras A!\n'
      f'({n.lower().count('e')}) letras E!\n'
      f'({n.lower().count('i')}) letras I!\n'
      f'({n.lower().count('o')}) letras O!\n'
      f'({n.lower().count('u')}) letras U!')

n = n.split()

print(f'O nome completo possui {len(''.join(n))} letras\n'
      f'O primeiro nome, {n[0]}, possui {len(n[0])} letras!')