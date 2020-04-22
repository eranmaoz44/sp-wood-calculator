class WoodBeam(object):
    def __init__(self, width, height, length):
        self.width = width
        self.height = height
        self.length = length

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_length(self):
        return self.length

    def __str__(self) -> str:
        return "{0} x {1}\t{2}".format(self.width, self.height, self.length)





