import time

from game.interpreter import ImageLoad
from game.interpreter.solver import Solver
from game.saves import saved
from game.config import GameStatus
from game.scenes.base_scene import BaseScene
from game.scenes.manage_scene import SceneManager
from game.scenes.sequences.dialog_scene import DialogScene
from game.scenes.sequences.choice_scene import ChoiceScene
from game.scenes.sequences.end_scene import EndScene
from game.scenes.sequences.transition_scene import TransitionScene


from typing import Optional
class GameScenes(BaseScene):
    def __init__(self, screen) -> None:
        self.screen = screen
        self.solve = Solver()

        self.manage_scene = SceneManager(self.screen)

        self.manage_scene.register("transition", TransitionScene(screen))
        self.manage_scene.register("dialog", DialogScene(screen))
        self.manage_scene.register("choice", ChoiceScene(screen))
        self.manage_scene.register("end", EndScene(screen))

    def enter(self) -> None:
        game_process = saved.load()
        GameStatus.GAMESTATES = game_process
        GameStatus.GAMESTATES.current_stage_dialog -= 1
        GameStatus.FIGURE_IMAGE = ImageLoad.load_all_figure()

        next_scene = self.solve.next()
        if next_scene != "none":
            saved.save(GameStatus.GAMESTATES)
            self.manage_scene.switch(next_scene)

    def update(self) -> Optional[str]:
        GameStatus.GAMESTATES.time = time.time()
        return self.manage_scene.update()

    def draw(self) -> None:
        self.manage_scene.draw()
