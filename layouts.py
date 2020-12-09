from libqtile import layout

layout_theme = {
    "border_width": 2,
    "margin": 6,
    "border_focus": "e1acff",
    "border_normal": "1D2330"
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Stack(num_stacks=2),
]
