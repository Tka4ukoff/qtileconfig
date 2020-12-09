import fontawesome as fa

from dataclasses import dataclass
from libqtile.config import Match, Group


@dataclass
class WorkSpace:
    name: str
    icon: str
    bind: str
    matches: [Match] = None


screenWorkSpaces = [
    [
        WorkSpace(name="Code", icon=fa.icons["code"], bind="6"),
        WorkSpace(name="Docker", icon=fa.icons["cloud"], bind="7"),
        WorkSpace(name="Terminal", icon=fa.icons["terminal"], bind="8"),
        WorkSpace(name="FM", icon=fa.icons["file"], bind="9"),
        WorkSpace(name="Git", icon=fa.icons["code-branch"], bind="0"),
    ],
    [
        WorkSpace(name="Firefox", icon=fa.icons["firefox"], bind="1"),
        WorkSpace(name="Database", icon=fa.icons["database"], bind="2"),
        WorkSpace(name="Player", icon=fa.icons["play-circle"], bind="3"),
        WorkSpace(name="Social", icon=fa.icons["telegram"], bind="4"),
        WorkSpace(name="5", icon=fa.icons["database"], bind="5"),
    ]
]

groups = []
for workspaces in screenWorkSpaces:
    for workspace in workspaces:
        groups.append(Group(
            name=workspace.name,
            label=workspace.icon,
            matches=workspace.matches
        ))
