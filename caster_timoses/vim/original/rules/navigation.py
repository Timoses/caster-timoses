from dragonfly import MappingRule, Key, IntegerRef, Text, Repeat
# FIXME: Just import config
from ..vim_config import get_config

c = get_config()

class NavigationRule(MappingRule):
    mapping = {
        # Jump list:
        # (gist = jump list)
        "go old | gist up": Key("c-o"),
        "go new | gist down": Key("c-i"),

        "go old file | gist file up": Key("c-o:2/150, enter"),
        "go new file | gist file down": Key("c-i:2/150, enter"),

        "go alternate": Key("colon, e, hash, enter"),

        "go file": Key("g, f"),
        "go tag": Key("c-rbracket"),
        "go tag back": Key("c-t"),

        # Cursor:
        "cursor top": Key("s-h"),
        "cursor middle": Key("s-m"),
        "cursor (low | bottom)": Key("s-l"),

        # Windows/viewports:
        "win west": Key(c.system.windowSwitchPrefix + "h"),
        "win east": Key(c.system.windowSwitchPrefix + "l"),
        "win north": Key(c.system.windowSwitchPrefix + "k"),
        "win south": Key(c.system.windowSwitchPrefix + "j"),
        "win switch": Key("c-w, c-w"),

        "win split": Key("c-w, s"),
        "win (vault | fault)": Key("c-w, v"),

        "win equal": Key("c-w, equal"),

        # Tabs:
        "[<n>] tab right": Key("g, t") * Repeat(extra="n"),
        "[<n>] tab left": Key("g, s-t") * Repeat(extra="n"),
        "tab [<n>]": Key("%(n)d, g, t"),

        # Lines:
        "go line <n100>": Text("%(n100)dgg"),

        # New:
        "new tab": Key("colon") + Text("tabnew") + Key("enter"),
        "new split": Key("colon") + Text("split") + Key("enter"),
        "new fault": Key("colon") + Text("vsplit") + Key("enter"),
    }
    extras = [
        IntegerRef("n", 1, 10),
        IntegerRef("n100", 1, 100),
    ]
    defaults = {
        "n": 1,
    }
