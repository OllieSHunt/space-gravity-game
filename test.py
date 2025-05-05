import unittest
import pygame

import utils

# Unit tests for the functions in utils.py
class TestUtils(unittest.TestCase):
    # Tests for the "angle_between" function
    def test_angle_between(self):
        self.assertEqual(utils.angle_between(pygame.Vector2(0, 1), pygame.Vector2(1, 0)), 45)
        self.assertEqual(utils.angle_between(pygame.Vector2(0, -1), pygame.Vector2(-1, 0)), -135)
        self.assertEqual(utils.angle_between(pygame.Vector2(1, 0), pygame.Vector2(0, 1)), -135)
        self.assertEqual(utils.angle_between(pygame.Vector2(-1, 0), pygame.Vector2(0, -1)), 45)
        self.assertEqual(utils.angle_between(pygame.Vector2(0.5, 0.5), pygame.Vector2(0.5, 0.5)), 0)
        self.assertEqual(utils.angle_between(pygame.Vector2(0.5, 0.5), pygame.Vector2(1.5, 1.5)), -45)

    # Tests for the "find_first_of_type" function
    def test_find_first_of_type(self):
        # Test data
        test_list = [1, 2.3, "4"]

        self.assertEqual(utils.find_first_of_type(test_list, int), 1)
        self.assertEqual(utils.find_first_of_type(test_list, float), 2.3)
        self.assertEqual(utils.find_first_of_type(test_list, str), "4")

        # Should return None if not found
        self.assertEqual(utils.find_first_of_type(test_list, bool), None)

if __name__ == '__main__':
    unittest.main()
