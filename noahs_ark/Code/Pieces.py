from abc import ABC, abstractmethod
from enum import Enum


class PieceType(Enum):
    FREE = 0
    WALL = 1
    HIPPO = 2
    ZEBRA = 4
    LION = 6
    GIRAFFE = 8
    ELEPHANT = 10


    @staticmethod
    def get_animal_piece_types():
        return [PieceType.HIPPO, PieceType.ZEBRA, PieceType.LION, PieceType.GIRAFFE, PieceType.ELEPHANT]

    def get_fancy_identifier(self):
        if self == PieceType.FREE:
            return ' '
        return self.name.upper()[0]


class Gender(Enum):
    MALE = 0
    FEMALE = 1


    def is_male(self):
        return self == Gender.MALE


class Piece(ABC):
    piece_type: PieceType


    def __init__(self, piece_type: PieceType):
        self.piece_type = piece_type


    def get_number(self):
        return self.piece_type.value

    def get_fancy_identifier(self):
        return self.piece_type.get_fancy_identifier()


class Wall(Piece):

    def __init__(self):
        super().__init__(PieceType.WALL)


class Free(Piece):

    def __init__(self):
        super().__init__(PieceType.FREE)


class Animal(Piece):
    gender: Gender


    def __init__(self, species: PieceType, gender: Gender):
        super().__init__(species)
        self.gender = gender


    def is_male(self):
        return self.gender.is_male()


    def get_number(self):
        return self.piece_type.value + self.gender.value

    def get_name(self):
        return self.piece_type.name.title()


    @abstractmethod
    def get_pattern(self) -> list[list[int]]:
        pass


class Hippo(Animal):

    def __init__(self, gender: Gender):
        super().__init__(PieceType.HIPPO, gender)


    def get_pattern(self):
        if self.is_male():
            return [[1, 1, 1],
                    [0, 0, 0]]
        else:
            return [[1, 1, 0],
                    [0, 0, 0]]


class Zebra(Animal):

    def __init__(self, gender: Gender):
        super().__init__(PieceType.ZEBRA, gender)


    def get_pattern(self):
        if self.is_male():
            return [[1, 1, 0],
                    [0, 0, 0]]
        else:
            return [[1, 0, 0],
                    [1, 0, 0]]


class Lion(Animal):

    def __init__(self, gender: Gender):
        super().__init__(PieceType.LION, gender)


    def get_pattern(self):
        if self.is_male():
            return [[1, 1, 0],
                    [0, 0, 0]]
        else:
            return [[1, 1, 0],
                    [1, 0, 0]]


class Giraffe(Animal):

    def __init__(self, gender: Gender):
        super().__init__(PieceType.GIRAFFE, gender)


    def get_pattern(self):
        if self.is_male():
            return [[0, 1, 0],
                    [1, 1, 0]]
        else:
            return [[1, 0, 0],
                    [1, 0, 0]]


class Elephant(Animal):

    def __init__(self, gender: Gender):
        super().__init__(PieceType.ELEPHANT, gender)


    def get_pattern(self):
        if self.is_male():
            return [[1, 1, 0],
                    [0, 0, 0]]
        else:
            return [[1, 0, 0],
                    [1, 1, 0]]


def get_animals_to_place() -> list[Animal]:
    return [Hippo(Gender.MALE),
            Hippo(Gender.FEMALE),
            Zebra(Gender.MALE),
            Zebra(Gender.FEMALE),
            Lion(Gender.MALE),
            Lion(Gender.FEMALE),
            Giraffe(Gender.MALE),
            Giraffe(Gender.FEMALE),
            Elephant(Gender.MALE),
            Elephant(Gender.FEMALE)]
