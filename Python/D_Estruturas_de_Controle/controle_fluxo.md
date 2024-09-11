# Controle de Fluxo

O controle de fluxo gerencia a ordem em que o código é executado.

## Tipos de Controle de Fluxo

- **`break` (interromper):** Sai imediatamente do laço mais interno.
  - **Exemplo:**
    ```python
    while True:
        resposta = input("Digite 'sair' para sair: ")
        if resposta == "sair":
            break
    ```

- **`continue` (continuar):** Pula o restante do código na iteração atual do laço e vai para a próxima iteração.
  - **Exemplo:**
    ```python
    for numero in range(10):
        if numero % 2 == 0:
            continue
        print(numero)
    ```

- **`pass` (não faz nada):** Usado como um espaço reservado para estruturas de controle que ainda não foram implementadas.
  - **Exemplo:**
    ```python
    for numero in range(5):
        if numero == 3:
            pass
        print(numero)
    ```

### Exemplos no Código

Consulte o arquivo `controle_fluxo.py` para ver exemplos práticos de como usar o controle de fluxo em Python.
