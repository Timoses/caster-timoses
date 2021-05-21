import platform

from dragonfly import Repeat, Pause, Function, Choice, MappingRule, Dictation, IntegerRef, Key, Text, Grammar

from castervoice import Plugin

system = platform.system()
if system == "Darwin":
    CTRL = "w"
    JUMP_WALL = {"left": "w-left",
                 "right": "w-right",
                 "up": "w-up",
                 "down": "w-down"}
    JUMP_WORD = {"left": "a-left",
                 "right": "a-right"}
    WORD_DELETE_MODIFIER = "a"
    DELETE_DIR = {"left": "backspace",
                  "right": "delete"}
else:
    CTRL = "c"
    JUMP_WALL = {"left": "home",
                 "right": "end",
                 "up": "c-home",
                 "down": "c-end"}
    JUMP_WORD = {"left": "c-left",
                 "right": "c-right"}
    WORD_DELETE_MODIFIER = "c"
    DELETE_DIR = {"left": "backspace",
                  "right": "delete"}


class FirefoxRule(MappingRule):
    mapping = {
        "(new window|window new)":
            Key("{}-n".format(CTRL)),
        "new private window|private window new":
            Key("ws-p"),
        "window close|close all tabs":
            Key("{}s-w".format(CTRL)),
        "new tab [<n>]|tab new [<n>]":
            Key("{}-t".format(CTRL)) * Repeat(extra="n"),
        "reopen tab [<n>]|tab reopen [<n>]":
            Key("{}s-t".format(CTRL)) * Repeat(extra="n"),
        "(back|previous) tab [<n>]|tab (left|lease) [<n>]":
            Key("cs-tab") * Repeat(extra="n"),
        "(next|forward) tab [<n>]|tab (right|sauce) [<n>]":
            Key("c-tab") * Repeat(extra="n"),
        "close tab [<n>]|tab close [<n>]":
            Key("{}-w".format(CTRL)) * Repeat(extra='n'),
        "go (back|prev|prior|previous) [<n>]":
            Key("{}-left/20".format(CTRL)) * Repeat(extra="n"),
        "go (next|forward) [<n>]":
            Key("{}-right/20".format(CTRL)) * Repeat(extra="n"),
        "find (next|forward) [match] [<n>]":
            Key("{}-g/20".format(CTRL)) * Repeat(extra="n"),

        "find <search>":
            Key("{}-f/20".format(CTRL)) + Text("%(search)s"),
        "search <search>":
            Key("{}-l/20".format(CTRL)) + Text("%(search)s")
    }
    extras = [
        Choice("nth", {
                "first": "1",
                "second": "2",
                "third": "3",
                "fourth": "4",
                "fifth": "5",
                "sixth": "6",
                "seventh": "7",
                "eighth": "8",
            }),
        IntegerRef("n", 1, 100),
        IntegerRef("m", 1, 10),
        Dictation("search")
    ]
    defaults = {"n": 1, "m": "", "nth": ""}


class FirefoxPlugin(Plugin):

    """Docstring for DictationPlugin. """

    def __init__(self, manager):
        """TODO: to be defined. """

        super().__init__(manager)

    def get_grammars(self):
        grammar = Grammar(name="Git")
        grammar.add_rule(FirefoxRule())
        return [grammar]
