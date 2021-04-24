# config/settings/__init__.py

try:
    from .production import *
except Exception:
    from .local import *
