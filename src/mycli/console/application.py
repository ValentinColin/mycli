from importlib import import_module

from typing import Callable

from mycli.console.commands.about import AboutCommand
from mycli.console.commands.source import SourceCommand
from mycli.console.commands.cleo import CleoCommand
from cleo.application import Application


def load_command(name: str) -> Callable:
    def _load() -> type[Command]:
        words = name.split(" ")
        module = import_module("mycli.console.commands." + ".".join(words))
        command_class = getattr(module, "".join(c.title() for c in words) + "Command")
        return command_class()

    return _load


application = Application()
application.add(AboutCommand())
application.add(SourceCommand())
application.add(CleoCommand())


def main() -> int:
    return application.run()


if __name__ == '__main__':
    main()
