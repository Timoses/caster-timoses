from dragonfly import MappingRule, Key, Grammar, Text, IntegerRef
from castervoice import Plugin

class UnixShellRule(MappingRule):

    def __init__(self, config):

        mapping = {
            "shell (terminate|cancel)":
                Key('c-c'),
            "shell log out":
                Key('c-d'),
            "shell suspend":
                Key('c-z'),
            "shell foreground":
                Text('fg\n'),
            "shell background":
                Text('bg\n'),
            "shell up [<n>]":
                Key('a-k:%(n)d'),
            "shell down [<n>]":
                Key('a-j:%(n)d'),
            "shell history":
                Text('history\n'),
            "shell history <n> [<n2>] [<n3>] [<n4>]":
                Text('#!%(n)d BROKEN')
        }
        extras = [
            IntegerRef("n", 1, 10),
            IntegerRef("n2", 10, 11),
            IntegerRef("n3", 10, 11),
            IntegerRef("n4", 10, 11),
        ]

        defaults = {
            "n": 1
        }

        MappingRule.__init__(self, mapping=mapping, extras=extras, defaults=defaults)




class UnixLsPlugin(Plugin):

    """Docstring for DictationPlugin. """

    def __init__(self, manager):
        """TODO: to be defined. """

        super().__init__(manager)

    def get_grammars(self):
        grammar = Grammar(name="UnixShell")
        print(self.config)
        grammar.add_rule(UnixShellRule(self.config))
        return [grammar]

