

class Coordinate:
    x: int
    y: int

    def __init__(self, y: int, x: int):
        self.x = x
        self.y = y


    def get_surrounding_coordinates(self):
        modifiers = [-1, 1]
        return [Coordinate(self.y + dy, self.x + dx) for dy in modifiers for dx in modifiers]


    def __str__(self):
        return f"({self.y},{self.x})"

