print("Selecione o número da operação desejada:")


print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

escolher = int(input("Digite sua opção (1/2/3/4): "))

numb1 = int(input("Digite o primeiro número: "))
numb2 = int(input("Digite o segundo número: "))
total = 0 


if escolher == 1:
 total = numb1 + numb2
 print(total)
elif escolher == 2:
     total = numb1 - numb2
     print(total)
elif escolher == 3:
     total = numb1 * numb2
     print(total)
elif escolher == 4:
     total = numb1 / numb2
     print(total)  
else:
    print('Invalido')

    