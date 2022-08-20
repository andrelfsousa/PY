while True:
    try:   
        Escolha=(int(input("(1) para calcular \n(2) para sair \nDigite:  ")))
        if (Escolha == 1):
            Calcular=(float(input("Digite o valor do salario: ")))
            if Calcular < 1903.98:
                print("Salário isento de imposto!")
            elif Calcular > 1903.98 and Calcular <= 2826.65:
                S2 = Calcular*0.075
                SL = Calcular-S2
                print('\n--------------------------\nSALÁRIO LIQUIDO=',SL)
                print("Aliquita de (7,5%)\n--------------------------\n")
            elif Calcular > 2826.65 and Calcular <= 3751.06:
                S2 = Calcular*0.15
                SL = Calcular-S2
                print('\n--------------------------\nSALÁRIO LIQUIDO=',SL)
                print("Aliquita de (15%)\n--------------------------\n")
            elif Calcular > 3751.06 and Calcular <= 4664.68:
                S2 = Calcular*0.225 
                SL = Calcular-S2
                print('\n--------------------------\nSALÁRIO LIQUIDO=',SL)
                print("Aliquita de (22,5%)\n--------------------------\n")
            elif Calcular > 4664.68:
                S2 = Calcular * 0.275 
                SL = Calcular-S2
                print('\n--------------------------\nSALÁRIO LIQUIDO=',SL)
                print("Aliquita de (27,5%)\n--------------------------\n")

        elif (Escolha ==2):
            print("Saindo do aplicativo")
            print("..........")
            print(".....")
            break
        #erros
        elif (Escolha != 1 or Escolha!= 2):
            print('Erro digite (1) ou (2)!')
    except:
        print('Erro! \nNão digite letras ou simbolos.\n Digite (1) ou (2)!!')