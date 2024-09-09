# tipos_basicos.py
# Exemplos de tipos básicos em Python

# 1. Inteiros (int)
# O tipo 'int' é usado para representar números inteiros, ou seja, números sem parte decimal.
# Exemplo de uso de inteiros:

idade = 25  # Tipo inteiro
ano_nascimento = 1998
ano_atual = 2024
idade_ano_que_vem = ano_atual - ano_nascimento

print("1. Exemplo de inteiros:")
print("Idade:", idade)
print("Idade no próximo ano:", idade_ano_que_vem)
print()  # Linha em branco para separação

# 2. Números de Ponto Flutuante (float)
# O tipo 'float' é usado para representar números com parte decimal.
# Exemplo de uso de números de ponto flutuante:

preco = 19.99  # Tipo float
desconto = 0.15

preco_com_desconto = preco * (1 - desconto)

print("2. Exemplo de números de ponto flutuante:")
print("Preço original:", preco)
print("Preço com desconto:", preco_com_desconto)
print()  # Linha em branco para separação

# 3. Strings (str)
# O tipo 'str' é usado para representar cadeias de caracteres (texto).
# Exemplo de uso de strings:

nome = "Maria"  # Tipo string
saudacao = "Olá, " + nome + "!"  # Concatenação de strings

print("3. Exemplo de strings:")
print(saudacao)
print()  # Linha em branco para separação

# 4. Booleanos (bool)
# O tipo 'bool' é usado para representar valores booleanos: True (Verdadeiro) ou False (Falso).
# Exemplo de uso de valores booleanos:

idade = 18
maior_de_idade = idade >= 18  # Verifica se a idade é maior ou igual a 18

print("4. Exemplo de booleanos:")
if maior_de_idade:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
