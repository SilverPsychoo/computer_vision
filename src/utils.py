def normalize_name(txt: str) -> str:
    """
    Esta función normaliza strings.
    - Quita espacios al inicio y al final
    - Elimina espacios extra entre palabras
    - Convierte el texto a formato Título

    Ejemplo:
    "   jOnaThAN   LeONel  " -> "Jonathan Leonel"
    """
    return " ".join(txt.strip().title().split())


def to_mxn(valor, tasa: float = 1.0) -> float:
    """
    Convierte un valor numérico a MXN multiplicándolo por la tasa.
    """
    return float(valor) * float(tasa)