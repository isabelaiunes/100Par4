# Criar uma lista de números de 1 a 100
numeros = list(range(1, 101))
# Imprimir os números pares que são divisíveis por 4 #
for num in numeros:
    if num % 2 == 0 and num % 4 == 0:
        print(num)
        