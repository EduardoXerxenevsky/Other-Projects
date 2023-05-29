import random

vetorPalavras = ['abacaxi', 'banana', 'laranja', 'limao', 'uva', 'manga', 'morango', 'melancia']
palavraEscolhida = random.choice(vetorPalavras)
letraErrada = []
letraCerta = []

while True:
    print('Adivinhe a palavra secreta:')
    
    for letra in palavraEscolhida:
        if letra in letraCerta:
            print(letra, end=' ')
        else:
            print('_', end='')
    
    print('\n')
    
    palpite = input('Digite uma letra: ').lower()
    
    if palpite in letraCerta or palpite in letraErrada:
        print('Você já tentou essa letra. Tente novamente.')
    elif palpite in palavraEscolhida:
        letraCerta.append(palpite)
        print('Letra correta!')
        
        if len(letraCerta) == len(set(palavraEscolhida)):
            print('Parabéns! Você adivinhou a palavra secreta!')
            break
    else:
        letraErrada.append(palpite)
        print('Letra incorreta!')
        
        if len(letraErrada) == 6:
            print('Você perdeu! A palavra secreta era', palavraEscolhida)
            break