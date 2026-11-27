import logging
from pathlib import Path

def get_logger(name: str = "integrador") -> logging.Logger:
    """Crea y devuelve un logger configurado para escribir en consola y en ejecucion.log."""
    logger = logging.getLogger(name)
    # Evita agregar salidas duplicadas si este logger ya fue configurado antes
    if logger.handlers:
        return logger

    # Registra mensajes desde nivel INFO en adelante (INFO, WARNING, ERROR, CRITICAL)
    logger.setLevel(logging.INFO)

    #Prepara la carpeta reports y la ruta del archivo de registro
    log_dir = Path(__file__).resolve().parent.parent / "reports"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "ejecucion.log"

    # Define cómo se verá cada línea del registro (fecha/hora, nivel, origen y mensaje)
    formato = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Guarda los registros en ejecucion.log (mode="w" reinicia el archivo en cada corrida)
    file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
    file_handler.setFormatter(formato)

    # Muestra los mismos registros en la terminal durante la ejecución
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formato)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger