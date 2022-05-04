import mycli
import cleo
from mycli.console.commands.command import Command


class SourceCommand(Command):

    name = "source"

    description = "Show the different source based or inspiring"

    def handle(self) -> None:
        self.line(
            f"""\
<info>Package</info>
<comment>CLEO: <fg=blue>https://github.com/sdispater/cleo/</></comment>"""
        )
