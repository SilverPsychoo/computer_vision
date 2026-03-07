from pathlib import Path
BASE = Path(__file__).resolve().parent.parent
print(BASE) # Carpeta de mi proyecto

raw = BASE / "data" / "raw"
clean = BASE / "data" / "clean"

# Creación de las carpetas
raw.mkdir(parents=True, exist_ok=True)
clean.mkdir(parents=True, exist_ok=True)

# Escribir a un archivo txt
txt_path = raw / "notas.txt"
txt_path.write_text("Hola como estas\n \tEstoy bien gracias", encoding="utf-8")

contenido = txt_path.read_text(encoding="utf-8")
print(contenido)