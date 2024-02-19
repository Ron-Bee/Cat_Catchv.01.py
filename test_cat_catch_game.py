import unittest
import pygame
from pygame.locals import *
import random
import sys
import os
import math
import re
from contextlib import contextmanager

# Mock pygame
@contextmanager
def mock_pygame():
    mock_display = mock.Mock()
    mock_display.get_surface.return_value = mock.Mock()
    mock_display.set_mode.return_value = mock_display
    mock_event = mock.Mock()
    mock_event.type = QUIT
    mock_event.key = K_ESCAPE
    mock.patch('pygame.display', mock_display)
    mock.patch('pygame.event', mock_event)
    yield
    mock.patch.stopall()

# Mock os
@contextmanager
def mock_os():
    mock_path = mock.Mock()
    mock_path.joinpath.side_effect = lambda x: mock_path
    mock.patch('os.path', mock_path)
    yield
    mock.patch.stopall()

# Mock math
@contextmanager
def mock_math():
    mock.patch('math.sqrt', lambda x: x)
    yield
    mock.patch.stopall()

# Mock re
@contextmanager
def mock_re():
    mock.patch('re.sub', lambda x, y, z: z)
    yield
    mock.patch.stopall()

class TestCatCatchGame(unittest.TestCase):

    def setUp(self):
        self.game = CatCatchGame()

    def test_init(self):
        self.assertIsInstance(self.game.screen, pygame.Surface)
        self.assertIsInstance(self.game.clock, pygame.time.Clock)
        self.assertIsInstance(self.game.main_title, MainTitle)
        self.assertEqual(self.game.num_squares, NUM_SQUARES)
        self.assertIsInstance(self.game.paths, list)
        self.assertIsInstance(self.game.squares, list)
        self.assertIsInstance(self.game.color, tuple)
        self.assertIsInstance(self.game.center_avoid_area, pygame.Rect)
        self.assertIsInstance(self.game.main_rect, pygame.Rect)
        self.assertIsInstance(self.game.start_time, int)

    def test_generate_square_paths(self):
        self.assertEqual(len(self.game.paths), NUM_SQUARES)
        for path in self.game.paths:
            self.assertTrue(path.endswith('.png'))

    def test_create_squares(self):
        self.assertEqual(len(self.game.squares), NUM_SQUARES)
        for square in self.game.squares:
            self.assertIsInstance(square['rect'], pygame.Rect)
            self.assertTrue(square['path'].endswith('.png'))
            self.assertIn(square['direction'], ['left', 'right', 'up', 'down'])

    def test_is_in_center_avoid_area(self):
        self.assertTrue(is_in_center_avoid_area(self.game.main_rect, self.game.center_avoid_area))
        self.assertFalse(is_in_center_avoid_area(self.game.main_rect, pygame.Rect(0, 0, 1, 1)))

    def test_is_collision(self):
        square1 = {'rect': pygame.Rect(0, 0, 1, 1)}
        square2 = {'rect': pygame.Rect(1, 1, 1, 1)}
        self.assertTrue(is_collision(square1['rect'], square2['rect']))
        self.assertFalse(is_collision(square1['rect'], pygame.Rect(2, 2, 1, 1)))

    def test_find_closest_square(self):
        closest_square = find_closest_square(self.game.main_rect, self.game.squares, self.game.center_avoid_area)
        self.assertIsInstance(closest_square, dict)
        self.assertIn('rect', closest_square)
        self.assertIn('path', closest_square)
        self.assertIn('direction', closest_square)
        self.assertTrue(is_in_center_avoid_area(closest_square['rect'], self.game.center_avoid_area))

    def test_update_square_positions(self):
        with mock_pygame(), mock_os(), mock_math(), mock_re():
            update_square_positions(self.game.squares, self.game.center_avoid_area, self.game.start_time, self.game.main_rect)
            self.assertEqual(self.game.squares[0]['direction'], 'right')
            self.assertEqual(self.game.squares[1]['direction'], 'up')
            self.assertEqual(self.game.squares[2]['direction'], 'left')
            self.assertEqual(self.game.squares[3]['direction'], 'down')
            self.assertEqual(self.game.squares[4]['direction'], 'right')
            self.assertEqual(self.game.squares[5]['direction'], 'up')
            self.assertEqual(self.game.squares[6]['direction'], 'left')
            self.assertEqual(self.game.squares[7]['direction'], 'down')
            self.assertEqual(self.game.squares[8]['direction'], 'right')
            self.assertEqual(self.game.squares[9]['direction'], 'up')
            self.assertEqual(self.game.squares[10]['direction'], 'left')
            self.assertEqual(self.game.squares[11]['direction'], 'down')
            self.assertEqual(self.game.squares[12]['direction'], 'right')
            self.assertEqual(self.game.squares[13]['direction'], 'up')
            self.assertEqual(self.game.squares[14]['direction'], 'left')
            self.assertEqual(self.game.squares[15]['direction'], 'down')
            self.assertEqual(self.game.squares[16]['direction'], 'right')
            self.assertEqual(self.game.squares[17]['direction'], 'up')
            self.assertEqual(self.game.squares[18]['direction'], 'left')
            self.assertEqual(self.game.squares[19]['direction'], 'down')

    def test_display_file_name(self):
        with mock_pygame():
            file_name = 'test.png'
            display_file_name(self.game.screen, file_name)
            self.assertTrue(self.game.screen.blit.called)

    def test_draw_squares(self):
        with mock_pygame():
            draw_squares(self.game.screen, self.game.squares, self.game.color)
            self.assertTrue(self.game.screen.fill.called)
            self.assertTrue(self.game.screen.blit.called)

    def test_draw_countdown_clock(self):
        with mock_pygame():
            draw_countdown_clock(self.game.screen, self.game.start_time)
            self.assertTrue(self.game.screen.blit.called)

class CatCatchGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.main_title = MainTitle()
        self.num_squares = NUM_SQUARES
        self.paths = generate_square_paths(self.num_squares)
        self.squares = create_squares(self.num_squares, self.paths)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.center_avoid_area = CENTER_AVOID_AREA
        self.main_rect = pygame.Rect(START_POSITION[0], START_POSITION[1], SQUARE_SIZE, SQUARE_SIZE)
        self.start_time = pygame.time.get_ticks()  # Get the initial time

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        update_square_positions(self.squares, self.center_avoid_area, self.start_time, self.main_rect, speed_factor=50)

    def draw(self):
        self.screen.fill((255, 198, 198))
        self.screen.blit(self.main_title.surface, (0, 0))
        draw_squares(self.screen, self.squares, self.color)
        draw_countdown_clock(self.screen, self.start_time)

        #