default_app_config = 'kitsune.sumo.apps.SumoConfig'


class ProgrammingError(Exception):
    """Somebody made a mistake in the code."""


# MONKEYPATCH! WOO HOO! LULZ
from kitsune.sumo.monkeypatch import patch  # noqa
patch()
