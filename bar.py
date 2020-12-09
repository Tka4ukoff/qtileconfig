from libqtile import bar, widget
from colors import colors


def new_bar(vg):
    return bar.Bar(
        [
            # Group box
            widget.GroupBox(
                visible_groups=vg,
                highlight_method="line",
                highlight_color=colors["comment_grey"],

                urgent_border=colors["light_red"],
                inactive=colors["light_yellow"],
                active=colors["blue"],

                fontsize=16,
                borderwidth=0
            ),

            widget.Sep(linewidth=2, size_percent=100, padding=12),

            # Window Name
            widget.WindowName(
                fontsize=14,
                font="Fira Code"
            ),

            # Time
            widget.Clock(
                format="%B %d  [ %H:%M ]",
                fontsize=14,
                font="Fira Code"
            ),
            # Keyboard layout
            widget.KeyboardLayout(
                configured_keyboards=['us', 'ru'],
                fontsize=14,
                font="Fira Code"
            ),
            widget.Systray(),
        ],
        30,
        background=colors["black"]
    )
