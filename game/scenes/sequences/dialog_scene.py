import time
import textwrap
import pygame
from game.interpreter import ImageLoad
from game.interpreter.solver import Solver
from game.scenes import BaseScene
from game.saves import saved
from game.config import Display, GameStatus
from game.ui.message import Message


class DialogScene(BaseScene):
    def __init__(self, screen) -> None:
        self.screen: pygame.Surface = screen
        self.figure_image: pygame.Surface | None = None
        self.background_image = None
        self.dialog_ui = ImageLoad.load_ui("dialog.png")
        self.solve: Solver = Solver()

    def enter(self) -> None:
        self.is_mouse_press = False
        if GameStatus.GAMESTATES.current_show_name:
            current_show_name = GameStatus.GAMESTATES.current_show_name
            figure_image_text = (
                current_show_name + "_" + GameStatus.GAMESTATES.current_figure
            )
            self.figure_image = GameStatus.FIGURE_IMAGE[figure_image_text]

        self.background_image = ImageLoad.load_background(
            GameStatus.GAMESTATES.current_background
        )

        self.show_name_msg = Message(self.screen)
        self.show_name_msg.msg = GameStatus.GAMESTATES.current_show_name
        self.show_name_msg.x = 300
        self.show_name_msg.y = 580
        self.show_name_msg.size = 45
        self.show_name_msg.color = (232, 242, 252)
        self.show_name_msg.center = True

    def update(self) -> str:
        if self.is_mouse_press:
            time.sleep(0.1)
            pygame.event.clear()
            next_scene = self.solve.next()
            if next_scene != "none":
                saved.save(GameStatus.GAMESTATES)
                return next_scene
        else:
            self.is_mouse_press = pygame.mouse.get_pressed()[0]

    def draw(self) -> None:
        if self.background_image:
            self.screen.blit(self.background_image, (0, 0))
        if self.figure_image:
            self.screen.blit(self.figure_image, (800, 130))
        self.screen.blit(self.dialog_ui, (150, 550))

        self.show_name_msg.show()
        self.show_text_eachline()

    def show_text_eachline(self) -> None:
        line = 0
        show_text_list = []
        if isinstance(GameStatus.GAMESTATES.current_show_text, str):
            text = GameStatus.GAMESTATES.current_show_text
            text = "\n".join(textwrap.wrap(text, width=Display.FONT_WIDTH))
            show_text_list = text.split("\n")
        for show_text in show_text_list:
            show_text_msg = Message(self.screen)
            show_text_msg.msg = show_text
            show_text_msg.x = 200
            show_text_msg.y = 620 + line * 41
            show_text_msg.size = 40
            show_text_msg.color = (0, 0, 0)
            show_text_msg.show()
            line += 1
