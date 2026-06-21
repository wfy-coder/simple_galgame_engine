from game.config import GameStatus
from game.utils import read_script


class Solver:
    def __init__(self) -> None:
        self.text = read_script()

    def next(self) -> str:
        stage = GameStatus.GAMESTATES.current_stage
        dialog = GameStatus.GAMESTATES.current_stage_dialog
        return self.script_handle(self.text[str(stage)][dialog])

    def switch_background(self, text: list) -> str:
        GameStatus.GAMESTATES.current_background = text[1]
        return "none"

    def switch_dialog(self, text: list) -> str:
        GameStatus.GAMESTATES.current_show_name = text[0]
        GameStatus.GAMESTATES.current_show_text = text[2]
        GameStatus.GAMESTATES.current_figure = (
            text[1] if isinstance(text[1], str) else GameStatus.FIGURE_STR[text[1]]
        )
        return "dialog"

    def switch_transition(self, text: list) -> str:
        GameStatus.GAMESTATES.current_show_name = text[1]
        GameStatus.GAMESTATES.current_show_text = text[2]
        GameStatus.GAMESTATES.current_background = text[3]
        return "transition"

    def switch_choice(self, text: list) -> str:
        GameStatus.GAMESTATES.current_stage_dialog = 0
        GameStatus.GAMESTATES.current_show_text = text[1:]
        return "choice"

    def switch_call(self, text: list) -> str:
        GameStatus.GAMESTATES.current_stage_dialog = 0
        GameStatus.GAMESTATES.current_stage = text[1]
        return "none"

    def switch_end(self) -> str:
        return "end"

    def script_handle(self, text: list) -> str:
        GameStatus.GAMESTATES.current_stage_dialog += 1
        match text[0]:
            case "@T":
                return self.switch_transition(text)
            case "@B":
                return self.switch_background(text)
            case "@S":
                return self.switch_choice(text)
            case "@P":
                return self.switch_call(text)
            case "@E":
                return self.switch_end()
            case _:
                return self.switch_dialog(text)
