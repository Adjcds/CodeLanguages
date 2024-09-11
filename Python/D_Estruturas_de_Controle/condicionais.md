# Estruturas Condicionais

As estruturas condicionais permitem que seu programa tome decisões com base em condições específicas. 

## Tipos de Estruturas Condicionais

- **`if` (se):** Executa um bloco de código se a condição for verdadeira.
  - **Exemplo:**
    ```python
    idade = 18
    if idade >= 18:
        print("Você é maior de idade.")
    ```

- **`elif` (senão, se):** Verifica condições adicionais se a condição `if` for falsa.
  - **Exemplo:**
    ```python
    idade = 16
    if idade >= 18:
        print("Você é maior de idade.")
    elif idade >= 13:
        print("Você é um adolescente.")
    ```

- **`else` (senão):** Executa um bloco de código se todas as condições anteriores forem falsas.
  - **Exemplo:**
    ```python
    idade = 10
    if idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")
    ```

### Exemplos no Código

Consulte o arquivo `condicionais.py` para ver exemplos práticos de como usar estruturas condicionais em Python.