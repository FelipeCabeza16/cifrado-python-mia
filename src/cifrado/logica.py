"""Lógica de negocio del cifrado. No depende de la interfaz gráfica."""

LONGITUD = 6
DESPLAZAMIENTO = 7
# Pares de posiciones (base 0) que se intercambian: 1º-3º, 2º-4º y 5º-6º.
INTERCAMBIOS = ((0, 2), (1, 3), (4, 5))


def validar_numero(texto):
    """Devuelve el texto limpio o lanza ValueError si no son exactamente 6 dígitos."""
    texto = texto.strip()
    if not (texto.isascii() and texto.isdigit() and len(texto) == LONGITUD):
        raise ValueError(f"Ingrese un número entero de exactamente {LONGITUD} dígitos.")
    return texto


def intercambiar_posiciones(digitos):
    """Aplica los intercambios de posiciones; es su propia inversa."""
    resultado = list(digitos)
    for a, b in INTERCAMBIOS:
        resultado[a], resultado[b] = resultado[b], resultado[a]
    return resultado


def cifrar(texto):
    """Suma 7 a cada dígito (módulo 10) y luego intercambia posiciones."""
    digitos = [(int(d) + DESPLAZAMIENTO) % 10 for d in validar_numero(texto)]
    return "".join(str(d) for d in intercambiar_posiciones(digitos))


def descifrar(texto):
    """Revierte `cifrar`: primero deshace los intercambios y luego resta 7 (módulo 10)."""
    digitos = [int(d) for d in intercambiar_posiciones(validar_numero(texto))]
    return "".join(str((d - DESPLAZAMIENTO) % 10) for d in digitos)
