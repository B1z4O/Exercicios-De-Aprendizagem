cidade=input('Em qual cidade você nasceu?').strip().lower().split()
cidade=cidade[0] #Para considerar apenas o primeiro nome no caso de nomes compostos (Rio de Janeiro, Santo André, São Paulo, etc.

if 'santo' in cidade and len(cidade) == 5: #Neste caso o len só vai deixar o nome passar se tiver exatas 5 letras, impedindo assim de confundir 'Santos'(6 letras) com 'Santo'(5 letras)!
    print('Está correto, você mora em Santo André!')
else:
    print('Está errado, está não é sua cidade!')