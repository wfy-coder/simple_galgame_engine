import pygame
import sys

from game.config import Display
from game.scenes import SceneManager
from game.scenes.author_scene import AuthorScene
from game.scenes.title_scene import TitleScene
from game.scenes.game_scene import GameScenes


class Game(object):
    def __init__(self, screen) -> None:
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()

        self.scene_manager = SceneManager(screen)

        self.scene_manager.register("title", TitleScene(screen))
        self.scene_manager.register("author", AuthorScene(screen))
        self.scene_manager.register("game", GameScenes(screen))

        self.scene_manager.switch("title")

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def update(self) -> None:
        self.scene_manager.update()

    def draw(self) -> None:
        self.scene_manager.draw()
        pygame.display.flip()

    def run(self) -> None:
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(Display.FPS)
