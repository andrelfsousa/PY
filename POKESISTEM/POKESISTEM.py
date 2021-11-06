#BY: ANDRÉ LUIZ FERREIRA DE SOUSA
##################################################################################### FUNÇÃO LINHA DE SEPARAÇÃO
def linha(tam = 42):
    return'-'* tam
##################################################################################### FUNÇÃO LINHA 2X
def linha2(tam = 42):
    return'='* tam
##################################################################################### FUNÇÃO CABEÇALHO
def cabeçalho(txt):
    print(txt.center(42))
##################################################################################### FUNÇÃO ERRO
def erro():
    print('\ERRO!')
    print('DIGITE 1 OU 2 !')
##################################################################################### FUNÇÃO TEMPO 
import time
def tempo2():
    time.sleep(1)
import time
def tempo3():
    time.sleep(3)
################################################################################### FUNÇÃO LISTA ORGANIZADA MENU
def menuorg():
    c = 1
    for item in menu:
          print(f'\033[1;33m{c} - {item}\033[0;0m')
          c+=1
################################################################################### FUNÇÃO LISTA ORGANIZADA POKE 1
def pokeorg():
    c = 1
    for item in pokemon:
          print(f'\033[1;34m{c}-{item}\033[0;0m')
          c+=1
#################################################################################### FUNÇÃO LISTA ORGANIZADA POKE 0
def pokeorg2():
    c = 0
    for item in pokemon:
          print(f'{c}-{item}')
          c+=1  
################################################################################### FUNÇÃO LETRA 
def letra():
    palavra = input("Digite a primeira letra: ")
    primeira_letra = [x for x in pokemon if x[0] == palavra.upper() or x[0] == palavra.lower()]#Pega palavra minuculas ou maiusculas e mostra aos itens da lista
    print(linha())
    print(primeira_letra)
    print(linha())
#----------------------------------------------------------------------LISTAS----------------------------------------------------------------------#
menu = (['Adicionar pokémon'],['Remover pokémon'],['Listar pokémons'],['Mostrar pokémons por letra inicial'],['Sair'])

pokemon= ['Aatrox','azir','Ashe','Bardo','Brand','Camille','corki','Darius','dr.mundo','Ekko','Ezreal','Fiora','Fizz','Galio','Garen','Hecarim','lllaoi','Jax','kartus','leona','Ziggs']
############################################################################################
while True:
 try:     
    print(linha2())
    cabeçalho('\033[1;32m          ░P░O░K░É░S░I░S░T░E░M░\033[0;0m')
    print(linha())
    cabeçalho('\033[1;32m            MENU\033[0;0m')
    menuorg()
    print(linha())
    escolha = int(input("Digite o número da sua escolha: ")) 
    if escolha == 1: #ADICIONAR
        dig = str(input('Digite o nome do pokemon: '))
        pokemon.append(dig)
        cabeçalho('LISTA ATUALIZADA')
        pokeorg()
        print(linha())      
        while True:
            try:
                escolha2 = int(input("Deseja adicionar outro pokémon? 1/2 :  "))
                if escolha2 ==1: #ADICIONAR 2X
                        dig = (input('Digite o nome do pokémon: '))
                        pokemon.append(dig)
                        cabeçalho('LISTA ATUALIZADA')
                        pokeorg()
                        print(linha())
                elif escolha2 ==2:
                        break
            except ValueError:
                print("\033[1;31mERRO!\nDigite\n[1] - Sim ou [2] - Não!\033[0;0m")
    elif escolha == 2: #REMOVE
        print(linha())
        pokeorg2()
        print(linha())
        apg = int(input("Digite o número do índice pokémon para remoção: "))
        pokemon.pop(apg)
        print(linha())
        cabeçalho('LISTA ATUALIZADA')
        print(linha())
        pokeorg2()
        print(linha())
        while True: #REMOVE2
         try:
            escolha3 = int(input("Deseja remover outro pokémon? 1/2 : "))
            if escolha3 == 1:
                apg = int(input("Digite o número do índice pokémon para remover: "))
                pokemon.pop(apg)
                print(linha())
                cabeçalho('LISTA ATUALIZADA')
                print(linha())
                pokeorg2()
                print(linha())
            elif escolha3 ==2:
                break
         except ValueError:
                print("\033[1;31mERRO!\nDIGITE UM NÚMERO VALIDO!!\033[0;0m")
#################################################################################### LISTA
    elif escolha == 3:
        print(linha())
        cabeçalho('LISTA ATUALIZADA')
        pokeorg()
        tempo3()    
        print(linha())
        print("Total de pokémons na lista:  ", len(pokemon)) #LISTA QUANT
        print(linha())
        tempo2()
##################################################################################
    elif escolha == 4:
            letra()
            while True:
             try:
                escolha4 = int(input('Deseja verificar novamente? 1/2 : '))
                if escolha4 == 1:
                    letra()
                elif escolha4 == 2:
                    break
             except ValueError:
                print("\033[1;31mERRO!\nDigite\n[1] - Sim ou [2] - Não!\033[0;0m")    
    elif escolha == 5:
        tempo2()
        print(linha2())
        tempo2()
        cabeçalho('\033[1;31m   ░E░N░C░E░R░R░A░N░D░O░ ░S░I░S░T░E░M░A░\033[0;0m')
        tempo2()
        cabeçalho('........')
        tempo2()
        cabeçalho('....')
        tempo2()
        cabeçalho('..')
        print(linha2())
        break
    if(escolha==0)or(escolha>5): #ERRO NUMERO 0 OU MAIOR QUE 5
        print(linha2())
        tempo2()
        print('\033[1;31mERRO! DIGITE UM NÚMERO VALIDO!!\033[0;0m')
        tempo2()
 except ValueError:#ERRO LETRA
                print(linha2())
                tempo2()
                cabeçalho('\033[1;31mERRO! DIGITE UM NÚMERO VALIDO!!\033[0;0m')
                tempo2()