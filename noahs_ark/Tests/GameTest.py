import unittest

from noahs_ark.Code.Pieces import *
from noahs_ark.Code.Coordinate import Coordinate
from noahs_ark.Code.Game import Game, Grid


# noinspection PyBroadException
class GameTest(unittest.TestCase):

    def setUp(self) -> None:
        self.game = Game()


    def test_initial_animals(self):
        for _ in range(1000):
            try:
                self.setUp()
                self.game.place_initial_animals()
            except Exception:
                self.fail("Exception raised unexpectedly!")


class GridTest(unittest.TestCase):

    def setUp(self) -> None:
        self.grid = Grid()


    def test_validity(self):
        self.assertTrue(self.grid.is_valid_coordinate(Coordinate(0, 0)))
        self.assertTrue(self.grid.is_valid_coordinate(Coordinate(5, 0)))
        self.assertTrue(self.grid.is_valid_coordinate(Coordinate(0, 8)))
        self.assertTrue(self.grid.is_valid_coordinate(Coordinate(5, 8)))

        self.assertFalse(self.grid.is_invalid_coordinate(Coordinate(0, 0)))

        self.assertFalse(self.grid.is_valid_coordinate(Coordinate(-1, 0)))
        self.assertFalse(self.grid.is_valid_coordinate(Coordinate(0, -1)))
        self.assertFalse(self.grid.is_valid_coordinate(Coordinate(0, 9)))
        self.assertFalse(self.grid.is_valid_coordinate(Coordinate(7, 0)))
        self.assertFalse(self.grid.is_valid_coordinate(Coordinate(7, 9)))




    def test_placing_at_coordinates(self):
        # HIPPO
        hippo_male = Hippo(Gender.MALE)
        self.assertTrue(self.grid.can_be_placed_at_coordinates(Coordinate(1, 2), hippo_male))
        self.assertTrue(self.grid.can_be_placed_at_coordinates(Coordinate(1, 4), hippo_male))
        self.assertTrue(self.grid.can_be_placed_at_coordinates(Coordinate(3, 1), hippo_male))

        self.assertFalse(self.grid.can_be_placed_at_coordinates(Coordinate(1, 6), hippo_male))
        self.assertFalse(self.grid.can_be_placed_at_coordinates(Coordinate(1, 7), hippo_male))
        self.assertFalse(self.grid.can_be_placed_at_coordinates(Coordinate(0, 2), hippo_male))
        self.assertFalse(self.grid.can_be_placed_at_coordinates(Coordinate(5, 1), hippo_male))

        # LION
        lion_female = Lion(Gender.FEMALE)
        self.assertTrue(self.grid.can_be_placed_at_coordinates(Coordinate(1, 2), lion_female))
        self.assertTrue(self.grid.can_be_placed_at_coordinates(Coordinate(3, 6), lion_female))

        self.assertFalse(self.grid.can_be_placed_at_coordinates(Coordinate(3, 8), lion_female))

        # ELEPHANT
        elephant_female = Elephant(Gender.FEMALE)
        self.assertTrue(self.grid.can_be_placed_at_coordinates(Coordinate(1, 6), elephant_female))
        self.assertTrue(self.grid.can_be_placed_at_coordinates(Coordinate(1, 3), elephant_female))

        self.assertFalse(self.grid.can_be_placed_at_coordinates(Coordinate(1, 8), elephant_female))


if __name__ == '__main__':
    unittest.main()
