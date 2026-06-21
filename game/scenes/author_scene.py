from game.scenes.base_scene import BaseScene
from game.ui.message import Message


class AuthorScene(BaseScene):
    def enter(self) -> None:
        pass

    def draw(self) -> None:
        msg = Message(self.screen)
        msg.msg = "开发者:4564564"
        msg.x = 200
        msg.y = 300
        msg.show()
