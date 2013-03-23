__author__ = 'rob'


# Space Game is a hacker-ish space adventure game by Rob Fisher.

import cmd
import gridsquare


class SpaceGameCommandInterpreter(cmd.Cmd):
    """Main game command interpreter."""

    def do_info(self, line):
        if line:
            print 'No information about ' + line
        else:
            print "This is Space Game. Try the gs command."

    def do_gs(self, line):
        try:
            args = line.split(',')
            x = int(args[0])
            y = int(args[1])
        except (ValueError, AttributeError):
            print 'Try typing: gs ' + str(gridsquare.civilisation_centre_x) + ', ' + str(
                gridsquare.civilisation_centre_y)
            return

        gs = gridsquare.GridSquare(x, y)
        gs.info()

    def do_EOF(self, line):
        print 'Bye.'
        return True


if __name__ == '__main__':
    commandInterpreter = SpaceGameCommandInterpreter()
    commandInterpreter.prompt = 'sg> '
    commandInterpreter.cmdloop('Welcome to Space Game.')
