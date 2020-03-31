# Programa ler dados digitado, e dá informações sobre ele.

dado = input('Digite algo: ')
# Verifica se há possibilidade de o caractere ser tipo primitivo.
print("Tipo primitivo do dado: ", type(dado))
# Verifica se há possibilidade de o caractere ser somente espaços.
print("Somente espaços: ", dado.isspace())
# Verifica se há possibilidade de o caractere ser um número.  
print("É númérico: ", dado.isnumeric())
# Verifica se há possibilidade de o caractere ser alfabético.
print("É alfabético: ", dado.isalpha())
# Verifica se há possibilidade de o caractere ser alfanumérico.
print("É alfanumérico: ", dado.isalnum())
# Verifica se há possibilidade de o caractere ser tipo primitivo.
print('Somente maiúsculas: ', dado.isupper())
# Verifica se há possibilidade de o caractere ser tipo primitivo.
print('Somente minusculas: ', dado.islower())
# Verifica se há possibilidade de o caractere ser capitalizada.
print(" Está capitalizada: ", dado.istitle())
