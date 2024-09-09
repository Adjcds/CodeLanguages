# tipos_compostos.py
# Exemplos de tipos compostos em Python

# 1. Listas (list)
# Listas são coleções ordenadas de itens que podem ser de diferentes tipos. Elas são mutáveis, ou seja, você pode alterar seus itens.
# Exemplo de uso de listas:

frutas = ["maçã", "banana", "laranja"]  # Tipo lista
frutas.append("uva")  # Adiciona um item à lista

print("1. Exemplo de listas:")
print("Lista de frutas:", frutas)
print("Número de frutas:", len(frutas))  # Exibe a quantidade de itens na lista
print()  # Linha em branco para separação

# 2. Tuplas (tuple)
# Tuplas são coleções ordenadas de itens que podem ser de diferentes tipos, mas são imutáveis, ou seja, não podem ser alteradas após a criação.
# Exemplo de uso de tuplas:

coordenadas = (10, 20)  # Tipo tupla

print("2. Exemplo de tuplas:")
print("Coordenadas:", coordenadas)
print()  # Linha em branco para separação

# 3. Conjuntos (set)
# Conjuntos são coleções não ordenadas de itens únicos, ou seja, não permitem duplicatas. Eles são úteis para operações matemáticas como união e interseção.
# Exemplo de uso de conjuntos:

numeros = {1, 2, 3, 4}  # Tipo conjunto
numeros.add(5)  # Adiciona um item ao conjunto

print("3. Exemplo de conjuntos:")
print("Conjunto de números:", numeros)
print()  # Linha em branco para separação

# 4. Dicionários (dict)
# Dicionários são coleções de pares chave-valor. Cada chave é única e está associada a um valor. Eles são mutáveis e permitem armazenar dados estruturados.
# Exemplo de uso de dicionários:

pessoa = {"nome": "João", "idade": 30}  # Tipo dicionário
pessoa["cidade"] = "São Paulo"  # Adiciona um novo item ao dicionário

print("4. Exemplo de dicionários:")
print("Dados da pessoa:", pessoa)
