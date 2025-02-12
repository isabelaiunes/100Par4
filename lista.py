# Para criar uma lista de números de 1 a 100 #
numeros = list(range(1, 101))
# Para imprimir os números pares que são divisíveis por 4 #
for num in numeros:
    if num % 2 == 0 and num % 4 == 0:
        print(num)

# Pode-se fazer isso através de uma list comprehension também #

# Para criar uma lista com os números entre 1 e 100 #
numeros = list(range(1, 101))
# List comprehension para gerar uma lista somente com os números pares e divisíveis por 4 #
pares_div = [numero for numero in numeros if numero % 2 == 0 and numero % 4 == 0] 
# Imprima a lista gerada #
print(pares_div)

# Dessa forma, tudo é feito em uma linha de código #
# Pode mudar o código para criar a lista que desejar :) #