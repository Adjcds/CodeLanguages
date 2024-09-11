# controle_fluxo.py
# Exemplos de controle de fluxo em Python

# Uso do 'pass' como um placeholder
for i in range(3):
    pass  # 'pass' é usado quando o código ainda não foi implementado

# Usando 'else' com 'for'
for i in range(5):
    print(i)
else:
    print("Loop concluído com sucesso!")  # Executa após o término do loop

# Usando 'else' com 'while'
contador = 0
while contador < 3:
    print("Contador:", contador)
    contador += 1
else:
    print("While concluído com sucesso!")  # Executa após o término do while
