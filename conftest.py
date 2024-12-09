import sys
import os
from pathlib import Path

# Añadir el directorio `src` al path de Python
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'src'))