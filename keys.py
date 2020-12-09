import libqtile
from libqtile.config import Key
from libqtile.command import lazy

from groups import screenWorkSpaces

wKey = "mod4"
aKey = "mod1"
sKey = "shift"
cKey = "control"

keys = [
    # Qtile
    Key([wKey, sKey], "r", lazy.restart()),
    Key([wKey, cKey, sKey], "l", lazy.shutdown()),

    # Window
    Key([wKey, sKey], "q", lazy.window.kill()),
    Key([wKey], "f", lazy.window.toggle_fullscreen()),
    Key([wKey, sKey], "f", lazy.window.toggle_floating()),

    # Spawn
    Key([wKey], "Return", lazy.spawn("urxvt -e fish")),
    Key([wKey], "d", lazy.spawn("rofi -show drun")),

    # Layout
    Key([wKey], "Tab", lazy.next_layout()),

    # Navigate between windows
    Key([wKey], "h", lazy.layout.left()),
    Key([wKey], "j", lazy.layout.down()),
    Key([wKey], "k", lazy.layout.up()),
    Key([wKey], "l", lazy.layout.right()),

    # Shuffle curr windows
    Key([wKey, sKey], "h", lazy.layout.shuffle_left(), lazy.layout.swap_left()),
    Key([wKey, sKey], "j", lazy.layout.shuffle_down()),
    Key([wKey, sKey], "k", lazy.layout.shuffle_up()),
    Key([wKey, sKey], "l", lazy.layout.shuffle_right(), lazy.layout.swap_right()),
]

for screen, workSpaces in enumerate(screenWorkSpaces):
    for workSpace in workSpaces:
        keys.append(Key([wKey], workSpace.bind, lazy.group[workSpace.name].toscreen(screen), lazy.to_screen(screen)))

        keys.append(Key([wKey, sKey], workSpace.bind, lazy.window.togroup(workSpace.name),
                        lazy.group[workSpace.name].toscreen(screen), lazy.to_screen(screen)))
