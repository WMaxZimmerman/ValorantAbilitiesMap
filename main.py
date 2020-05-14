from tkinter import Tk, Canvas, NW, Button, Toplevel, Text, WORD, INSERT
from cv2 import cvtColor, imread, COLOR_BGR2RGB
import numpy as np
import PIL.Image
import PIL.ImageTk
from csv import *
from os.path import join, abspath
import sys
import urllib.request
from pathlib import Path
import get_agent_choice as gac
import helpers.resource_helper as rh


def startUp():
    imgDirPath = rh.get_resource_path('Images')
    Path(imgDirPath).mkdir(exist_ok=True)

    locDirPath = rh.get_resource_path('Locations')
    Path(locDirPath).mkdir(exist_ok=True)

    locImgDirPath = rh.get_resource_path('LocationImages')
    Path(locImgDirPath).mkdir(exist_ok=True)


startUp()
window = Tk()
window.title('Map Choice')

start = gac.getAgentChoice(window)
