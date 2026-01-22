from utils import normalize_name, to_mxn

raw = [
    {"nombre": "ana", "activo": True,  "monto": "100"},
    {"nombre": "LUIS", "activo": False, "monto": "0"},
    {"nombre": "marIa", "activo": True,  "monto": "99.9"},
]

def clean(reg):
    return {
        "nombre": normalize_name(reg["nombre"]),
        "activo": bool(reg["activo"]),
        "monto_mxn": to_mxn(reg["monto"], tasa=1.0),
    }
    
for r in raw:
    print(clean(r))
