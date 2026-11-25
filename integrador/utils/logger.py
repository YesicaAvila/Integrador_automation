import logging
from pathlib import Path

def get_logger(name: str = "integrador") -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    log_dir = Path(__file__).resolve().parent.parent / "reports"
    log_dir.mkdir(parent=True, exist_ok=True)
    log_file = log_dir / "ejecucion.log"

    formato = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
    file_handler.setFormatter(formato)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formato)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger