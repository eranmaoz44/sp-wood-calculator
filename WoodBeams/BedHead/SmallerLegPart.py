from WoodBeams.WoodBeam import WoodBeam


class SmallerLegPart(WoodBeam):
    def __init__(self, length):
        super().__init__(3.2, 9, length)

