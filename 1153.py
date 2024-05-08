N = int(input())
valorFinal = N

for x in range(N-1, 0, -1):
    valorFinal *= x

print(valorFinal)
