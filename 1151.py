N = int(input())
num1 = 0
num2 = 1
proxNumero = num2
cont = 1

print(num1, num2, end = " ")

while cont <= N-2:
    if cont == N-2:
        print(proxNumero)
    else:
        print(proxNumero, end=" ")
    num1, num2 = num2, proxNumero
    proxNumero = num1 + num2
    cont += 1
     
