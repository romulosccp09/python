# Cáuculo IMC!!!
# Desenvolvido por Rômulo de Carvalho, para teste com git github.
# Programa caucula o ídice de massa corpórea do usuário.
# Declarando variáveis
pessoa = input("Digite seu nome: ") # Nome do usuário.
idade = int(input("Digite sua idade: ")) # Idade do usuário.
peso = float(input("Digite seu peso: ")) # Peso do usuáriose.
altura = float(input("Digite sua altura: ")) # Altura do usuário.
# Cauculando imc do usuário.
imc = peso/(altura*altura)
# Mostra os resultados para o usuário!!!
print("{}, você tem {} anos, seu imc é de {:.2f}" .format(pessoa,idade,imc))

# Codições dos resultados!
if imc <= 17:
    print(' Cuidado, Seu IMC está abaixo do ideal!')

elif imc >17 and imc <=25:
    print('Parabéns, seu IMC está no parâmetro ideal! ')

else:
    print('Cuidado, seu IMC está acima do ideal!')
