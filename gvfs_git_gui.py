def match(command):
    return ('git-gui.exe' in command.stderr.lower()
            and 'GVFS repo' in command.stderr)


def get_new_command(command):
    return 'git-gui.exe'

requires_output = True