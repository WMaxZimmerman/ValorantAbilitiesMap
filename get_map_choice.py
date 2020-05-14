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
import show_map as sm
import helpers.resource_helper as rh


class getMapChoice:
    global window

    def __init__(self, window, agent):
        self.window = window
        self.agent = agent
        imgName = 'Images\\MapList.png'
        imgPath = rh.get_resource_path(imgName)

        url = 'https://valmap.s3.amazonaws.com/MapList.png'

        with urllib.request.urlopen(url) as response, open(imgPath, 'wb') as out_file:
            data = response.read()
            out_file.write(data)

        cv_img = cvtColor(imread(imgPath), COLOR_BGR2RGB)

        height, width, ne_channels = cv_img.shape

        self.canvas = Canvas(window, width=width, height=height)
        self.canvas.bind("<Button 1>", self.mapChoice)

        self.canvas.pack()

        photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
        self.canvas.create_image(0, 0, image=photo, anchor=NW)

        self.B = Button(self.window, text="Back", command=lambda: [
                        self.B.destroy(), self.canvas.pack_forget(), getAgentChoice(self.window)])
        self.B.pack()

        window.mainloop()

    def mapChoice(self, event):
        self.canvas.pack_forget()
        self.B.destroy()

        if 0 <= event.y < 200:
            mapWindow = sm.showMap(self.window, 'Bind', self.agent)

        elif 200 <= event.y < 400:
            mapWindow = sm.showMap(self.window, 'Haven', self.agent)

        elif 400 <= event.y < 600:
            mapWindow = sm.showMap(self.window, 'Split', self.agent)
