from importlib import import_module

from typing import Callable

from .commands.about import AboutCommand
from cleo import Application


def load_command(name: str) -> Callable:
    def _load() -> type[Command]:
        words = name.split(" ")
        module = import_module("mycli.console.commands." + ".".join(words))
        command_class = getattr(module, "".join(c.title() for c in words) + "Command")
        return command_class()

    return _load


application = Application()
application.add(AboutCommand())


def main() -> int:
    return application.run()


if __name__ == '__main__':
    main()
