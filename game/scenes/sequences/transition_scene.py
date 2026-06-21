import pygame
from game.interpreter.ImageLoad import load_transition
from game.interpreter.solver import Solver
from game.scenes.base_scene import BaseScene
from game.ui.message import Message
from game.saves import saved
from game.config import GameStatus


class TransitionScene(BaseScene):
    def __init__(self, screen) -> None:
        self.screen = screen
        self.timer = 0
        self.title_surface = screen  # pygame.Surface((Display.WIDTH, Display.HEIGHT))
        self.solve = Solver()

    def enter(self) -> None:
        self.chapter = GameStatus.GAMESTATES.current_show_name
        self.title = GameStatus.GAMESTATES.current_show_text
        self.background_name = GameStatus.GAMESTATES.current_background
        self.background = load_transition(self.background_name)

        self.msg_chapter = Message(self.screen)
        self.msg_chapter.msg = self.chapter
        self.msg_chapter.x = 250
        self.msg_chapter.y = 200
        self.msg_chapter.size = 100
        self.msg_chapter.center = True
        self.msg_chapter.surface = self.title_surface

        self.msg_title = Message(self.screen)
        self.msg_title.msg = self.title if isinstance(self.title, str) else "NULL"
        self.msg_title.x = 250
        self.msg_title.y = 350
        self.msg_title.size = 70
        self.msg_title.center = True
        self.msg_title.surface = self.title_surface

        self.transition_anime_enter(self.background)

    def update(self) -> str | None:
        if self.timer > 50:
            next_scene = self.solve.next()
            saved.save(GameStatus.GAMESTATES)
            if next_scene != "none":
                return next_scene

    def exit(self) -> None:
        self.transition_anime_exit(self.background)

    def draw(self) -> None:
        self.msg_title.show()
        self.msg_chapter.show()
        self.title_surface.blit(self.background, (750, 200))
        self.timer += 1

    def transition_anime_enter(self, image: pygame.Surface) -> None:
        alpha = 0
        while alpha < 255:
            self.screen.fill((0, 0, 0))
            alpha += 5
            image.set_alpha(alpha)
            self.screen.blit(image, (750, 200))
            pygame.display.flip()

    def transition_anime_exit(self, image: pygame.Surface) -> None:
        alpha = 255
        while alpha > 0:
            self.screen.fill((0, 0, 0))
            alpha -= 5
            image.set_alpha(alpha)
            self.screen.blit(image, (750, 200))
            pygame.display.flip()
