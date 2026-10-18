import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "plugins" / "seo-pro" / "skills" / "seo-pro" / "scripts"
FIXTURES = Path(__file__).resolve().parent / "fixtures"
for p in (SCRIPTS, ROOT / "tools", Path(__file__).resolve().parent):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))
