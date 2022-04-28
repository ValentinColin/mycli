from command_one import Command_One
from cleo import Application


application = Application()
application.add(Command_One())


def main() -> int:
    return application.run()


if __name__ == '__main__':
    main()
