from dragonfly import MappingRule, Key, Grammar, Text
from castervoice import Plugin

class UnixShellRule(MappingRule):

    def __init__(self, config):

        mapping = {
            "shell cancel":
                Key('c-c'),
            "shell terminate":
                Key('c-d'),
            "shell suspend":
                Key('c-z'),
            "shell foreground":
                Text('fg\n'),
            "shell background":
                Text('bg\n'),
        }

        MappingRule.__init__(self, mapping=mapping)




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

