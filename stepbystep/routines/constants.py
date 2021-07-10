from pathlib import Path

ROUTINES_DIR_NAME = ".stepbystep"

CURRENT_DIR = Path(__file__).resolve(strict=True).parent
TEMPLATES_DIR = CURRENT_DIR / "templates"
INITIAL_TEMPLATE_PATH = TEMPLATES_DIR / "initial.txt"
