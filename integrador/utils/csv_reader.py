import csv
from pathlib import Path

def leer_datos_login(nombre_archivo="login_data.csv"):
    ruta_csv = Path(__file__).resolve().parent.parent / "data" / nombre_archivo
    casos = []

    with open(ruta_csv, mode="r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            espera_exito = fila["expected_success"].strip().lower() == "true"
            casos.append((
                fila["username"].strip(),
                fila["password"].strip(),
                espera_exito,
                fila["expected_message"].strip(),
            ))

    return casos