import mycli
import cleo
from mycli.console.commands.command import Command


class AboutCommand(Command):

    name = "About"

    description = "Shows information about the package mycli"

    def handle(self) -> None:
        self.line(
            f"""\
<info>Mycli - CLI exemple for application in Python

Version: {mycli.__version__}
Cleo Version: {cleo.__version__}</info>

<comment>Mycli is an exemple of a Command Line Interface (CLI) for a new application which use Python
See <fg=blue>https://github.com/ValentinColin/mycli</> for more information.</comment>"""
        )
