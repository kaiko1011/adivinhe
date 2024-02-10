import random
import os
import time
erros = 0
jogador = 0
sorteado = random.randrange(0,100)
print("\'Bem vindo ao jogo de adivinhação!!\'\n\n")
while(sorteado != jogador ) :
    try:
        jogador = int(input("    Digite seu numero : ")) 
    except ValueError:
        print(" \n          Digite apenas numeros")
        time.sleep(2)
        os.system('cls')
        continue
    erros += 1    
    os.system('cls')
    if(sorteado == jogador):
        print("---------------------------------------------------------------------\n")
        print(f"Parabens o numero sorteado é o {jogador} , você acertou em  {erros}  tentativas")
    elif(sorteado < jogador) :
        print("\nErro o numero é menor\n")
    else:
        print("\nErro o numero é maior \n")

 


