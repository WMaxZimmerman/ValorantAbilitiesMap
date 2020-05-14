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
import get_map_choice as gmc
import helpers.resource_helper as rh


class getAgentChoice:
    global window

    def __init__(self, window):
        self.window = window

        imgName = 'Images\\AgentList.png'
        imgPath = rh.get_resource_path(imgName)

        url = 'https://valmap.s3.amazonaws.com/AgentList.png'

        with urllib.request.urlopen(url) as response, open(imgPath, 'wb') as out_file:
            data = response.read()
            out_file.write(data)

        cv_img = cvtColor(imread(imgPath), COLOR_BGR2RGB)

        height, width, ne_channels = cv_img.shape

        self.canvas = Canvas(window, width=width, height=height)
        self.canvas.bind("<Button 1>", self.agentChoice)

        self.canvas.pack()

        photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
        self.canvas.create_image(0, 0, image=photo, anchor=NW)

        window.mainloop()

    def agentChoice(self, event):
        self.canvas.pack_forget()

        if 0 <= event.y < 150:
            agentWindow = gmc.getMapChoice(self.window, 'Sova')

        elif 150 <= event.y < 300:
            agentWindow = gmc.getMapChoice(self.window, 'Viper')

        elif 300 <= event.y < 450:
            agentWindow = gmc.getMapChoice(self.window, 'Cypher')

        elif 450 <= event.y < 600:
            agentWindow = gmc.getMapChoice(self.window, 'Brimstone')

        elif event.y > 600:
            updateWindow = Toplevel(self.window)
            message = Text(updateWindow, height=6, width=75, wrap=WORD)
            message.insert(
                INSERT, 'Please update your application to include new Agents')
            message.pack()
