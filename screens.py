import fontawesome as fa

from libqtile.config import Screen
from bar import new_bar
from groups import screenWorkSpaces

screens = []

for workspaces in screenWorkSpaces:
    screens.append(Screen(
        top=new_bar(
            [workspace.name for workspace in workspaces]
        )
    ))
