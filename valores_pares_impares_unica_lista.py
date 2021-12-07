#Crie um programa onde o usuário possa digitar sete valores numéricos
#e cadastre-os em uma lista única que mantenha separados os valores pares
#e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

#---Declaração de Lista---#
valores = [[],[]]          #
#-------------------------#

#----- Código de Execução ----------------------#
for n in range (1,8):                           #
    num = int (input(f'Digite o {n}º número: '))#
    if num % 2 == 0:                            #
        valores[0].append(num)                  #
    elif num % 2 == 1:                          #
        valores[1].append(num)                  #
valores[0].sort()                               #
valores[1].sort()                               #
print (f'Pares: {valores[0]}')                  #
print (f'Ímpares: {valores[1]}')                #
#-----------------------------------------------#
