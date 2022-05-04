This is an exemple for create a CLI with CLEO

I add a dependency cleo like this:

```sh
poetry add cleo
```

don't forget to change mycli by the name of your application


## Structure des commandes

```
commands/
    command_1.py
    command_2.py
    command_3.py
    command_3/
        __init__.py
        command_3_1.py
        command_3_2.py
        command_3_3.py
    ...
```
