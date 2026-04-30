from math import isqrt

def eh_primo(numero: int) -> bool:
    """
    Verifica se um número é primo.

    Args:
        numero (int): Número a ser verificado

    Returns:
        bool: True se for primo, False caso contrário
    """
    if numero <= 1:
        return False

    if numero in (2, 3):
        return True

    if numero % 2 == 0:
        return False

    for divisor in range(3, isqrt(numero) + 1, 2):
        if numero % divisor == 0:
            return False

    return True