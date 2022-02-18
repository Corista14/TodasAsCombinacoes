import random
import string
import math


min_mai = string.ascii_letters # Todas as letras maisculas e minisculas
dig = string.digits # Todos os digitos de 0-9
todas = "".join([min_mai, dig]) # Juntar todos os caracteres

print('Quantos caracteres?')
caract = int(input(""))

# Criar uma lista vazia para adicionar todas as combinações possíveis
todas_comb = []


# Criar uma variavel com o número de combinações possíveis
comb_possiveis = math.comb(len(todas), caract)
print(f"Existem {comb_possiveis} com {caract} caractéres.")


# For loop para obter TODAS as combinações possíveis
for i in range(0, comb_possiveis + 1):
    combinacao = str("".join(random.sample(list(todas), caract)))
    todas_comb.append(combinacao)


with open(f"combinacoescom{caract}.txt", 'w') as f:
    f.write(str(todas_comb))


print(todas_comb)
input("")