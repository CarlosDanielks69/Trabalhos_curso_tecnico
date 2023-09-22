numeros = [12, 45, 78, 34, 90, 56, 78, 23, 45, 89]



print("A lista possui: ",len(numeros) , "Itens")
A = int(input("Informe um numero: "))



if 0 <= A < len(numeros):
    print("O índice desse número na lista é: ", numeros[A])


else:
    print("Item na lista não foi encontrado")
