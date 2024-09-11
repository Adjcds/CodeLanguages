# lacos_repeticao.py
# Exemplos de laços de repetição em Python

# Usando o laço 'for' para percorrer uma lista
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)  # Exibe cada número da lista

# Usando o laço 'for' com range
for i in range(1, 6):
    print(i)  # Exibe números de 1 a 5

# Usando o laço 'while'
contador = 0
while contador < 5:
    print("Contagem:", contador)  # Exibe o valor do contador
    contador += 1  # Incrementa o contador em 1

# Usando 'break' para sair de um laço
for i in range(10):
    if i == 3:
        break  # Sai do laço quando i é 3
    print(i)

# Usando 'continue' para pular uma iteração
for i in range(5):
    if i == 2:
        continue  # Pula o restante do código e vai para a próxima iteração
    print(i)
