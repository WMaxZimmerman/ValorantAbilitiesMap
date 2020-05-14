from tkinter import Canvas, Toplevel, Text, NW, Button
from cv2 import cvtColor, imread, COLOR_BGR2RGB
import PIL.ImageTk
import urllib.request
import helpers.resource_helper as rh
import show_map as sm
from ui.menus.base_menu import BaseMenu


class MapMenu(BaseMenu):
    def __init__(self, window, agent, backTarget):
        options = [
            "Bind",
            "Haven",
            "Split"
        ]
        typeName = 'MapList'
        super().__init__(
            window,
            options,
            typeName,
            sm.showMap,
            [agent],
            backTarget
        )
