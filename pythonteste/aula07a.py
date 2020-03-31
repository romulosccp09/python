# Autor: Rômulo de Cravalho.
# Email: romulo514@hotmail.com
# Exemplo Aula07, operadores aritiméticos!

numero = int(input("Digite um valor: "))
numero1 = int(input('Digite outro valor: '))

# Soma.
print('A soma de {} e {}, vale -> {}! \n'.format(numero, numero1, numero + numero1))

#Subtação.
print('A subtração entre {} e {}, vale -> {}! \n'.format(numero, numero1, numero - numero1))

#Multiplicação.
print('A multiplicação entre {} e {}, vale -> {}! \n'.format(numero, numero1, numero * numero1))

# Divisão.
print('A divisão ente {} e {}. vale -> {:.3f}! \n'.format(numero, numero1, numero / numero1))

#Divisão inteira.
print('A divisão inteira entre {} e {}, vale -> {}! 8\n'.format(numero, numero1, numero // numero1))

# Módulo (Resto da divisão).
print('O Módulo entre {} e {}, vale {}!'.format(numero, numero1, numero % numero1))
