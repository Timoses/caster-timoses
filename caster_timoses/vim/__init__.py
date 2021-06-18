from castervoice import Plugin

from caster_timoses.vim.original.gvim import normalModeGrammar, insertModeBootstrap, commandModeBootstrap, insertModeGrammar, commandModeGrammar

class Vim(Plugin):

    def __init__(self, manager):
        super().__init__(manager)

    def get_grammars(self):
        return [normalModeGrammar, insertModeBootstrap, commandModeBootstrap]

    def _apply_context(self, context=None):
        insertModeGrammar.set_context(context)
        commandModeGrammar.set_context(context)

    def load(self):
        Plugin.load(self)
        insertModeGrammar.load()
        commandModeGrammar.load()

    def enable(self):
        super().enable()
        insertModeGrammar.enable()
        commandModeGrammar.enable()

    def disable(self):
        super().disable()
        insertModeGrammar.disable()
        commandModeGrammar.disable()
