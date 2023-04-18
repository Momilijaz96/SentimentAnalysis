# Inside config.py, we'll add the code to define key directory locations

from pathlib import Path

# Directories
BASE_DIR = Path(__file__).resolve().parent.parent.absolute()
CONFIG_DIR = Path(BASE_DIR / "config")
