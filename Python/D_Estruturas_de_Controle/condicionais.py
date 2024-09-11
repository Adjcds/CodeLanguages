# condicionais.py
# Exemplos de estruturas condicionais em Python

idade = 18

# Condicional simples com if
if idade >= 18:
    print("Você é maior de idade.")  # Executa se a condição for verdadeira

# Condicional com if-else
if idade < 18:
    print("Você é menor de idade.")  # Executa se a condição for verdadeira
else:
    print("Você é maior de idade.")  # Executa se a condição for falsa

# Condicional com if-elif-else
nota = 7

if nota >= 9:
    print("Aprovado com distinção!")  # Se nota for 9 ou mais
elif nota >= 6:
    print("Aprovado.")  # Se nota for entre 6 e 8
else:
    print("Reprovado.")  # Se nota for menor que 6
