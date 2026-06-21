from game.saves import saved
from game.saves.game_data import GameStats
from game.scenes.base_scene import BaseScene
from game.ui.button import Button
from game.ui.message import Message
from game.interpreter.ImageLoad import load_background


class TitleScene(BaseScene):
    def __init__(self, screen) -> None:
        self.screen = screen

        self.title_background = load_background("标题背景.png")

        self.continue_btn = Button(screen)
        self.continue_btn.msg = "继续游戏"
        self.continue_btn.pos = (150, 350)
        self.continue_btn.text_size = 60

        self.game_start_btn = Button(screen)
        self.game_start_btn.msg = "从头开始"
        self.game_start_btn.pos = (150, 550)
        self.game_start_btn.text_size = 60

        self.game_data = GameStats()

    def enter(self) -> None:
        self.msg = Message(self.screen)
        self.msg.msg = "GALGAME模板"
        self.msg.x = 500
        self.msg.y = 100
        self.msg.size = 70
        self.msg.center = True

        self.msg.show()

    def exit(self) -> None:
        self.alpha_anime_exit(self.title_background)

    def update(self) -> str | None:
        if self.game_start_btn.pressed():
            saved.save(self.game_data)
            return "game"
        if self.continue_btn.pressed():
            return "game"

    def draw(self) -> None:
        self.screen.blit(self.title_background, (0, 0))
        self.game_start_btn.blit()
        self.continue_btn.blit()
        self.msg.show()
