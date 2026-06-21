import pygame

from game.interpreter import ImageLoad
from game.ui.message import Message


class Button:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.msg = "请输入文本"
        self.pos = []
        self.text_size = 40
        self.image_btn = ImageLoad.load_ui("button.png")

    def blit(self) -> None:
        if self.check_collision(
            pygame.mouse.get_pos(), (0, 0), self.pos, self.image_btn.get_size()
        ):
            self.image_btn.set_alpha(240)
        else:
            self.image_btn.set_alpha(180)
        self.screen.blit(self.image_btn, self.pos)
        msg = Message(self.screen)
        msg.msg = self.msg
        msg.x = self.pos[0] + self.image_btn.get_size()[0] / 2
        msg.y = self.pos[1] + self.image_btn.get_size()[1] / 2
        msg.center = True
        msg.size = self.text_size

        msg.show()

    def check_collision(self, pos1, box1, pos2, box2) -> bool:
        return (
            abs(pos1[0] + box1[0] / 2 - pos2[0] - box2[0] / 2) < (box1[0] + box2[0]) / 2
            and abs(pos1[1] + box1[1] / 2 - pos2[1] - box2[1] / 2)
            < (box1[1] + box2[1]) / 2
        )

    def pressed(self):
        return (
            self.check_collision(
                pygame.mouse.get_pos(), (0, 0), self.pos, self.image_btn.get_size()
            )
            and pygame.mouse.get_pressed()[0]
        )

    def reset(self, msg, pos) -> None:
        self.msg = msg
        self.pos = pos
