from typing import Any

from cleo.commands.command import Command as BaseCommand
from cleo.exceptions import ValueException


class Command(BaseCommand):

    def option(self, name: str, default: Any = None) -> Any:
        try:
            return super().option(name)
        except ValueException:
            return default
