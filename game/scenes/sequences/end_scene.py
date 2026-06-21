import sys
import time
import os
import pygame
from game.config import GameStatus
from game.interpreter.ImageLoad import load_background
from game.scenes.base_scene import BaseScene
from game.ui.message import Message


from typing import Optional
class EndScene(BaseScene):
    def __init__(self, screen) -> None:
        self.screen = screen
        self.is_mouse_press = False

        self.msg = Message(self.screen)
        self.msg.msg = "完"
        self.msg.x = 750
        self.msg.y = 250
        self.msg.size = 400
        self.msg.center = True

    def enter_anime(self, image) -> None:
        alpha = 255
        while alpha > 0:
            self.screen.fill((0, 0, 0))
            alpha -= 2
            image.set_alpha(alpha)
            self.msg.alpha = 255 - alpha
            self.screen.blit(image, (0, 0))
            self.msg.show()
            pygame.display.flip()

    def enter(self) -> None:
        self.background_name = GameStatus.GAMESTATES.current_background
        self.background = load_background(self.background_name)

        self.enter_anime(self.background)

    def update(self) -> Optional[str]:
        if self.is_mouse_press:
            time.sleep(0.1)
            os.execl(sys.executable, sys.executable, *sys.argv)
        else:
            self.is_mouse_press = pygame.mouse.get_pressed()[0]

    def draw(self) -> None:
        self.msg.show()
