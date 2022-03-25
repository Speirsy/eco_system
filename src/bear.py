class Bear:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.stomach = []

    def take_fish_from_river(self,fish):
        self.stomach.add(fish)
