frase=input('Digite uma frase:').strip().upper()
letra=input('Escolha uma letra:').strip().upper()

print(f'Nesta frase a letra A aparece ({frase.count(letra)}) vezes!\n'
      f'Pela primeira vez na posição ({frase.find(letra)+1})\n'
      f'E Pela última vez na posição ({frase.rfind(letra)+1})')