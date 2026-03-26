def fun_4(n: int) -> int:
    """
    Calcula o valor da função recursiva F(n).

    A função é definida por:
        F(n) = 2 * F(n - 1) + n^2
    com caso base:
        F(1) = 2

    Args:
        n (int): Valor inteiro maior ou igual a 1.

    Returns:
        int: Resultado de F(n).
    """
    if n == 1:
        return 2
    return 2 * fun_4(n - 1) + n ** 2

def fun_fechada(n: int) -> int:
    """
    Calcula o valor de F(n) usando a fórmula fechada.

    A função é definida por:
        F(n) = 13 * 2^(n - 1) - n^2 - 4n - 6

    Args:
        n (int): Inteiro maior ou igual a 1.

    Returns:
        int: Valor de F(n).

    Raises:
        ValueError: Se n for menor que 1.
    """
    if n < 1:
        raise ValueError("n deve ser >= 1")

    return 13 * (2 ** (n - 1)) - n ** 2 - 4 * n - 6

def main() -> None:
    """
    Função principal para entrada de dados e execução do programa.

    Solicita ao usuário um valor de n e exibe o resultado de F(n).
    """
    try:
        n = int(input("Digite um valor de n (>= 1): "))

        if n < 1:
            print("Erro: n deve ser >= 1")
            return

        resultado = fun_4(n)
        resultado_fechada = fun_fechada(n)
        print(f"Fun_4({n}) = {resultado}")
        print(f"Fun_fechada({n}) = {resultado_fechada}")

    except ValueError:
        print("Erro: digite um número inteiro válido")


if __name__ == "__main__":
    main()