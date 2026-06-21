import pygame
import time
from game.config import GameStatus
from game.saves import saved
from game.ui.button import Button
from game.interpreter import ImageLoad
from game.interpreter.solver import Solver
from game.scenes.base_scene import BaseScene


# 当转到choice场景，所有选项在GameStatus.GAMESTATE.current_show_text
# 请注意这是一个list类型,每个list当中为一个tuple
# 每个tuple当中，第一项为对话内容，第二项为转入场景
class ChoiceScene(BaseScene):
    def __init__(self, screen) -> None:
        self.screen: pygame.Surface = screen
        self.background_image = None
        self.choice_button = Button(self.screen)
        self.solve: Solver = Solver()

    def enter(self) -> None:
        self.is_button_press: bool = False
        self.background_image = ImageLoad.load_background(
            GameStatus.GAMESTATES.current_background
        )
        time.sleep(0.4)
        pygame.event.clear()

    def update(self) -> str | None:
        if self.is_button_press:
            next_scene = self.solve.next()
            if next_scene != "none":
                saved.save(GameStatus.GAMESTATES)
                return next_scene

    def show_button_eachline(self) -> None:
        button_text_list = []
        if isinstance(GameStatus.GAMESTATES.current_show_text, list):
            button_text_list = GameStatus.GAMESTATES.current_show_text
        line = 0
        for button_text, next_stage in button_text_list:
            self.choice_button.reset(button_text, (400, 200 + 200 * line))
            self.choice_button.blit()
            if self.choice_button.pressed():
                time.sleep(0.1)
                self.is_button_press = True
                GameStatus.GAMESTATES.current_stage = next_stage
            line += 1

    def draw(self) -> None:
        if self.background_image:
            self.screen.blit(self.background_image, (0, 0))
        self.show_button_eachline()
