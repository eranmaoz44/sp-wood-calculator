from BedHeads.BedHead import BedHead
from StaticVariables.StaticVariables import StaticVariables
from WoodBeams.BedHead.BigPart import BigPart
from WoodBeams.BedHead.LegPart import LegPart
from WoodBeams.BedHead.MediumPart import MediumPart


class ClassicHead(BedHead):
    _NAME = "Classic"

    def __init__(self, length, is_prepared_for_frame, is_with_hider):
        main_part_length  = length + 10 if is_prepared_for_frame  else length
        leg_length = StaticVariables.LEG_LENGTH_WITH_HIDER if is_with_hider else StaticVariables.LEG_LENGTH_WITHOUR_HIDER
        super().__init__(self._NAME,
                         length,
                         [BigPart(main_part_length), BigPart(main_part_length), MediumPart(main_part_length)],
                         [LegPart(leg_length), LegPart(leg_length)],
                         is_prepared_for_frame,
                         is_with_hider
                         )
