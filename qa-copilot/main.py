def add(a, b):
    """
    Suma dos números.

    Args:
        a (int | float): Primer número a sumar.
        b (int | float): Segundo número a sumar.

    Returns:
        int | float: Resultado de la suma de a y b.

    Raises:
        TypeError: Si alguno de los argumentos no es numérico.
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError('Ambos argumentos deben ser numéricos')
    return a + b

