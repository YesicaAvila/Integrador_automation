import csv
from pathlib import Path

def leer_datos_login(nombre_archivo="login_data.csv"):
    """Lee un archivo CSV de datos de login y devuelve una lista de casos para parametrizar."""
    # Construye la ruta hacia la carpeta data sin depender de dónde se ejecute pytest
    ruta_csv = Path(__file__).resolve().parent.parent / "data" / nombre_archivo
    casos = []

    with open(ruta_csv, mode="r", encoding="utf-8", newline="") as archivo:
        # Usa los encabezados de columna como claves de cada fila
        lector = csv.DictReader(archivo)
        for fila in lector:
            # Convierte el texto "true"/"false" en un valor booleano limpio
            espera_exito = fila["expected_success"].strip().lower() == "true"
            casos.append((
                fila["username"].strip(),
                fila["password"].strip(),
                espera_exito,
                fila["expected_message"].strip(),
            ))

    return casos