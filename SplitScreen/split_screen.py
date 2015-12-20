"""
SplitScreen v1.0.0
by Nick Fisher
https://github.com/spadgos/sublime-SplitScreen
"""
import sublime_plugin, sublime
import re


def addUp(lst):
    out = [0.0]
    for i in lst:
        out.append(out[-1] + i)

    return out


class SplitScreenCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Split ratios", "70:30", self.splitWindow, None, None)

    def splitWindow(self, inp):
        # sublime.message_dialog(inp)
        parts = re.split("\\s*,\\s*", inp)

        horiz = parts[0] or "1"
        vert = parts[1] or "1" if len(parts) > 1 else "1"

        vert = map(float, re.split(":", vert))
        horiz = map(float, re.split(":", horiz))
        vertTotal = sum(vert)
        horizTotal = sum(horiz)
        vert = map((lambda x: x / vertTotal), vert)
        horiz = map((lambda x: x / horizTotal), horiz)

        # cols = addUp(horiz)
        # rows = addUp(vert)

        # cells = []
        # for x, val1 in enumerate(horiz):
        #     for y, val2 in enumerate(vert):
        #         cells.append([x, y, x + 1, y + 1])


# self.window.run_command('set_layout', {
#     "cols": [0, 0.5, 1],
#     "rows": [0, 1],
#     "cells": [[0, 0, 1, 1], [1, 0, 2, 1]]
# })
# 
# self.window.run_command('set_layout', {
#     "cols": [0, 0.5, 1],
#     "rows": [0, 0.5, 1],
#     "cells": [[0, 0, 1, 1], [1, 0, 2, 1],
#               [0, 1, 1, 2], [1, 1, 2, 2]]
# })
# 
# self.window.run_command('set_layout', {
#     "cols": [0, 0.5, 1],
#     "rows": [0, 0.5, 1],
#     "cells": [[0, 0, 1, 2], [1, 0, 2, 1], [1, 1, 2, 2]]
# })