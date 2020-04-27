class BedHead(object):
    def __init__(self, name, length, main_parts, legs, is_prepared_for_frame, is_with_hider):
        self.name = name
        self.length = length
        self.main_parts = main_parts
        self.legs = legs
        self.is_prepared_for_frame = is_prepared_for_frame
        self.is_with_hider = is_with_hider

    def __str__(self) -> str:
        '{0} Bed, length {1}, main_parts {2}, legs {3}, prepared_for_frame: {4}, is_with_hider {5}'.format(
            self.name,
            self.length,
            ', '.join(self.main_parts),
            ', '.join(self.legs),
            self.is_prepared_for_frame,
            self.is_with_hider
        )


