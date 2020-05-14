from tkinter import Canvas, NW, Button, Text, WORD, INSERT, Toplevel
from cv2 import cvtColor, imread, COLOR_BGR2RGB
import numpy as np
import PIL.Image
import PIL.ImageTk
from csv import *
import urllib.request
import helpers.resource_helper as rh


class showMap:
    global windowMaster
    global canvas
    global height
    global width
    global mapName
    global agentName

    def __init__(self, caller, window, mapName, agent):
        self.caller = caller
        self.windowMaster = window
        self.mapName = mapName
        self.agentName = agent
        self.setUp()

    def setUp(self):
        imgName = 'Images\\' + self.mapName + 'Sides.png'
        imgPath = rh.get_resource_path(imgName)

        url = 'https://valmap.s3.amazonaws.com/' + self.mapName + 'Sides.png'

        with urllib.request.urlopen(url) as response, open(imgPath, 'wb') as out_file:
            data = response.read()
            out_file.write(data)

        self.windowMaster.title(self.mapName)

        imgPath = rh.get_resource_path(imgName)

        cv_img = cvtColor(imread(imgPath), COLOR_BGR2RGB)

        self.height, self.width, ne_channels = cv_img.shape

        self.canvas = Canvas(
            self.windowMaster, width=self.width, height=self.height)
        self.canvas.bind("<Button 1>", self.sideChoice)
        self.canvas.pack()

        photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
        self.canvas.create_image(0, 0, image=photo, anchor=NW)

        self.B = Button(self.windowMaster, text="Back", command=lambda: [self.B.destroy(
        ), self.canvas.pack_forget(), self.caller.setUp()])
        self.B.pack()

        self.windowMaster.mainloop()

    def sideChoice(self, event):
        self.canvas.pack_forget()
        self.B.destroy()
        thirdHeight = self.height / 3
        twoThirdHeight = thirdHeight * 2
        imgName = 'Images//' + self.mapName + '.png'
        imgPath = rh.get_resource_path(imgName)

        if 0 <= event.y <= thirdHeight:
            self.windowMaster.title(self.mapName + ' Attacker')

            self.attackerLoc(imgPath)

        elif thirdHeight < event.y <= twoThirdHeight:
            self.windowMaster.title(self.mapName + ' Both')

            self.bothLoc(imgPath)

        elif twoThirdHeight < event.y <= self.height:
            self.windowMaster.title(self.mapName + ' Defedender')

            self.defenderLoc(imgPath)

    def attackerLoc(self, imgName):
        imgPath = rh.get_resource_path(imgName)

        url = 'https://valmap.s3.amazonaws.com/' + self.mapName + '.png'

        with urllib.request.urlopen(url) as response, open(imgPath, 'wb') as out_file:
            data = response.read()
            out_file.write(data)

        fileName = 'Locations\\' + self.agentName + self.mapName + 'Attacker.csv'
        filePath = rh.get_resource_path(fileName)

        url = 'https://valmap.s3.amazonaws.com/' + self.agentName + \
            '/' + self.agentName + self.mapName + 'Attacker.csv'

        with urllib.request.urlopen(url) as response, open(filePath, 'wb') as out_file:
            data = response.read()
            out_file.write(data)

        self.locs = np.genfromtxt(filePath, delimiter='|', dtype='S400')
        self.locCount = self.locs.shape[0]

        cv_img = cvtColor(imread(imgPath), COLOR_BGR2RGB)

        height, width, ne_channels = cv_img.shape

        canvas = Canvas(self.windowMaster, width=width, height=height)
        canvas.bind("<Button 1>", self.posCheck)
        canvas.pack()

        photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
        canvas.create_image(0, 0, image=photo, anchor=NW)

        for x in range(0, self.locCount):
            if (int(self.locs[x, 0]) % 2) == 0:
                canvas.create_rectangle(int(self.locs[x, 1]), int(self.locs[x, 2]), (int(
                    self.locs[x, 1])+12), (int(self.locs[x, 2])+12), fill='blue')
            else:
                canvas.create_rectangle(int(self.locs[x, 1]), int(self.locs[x, 2]), (int(
                    self.locs[x, 1])+12), (int(self.locs[x, 2])+12), fill='red')

        B = Button(self.windowMaster, text="Back", command=lambda: [B.destroy(
        ), canvas.pack_forget(), self.setUp()])
        B.pack()

        self.windowMaster.mainloop()

    def bothLoc(self, imgName):
        imgPath = rh.get_resource_path(imgName)
        url = 'https://valmap.s3.amazonaws.com/' + self.mapName + '.png'

        with urllib.request.urlopen(url) as response, open(imgPath, 'wb') as out_file:
            data = response.read()
            out_file.write(data)

        fileName = 'Locations\\' + self.agentName + self.mapName + 'Attacker.csv'
        filePath = rh.get_resource_path(fileName)

        url = 'https://valmap.s3.amazonaws.com/' + self.agentName + \
            '/' + self.agentName + self.mapName + 'Attacker.csv'

        with urllib.request.urlopen(url) as response, open(filePath, 'wb') as out_file:
            data = response.read()
            out_file.write(data)

        self.locs = np.genfromtxt(filePath, delimiter='|', dtype='S400')
        self.locCount = self.locs.shape[0]

        fileName = 'Locations\\' + self.agentName + self.mapName + 'Defender.csv'
        filePath = rh.get_resource_path(fileName)
        url = 'https://valmap.s3.amazonaws.com/' + self.agentName + \
            '/' + self.agentName + self.mapName + 'Defender.csv'

        with urllib.request.urlopen(url) as response, open(filePath, 'wb') as out_file:
            data = response.read()
            out_file.write(data)

        self.locs2 = np.genfromtxt(filePath, delimiter='|', dtype='S400')
        self.locCount2 = self.locs2.shape[0]

        cv_img = cvtColor(imread(imgPath), COLOR_BGR2RGB)

        height, width, ne_channels = cv_img.shape

        canvas = Canvas(self.windowMaster, width=width, height=height)
        canvas.bind("<Button 1>", self.posCheckBoth)
        canvas.pack()

        photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
        canvas.create_image(0, 0, image=photo, anchor=NW)

        for x in range(0, self.locCount):
            if (int(self.locs[x, 0]) % 2) == 0:
                canvas.create_rectangle(int(self.locs[x, 1]), int(self.locs[x, 2]), (int(
                    self.locs[x, 1])+12), (int(self.locs[x, 2])+12), fill='blue')
            else:
                canvas.create_rectangle(int(self.locs[x, 1]), int(self.locs[x, 2]), (int(
                    self.locs[x, 1])+12), (int(self.locs[x, 2])+12), fill='red')
        for x in range(0, self.locCount2):
            if (int(self.locs2[x, 0]) % 2) == 0:
                canvas.create_rectangle(int(self.locs2[x, 1]), int(self.locs2[x, 2]), (int(
                    self.locs2[x, 1])+12), (int(self.locs2[x, 2])+12), fill='blue')
            else:
                canvas.create_rectangle(int(self.locs2[x, 1]), int(self.locs2[x, 2]), (int(
                    self.locs2[x, 1])+12), (int(self.locs2[x, 2])+12), fill='red')

        B = Button(self.windowMaster, text="Back", command=lambda: [B.destroy(
        ), canvas.pack_forget(), self.setUp()])
        B.pack()

        self.windowMaster.mainloop()

    def defenderLoc(self, imgName):
        imgPath = rh.get_resource_path(imgName)
        url = 'https://valmap.s3.amazonaws.com/' + self.mapName + '.png'

        with urllib.request.urlopen(url) as response, open(imgPath, 'wb') as out_file:
            data = response.read()
            out_file.write(data)

        fileName = 'Locations\\' + self.agentName + self.mapName + 'Defender.csv'
        filePath = rh.get_resource_path(fileName)

        url = 'https://valmap.s3.amazonaws.com/' + self.agentName + \
            '/' + self.agentName + self.mapName + 'Defender.csv'

        with urllib.request.urlopen(url) as response, open(filePath, 'wb') as out_file:
            data = response.read()
            out_file.write(data)

        self.locs = np.genfromtxt(filePath, delimiter='|', dtype='S400')
        self.locCount = self.locs.shape[0]

        cv_img = cvtColor(imread(imgPath), COLOR_BGR2RGB)

        height, width, ne_channels = cv_img.shape

        canvas = Canvas(self.windowMaster, width=width, height=height)
        canvas.bind("<Button 1>", self.posCheck)
        canvas.pack()

        photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
        canvas.create_image(0, 0, image=photo, anchor=NW)

        for x in range(0, self.locCount):
            if (int(self.locs[x, 0]) % 2) == 0:
                canvas.create_rectangle(int(self.locs[x, 1]), int(self.locs[x, 2]), (int(
                    self.locs[x, 1])+12), (int(self.locs[x, 2])+12), fill='blue')
            else:
                canvas.create_rectangle(int(self.locs[x, 1]), int(self.locs[x, 2]), (int(
                    self.locs[x, 1])+12), (int(self.locs[x, 2])+12), fill='red')

        B = Button(self.windowMaster, text="Back", command=lambda: [B.destroy(
        ), canvas.pack_forget(), self.setUp()])
        B.pack()

        self.windowMaster.mainloop()

    def posCheck(self, event):
        print(str(event.x) + ', ' + str(event.y))
        for x in range(0, self.locCount):
            if int(self.locs[x, 1]) < event.x < (int(self.locs[x, 1]) + 12):
                if int(self.locs[x, 2]) < event.y < (int(self.locs[x, 2]) + 12):
                    locWindow = Toplevel(self.windowMaster)
                    locWindow.title(str(int(self.locs[x, 0])))

                    locMessage = str(self.locs[x, 3])[1:]
                    message = Text(locWindow, height=6, width=75, wrap=WORD)
                    message.insert(INSERT, locMessage)
                    message.pack()

                    picName = 'LocationImages\\' + self.agentName + \
                        self.mapName + str(int(self.locs[x, 0])) + '.png'
                    picPath = rh.get_resource_path(picName)
                    url = 'https://valmap.s3.amazonaws.com/' + self.agentName + '/' + \
                        self.agentName + self.mapName + \
                        str(int(self.locs[x, 0])) + '.png'

                    with urllib.request.urlopen(url) as response, open(picPath, 'wb') as out_file:
                        data = response.read()
                        out_file.write(data)

                    cv_img = cvtColor(imread(picPath), COLOR_BGR2RGB)
                    height, width, ne_channels = cv_img.shape

                    canvas = Canvas(locWindow, width=width, height=height)
                    canvas.pack()

                    photo = PIL.ImageTk.PhotoImage(
                        image=PIL.Image.fromarray(cv_img))
                    canvas.create_image(0, 0, image=photo, anchor=NW)
                    self.windowMaster.mainloop()

    def posCheckBoth(self, event):
        print(str(event.x) + ', ' + str(event.y))
        for x in range(0, self.locCount):
            if int(self.locs[x, 1]) < event.x < (int(self.locs[x, 1]) + 12):
                if int(self.locs[x, 2]) < event.y < (int(self.locs[x, 2]) + 12):
                    locWindow = Toplevel(self.windowMaster)
                    locWindow.title(str(int(self.locs[x, 0])))

                    locMessage = str(self.locs[x, 3])[1:]
                    message = Text(locWindow, height=6, width=75, wrap=WORD)
                    message.insert(INSERT, locMessage)
                    message.pack()

                    picName = 'LocationImages\\' + self.agentName + \
                        self.mapName + str(int(self.locs[x, 0])) + '.png'
                    picPath = rh.get_resource_path(picName)
                    url = 'https://valmap.s3.amazonaws.com/' + self.agentName + '/' + \
                        self.agentName + self.mapName + \
                        str(int(self.locs[x, 0])) + '.png'

                    with urllib.request.urlopen(url) as response, open(picPath, 'wb') as out_file:
                        data = response.read()
                        out_file.write(data)

                    cv_img = cvtColor(imread(picPath), COLOR_BGR2RGB)
                    height, width, ne_channels = cv_img.shape

                    canvas = Canvas(locWindow, width=width, height=height)
                    canvas.pack()

                    photo = PIL.ImageTk.PhotoImage(
                        image=PIL.Image.fromarray(cv_img))
                    canvas.create_image(0, 0, image=photo, anchor=NW)
                    self.windowMaster.mainloop()

        for x in range(0, self.locCount2):
            if int(self.locs2[x, 1]) < event.x < (int(self.locs2[x, 1]) + 12):
                if int(self.locs2[x, 2]) < event.y < (int(self.locs2[x, 2]) + 12):
                    locWindow = Toplevel(self.windowMaster)
                    locWindow.title(str(int(self.locs2[x, 0])))

                    locMessage = str(self.locs2[x, 3])[1:]
                    message = Text(locWindow, height=6, width=75, wrap=WORD)
                    message.insert(INSERT, locMessage)
                    message.pack()

                    picName = 'LocationImages\\' + self.agentName + \
                        self.mapName + str(int(self.locs2[x, 0])) + '.png'
                    picPath = rh.get_resource_path(picName)
                    url = 'https://valmap.s3.amazonaws.com/' + self.agentName + '/' + \
                        self.agentName + self.mapName + \
                        str(int(self.locs2[x, 0])) + '.png'

                    with urllib.request.urlopen(url) as response, open(picPath, 'wb') as out_file:
                        data = response.read()
                        out_file.write(data)

                    cv_img = cvtColor(imread(picPath), COLOR_BGR2RGB)
                    height, width, ne_channels = cv_img.shape

                    canvas = Canvas(locWindow, width=width, height=height)
                    canvas.pack()

                    photo = PIL.ImageTk.PhotoImage(
                        image=PIL.Image.fromarray(cv_img))
                    canvas.create_image(0, 0, image=photo, anchor=NW)
                    self.windowMaster.mainloop()
