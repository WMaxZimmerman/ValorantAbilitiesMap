from tkinter import Tk
from pathlib import Path
import get_agent_choice as gac
from ui.menus.agent_menu import AgentMenu
import helpers.resource_helper as rh


def run():
    imgDirPath = rh.get_resource_path('Images')
    Path(imgDirPath).mkdir(exist_ok=True)

    locDirPath = rh.get_resource_path('Locations')
    Path(locDirPath).mkdir(exist_ok=True)

    locImgDirPath = rh.get_resource_path('LocationImages')
    Path(locImgDirPath).mkdir(exist_ok=True)

    window = Tk()
    window.title('Map Choice')

    start = AgentMenu(window)


if __name__ == "__main__":
    run()
