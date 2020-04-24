from WoodBeams.WoodBeam import WoodBeam


class LegPart(WoodBeam):
    def __init__(self, length):
        super().__init__(3.2, 14.5, length)
