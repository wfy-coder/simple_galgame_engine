import os

from game.saves.game_data import GameStats


class Display:
    FPS = 60
    WIDTH = 1500
    HEIGHT = 843
    FONT_WIDTH = 28
    TITLE = "galgame模板"
    FONT = "wenquanyizenhei"
    FONT_WIDTH_FIX = {"—": 2, "…": 2}


class Path:
    HEAD = "."
    PATH_SCRIPT = os.path.join(HEAD, "data", "script")
    PATH_SAVE = os.path.join(HEAD, "data", "save")
    PATH_FONTS = os.path.join(HEAD, "assets", "fonts")
    PATH_IMAGE = os.path.join(HEAD, "assets", "image")
    PATH_IMAGE_UI = os.path.join(HEAD, PATH_IMAGE, "ui")
    PATH_IMAGE_BACKGROUND = os.path.join(HEAD, PATH_IMAGE, "background")
    PATH_IMAGE_TRANSITION = os.path.join(HEAD, PATH_IMAGE, "transition")
    PATH_SOUNDS = os.path.join(HEAD, "assets", "sounds")


class GameStatus:
    GAMESTATES = GameStats()
    GAMESTATES.version = 0.1
    FIGURE_IMAGE = {}
    FIGURE_STR = {
        0: "常态",
        1: "微笑",
        2: "叹气",
        3: "伤心",
        4: "惊讶",
        5: "愤怒",
        6: "困倦",
    }
