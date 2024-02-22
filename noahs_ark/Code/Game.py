import random

from noahs_ark.Code.Coordinate import Coordinate
from noahs_ark.Code.Pieces import *


class Grid:
    fields: list[list[Piece]]

    def __init__(self):
        self.fields = [[Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall()],
                       [Wall(), Wall(), Free(), Free(), Free(), Free(), Free(), Wall(), Wall()],
                       [Wall(), Free(), Free(), Free(), Free(), Free(), Free(), Free(), Wall()],
                       [Wall(), Free(), Free(), Free(), Free(), Free(), Free(), Free(), Wall()],
                       [Wall(), Free(), Free(), Free(), Free(), Free(), Free(), Free(), Wall()],
                       [Wall(), Wall(), Free(), Free(), Free(), Free(), Free(), Wall(), Wall()],
                       [Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall(), Wall()]]


    def get_max_row_index(self) -> int:
        return len(self.fields)-1


    def get_max_col_index_in_row(self, row: int) -> int:
        return len(self.fields[row])-1

    def get_field_coordinates(self) -> list[Coordinate]:
        return [Coordinate(y, x) for y in range(len(self.fields)) for x in range(len(self.fields[y]))]

    def is_unsolvable(self):

        for coordinate in self.get_field_coordinates():
            if self.is_free_with_no_free_neighbours(coordinate):
                return True
        return False


    def

    def is_free_with_no_free_neighbours(self, coordinate: Coordinate) -> bool:
        if not self.coordinate_is_free(coordinate):
            return False
        for c in coordinate.get_surrounding_coordinates():
            if self.coordinate_is_free(c):
                return False
        return True



    def place_at_coordinate(self, coordinate: Coordinate, animal: Animal) -> bool:
        can_be_placed: bool = self.can_be_placed_at_coordinates(coordinate, animal)
        if can_be_placed:
            animal_pattern = animal.get_pattern()
            for dy in range(len(animal_pattern)):
                for dx in range(len(animal_pattern[dy])):
                    iter_x = coordinate.x + dx
                    iter_y = coordinate.y + dy
                    if animal_pattern[dy][dx] == 1:
                        self.fields[iter_y][iter_x] = animal
        return can_be_placed


    def can_be_placed_at_coordinates(self, coordinate: Coordinate, animal: Animal) -> bool:
        if not self.is_valid_coordinate(coordinate):
            return False

        animal_pattern = animal.get_pattern()
        for dy in range(len(animal_pattern)):
            for dx in range(len(animal_pattern[dy])):
                iter_x = coordinate.x + dx
                iter_y = coordinate.y + dy
                iter_coordinate = Coordinate(iter_y, iter_x)
                if animal_pattern[dy][dx] == 1:
                    if self.is_invalid_coordinate(iter_coordinate):
                        return False
                    if self.coordinate_is_blocked(iter_coordinate):
                        return False
        return True


    def is_valid_coordinate_for_animal(self, coordinate: Coordinate, animal: Animal):
        if self.get_max_row_index() < (coordinate.y + len(animal.get_pattern())):
            return False
        if self.get_max_col_index_in_row(coordinate.y) < (coordinate.x + len(animal.get_pattern()[0])):
            return False
        return True


    def is_invalid_coordinate(self, coordinate: Coordinate) -> bool:
        return not self.is_valid_coordinate(coordinate)


    def is_valid_coordinate(self, coordinate: Coordinate) -> bool:
        if (coordinate.x < 0) or (coordinate.y < 0):
            return False
        if coordinate.x >= len(self.fields[0]):
            return False
        if coordinate.y >= len(self.fields):
            return False
        return True


    def get_random_free_grid_field(self) -> Coordinate:
        free_fields = [Coordinate(y, x)
                       for x in range(len(self.fields[0]))
                       for y in range(len(self.fields))
                       if self.coordinate_is_free(Coordinate(y, x))]
        return random.choice(free_fields)


    def coordinate_is_blocked(self, coordinate: Coordinate) -> bool:
        return not self.coordinate_is_free(coordinate)


    def coordinate_is_free(self, coordinate: Coordinate) -> bool:
        piece = self.get_piece_at_coordinate(coordinate)
        if not piece:
            return False
        return isinstance(piece, Free)

    def get_piece_at_coordinate(self, coordinate: Coordinate) -> None | Piece:
        if not self.is_valid_coordinate(coordinate):
            return None
        return self.fields[coordinate.y][coordinate.x]


    def __str__(self):
        output = ""
        for line in self.fields:
            output += ', '.join([f"{row.get_number():02d}" for row in line]) + "\n"
        return output


    def __copy__(self):
        newone = type(self)()
        newone.fields = self.fields
        return newone



    upper_line_char = '='
    side_line_char = '|'
    between_line_horizontal_char = '-'
    between_line_vertical_char = '|'
    intersection_char = '+'
    padding_horizontal = 2
    length_of_identifier = 1

    def fancy_output(self) -> str:
        output = ""
        lines = []
        for line in self.fields:
            lines.append(self.side_line_char + self.between_line_vertical_char.join([f"{' '*self.padding_horizontal}{animal.get_fancy_identifier()}{' ' * self.padding_horizontal}" for animal in line]) + self.side_line_char + '\n')
        line_length = len(lines[0])
        for l in lines:
            if len(l) != line_length:
                raise Exception(f"Line length is differing, please check fancy output!")
        head_bottom_line = self.intersection_char + self.intersection_char.join([self.upper_line_char *
                                                  (2 * self.padding_horizontal + self.length_of_identifier) for _ in range(len(self.fields[0]))]) + self.intersection_char + '\n'
        between_line = self.intersection_char + self.intersection_char.join([self.between_line_horizontal_char *
                                                  (2 * self.padding_horizontal + self.length_of_identifier) for _ in range(len(self.fields[0]))]) + self.intersection_char + '\n'
        output = head_bottom_line + between_line.join([line for line in lines]) + head_bottom_line

        return output


class Game:

    animals_to_place: list[Animal]
    grid: Grid


    def __init__(self):
        self.animals_to_place = get_animals_to_place()
        self.grid = Grid()

    def place_initial_animals(self):
        initial_animals_placed = 3
        animals = [self.get_random_animal() for _ in range(initial_animals_placed)]
        for animal in animals:
            while True:
                coordinate = self.grid.get_random_free_grid_field()
                if self.grid.can_be_placed_at_coordinates(coordinate, animal):
                    self.grid.place_at_coordinate(coordinate, animal)
                    break

    def place_animal(self, coordinate: Coordinate, animal_type: PieceType, gender: Gender):
        animal = self.animals_to_place
        if not self.grid.place_at_coordinate(coordinate, animal):
            raise Exception(f"{animal.get_name()} can not be placed at {coordinate}")



    def get_random_animal(self) -> Animal:
        animal = random.choice(self.animals_to_place)
        self.animals_to_place.remove(animal)
        return animal




    def __str__(self):
        return self.grid.__str__()

    def fancy_output(self) -> str:
        return self.grid.fancy_output()
