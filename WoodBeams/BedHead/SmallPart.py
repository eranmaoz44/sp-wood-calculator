from WoodBeams.WoodBeam import WoodBeam


class SmallPart(WoodBeam):
    def __init__(self, length):
        super().__init__(3.2, 3.2, length)

