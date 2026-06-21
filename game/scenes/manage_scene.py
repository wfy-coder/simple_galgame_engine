import pygame
from typing import Dict
from game.scenes.base_scene import BaseScene


class SceneManager:
    def __init__(self, screen: pygame.Surface) -> None:
        self.screen: pygame.Surface = screen
        self.scenes: Dict[str, BaseScene] = {}
        self.current_scene: BaseScene | None = None

    def register(self, name: str, scene: BaseScene) -> None:
        self.scenes[name] = scene

    def switch(self, name: str) -> None:
        if self.current_scene:
            self.current_scene.exit()

        self.current_scene = self.scenes.get(name)

        if self.current_scene:
            self.current_scene.enter()

    def draw(self) -> None:
        if self.current_scene:
            self.current_scene.draw()

    def update(self) -> None:
        if self.current_scene:
            result = self.current_scene.update()
            if result:
                self.switch(result)
