from dragonfly import MappingRule, Text, Grammar
from castervoice import Plugin

class AnsibleCommandRule(MappingRule):

    def __init__(self, config):

        general = Text('')
        if 'inventory' in config:
            general = general + Text(' -i ' + config.get('inventory'))
        if 'ask_vault_pass' in config and config.get('ask_vault_pass') == True:
            general = general + Text(' --ask-vault-pass')
        if 'verbosity' in config:
            general = general + Text(' -' + 'v'*config.get('verbosity'))
        if 'playbook_directory' in config:
            general = general + Text(' ' + config.get('playbook_directory'))


        mapping = {
            "ansible playbook":
                Text("ansible-playbook") + general,
        }

        MappingRule.__init__(self, mapping=mapping)




class AnsibleCommandPlugin(Plugin):

    """Docstring for DictationPlugin. """

    def __init__(self, manager):
        """TODO: to be defined. """

        super().__init__(manager)

    def get_grammars(self):
        grammar = Grammar(name="AnsibleCommand")
        print(self.config)
        grammar.add_rule(AnsibleCommandRule(self.config))
        return [grammar]
