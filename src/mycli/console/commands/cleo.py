import mycli
import cleo
from mycli.console.commands.command import Command


class CleoCommand(Command):

    name = "cleo"

    description = "Show some information usefull for used CLEO"

    def handle(self) -> None:
        self.line(
            f"""\
Balide <INFO>: <info>This is an -info- format</info>
Balide <COMMENT>: <comment>This is an -comment- format</comment>
Balide <QUESTION>: <question>This is an -question- format</question>
Balide <ERROR>: <error>This is an -error- format</error>"""
        )
