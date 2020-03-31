# Autor: Rômulo de Cravalho.
# Email: romulo514@hotmail.com
# Exemplo Aula07 Alguns exemplos de formtar Strings.

nome = input('Qual seu nome? ')
print('Prazer em ti conhecer, {}!'.format(nome))

# Imprimindo com 20 caracteres!
print('prazer em ti conhecer. {:20}!'.format(nome))

# Alinhamento à deireita!
print('Prazer em ti conhecer {:>20}!'.format(nome))

#Alinhamento pra esquerda!
print('Prazer em ti conhecer {:<20}!'.format(nome))

#Usar circunflexo para centralizar.
print('Prazer em ti conhecer, {:^20}'.format(nome))

#Centralizado com caracter!
print('Prazer em ti conhecer, {:=^20}!'.format(nome))