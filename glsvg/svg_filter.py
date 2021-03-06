from __future__ import absolute_import, print_function, unicode_literals, division

class SVGFilterInputs:
    SourceGraphic = 'SourceGraphic'
    SourceAlpha = 'SourceAlpha'
    BackgroundImage = 'BackgroundImage'
    BackgroundAlpha = 'BackgroundAlpha'
    FillPaint = 'FillPaint'
    StrokePaint = 'StrokePaint'


class SVGFilter:

    def __init__(self, svg):
        self.svg = svg

    def render(self, renderfn):
        # do some setup

        renderfn()

        # undo some setup