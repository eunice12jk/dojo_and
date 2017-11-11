"""
Dojo App. pick a command below
Usage:
    create_room <room_type> <room_name> ...
    add_person <first_name> <last_name> <designation> [-w]
    q (quit)
    Options:
    -h --help Show this screen.
    -i --interactive Interactive mode.
    -v --version
"""
import cmd
import sys
from docopt import docopt, DocoptExit
from Dojo.dojo import Dojo

def app_exec(func):
    """
    Decorator definition for the app.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)
        except DocoptExit as e:
            msg = "Invalid command! See help."
            print(msg)
            print(e)
            return

        except SystemExit:
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)

    return fn


class DojoCli(cmd.Cmd):
    print(__doc__)
    prompt = "dojo$ "
    dojo = Dojo()

    @app_exec
    def do_create_room(self, arg):
        """Adds new room to Dojo
        Usage: create_room <room_type> <room_name> ...
        """
        self.dojo.create_room(arg)

    @app_exec
    def do_add_person(self, arg):
        """This command handles creation of person and allocated
        random room to new person
        Usage:
            add_person <first_name> <last_name> <designation> [-w]
        """
        self.dojo.add_person(arg)

if __name__ == '__main__':
    DojoCli().cmdloop()