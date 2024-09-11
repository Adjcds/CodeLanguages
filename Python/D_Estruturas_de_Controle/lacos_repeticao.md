# Laços de Repetição

Os laços de repetição permitem executar um bloco de código várias vezes.

## Tipos de Laços de Repetição

- **`for` (para):** Itera sobre uma sequência (como uma lista, tupla, ou string).
  - **Exemplo:**
    ```python
    for i in range(5):
        print(i)
    ```

- **`while` (enquanto):** Executa um bloco de código enquanto a condição for verdadeira.
  - **Exemplo:**
    ```python
    contador = 0
    while contador < 5:
        print(contador)
        contador += 1
    ```

- **`break` (interromper):** Interrompe o laço atual.
  - **Exemplo:**
    ```python
    for i in range(10):
        if i == 5:
            break
        print(i)
    ```

- **`continue` (continuar):** Pula a iteração atual e continua com a próxima.
  - **Exemplo:**
    ```python
    for i in range(10):
        if i % 2 == 0:
            continue
        print(i)
    ```

### Exemplos no Código

Consulte o arquivo `lacos_repeticao.py` para ver exemplos práticos de como usar laços de repetição em Python.
