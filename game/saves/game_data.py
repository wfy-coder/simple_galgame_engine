class GameStats:
    def __init__(self) -> None:
        self.version: float = 0.0
        self.time: float = 0.0
        self.current_stage: int = 1
        self.current_stage_dialog: int = 1
        self.current_show_name: str | None = "姓名"
        self.current_show_text: str | list[tuple[str, int]] = "一个对话"
        self.current_background: str = "background.png"
        self.current_figure: str = "figure.png"

    def __repr__(self) -> str:
        return f"GameStats(stage={self.current_stage},dialog={self.current_stage_dialog},background={self.current_background})"
