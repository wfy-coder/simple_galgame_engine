import pygame
import sys

from game.game_loop import Game
from game.config import Display


def main() -> None:
    pygame.init()
    pygame.display.set_caption(Display.TITLE)
    screen = pygame.display.set_mode((Display.WIDTH, Display.HEIGHT), pygame.DOUBLEBUF)
    Game(screen).run()


if __name__ == "__main__":
    sys.exit(main())
