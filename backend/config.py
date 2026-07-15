"""
Armazenar as configurações do sistema.
"""
from pathlib import Path

# ==========================
# Comunicação Serial
# ==========================

SERIAL_PORT = "COM5"      
SERIAL_BAUDRATE = 9600

# ==========================
# Banco de Dados
# ==========================

BASE_DIR = Path(__file__).resolve().parent
DATABASE_URL = f"sqlite:///{BASE_DIR / 'rfid_access.db'}"

# ==========================
# Aplicação
# ==========================

API_TITLE = "RFID Access Control"

DEBUG = True