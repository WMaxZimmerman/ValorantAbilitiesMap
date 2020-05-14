from tkinter import Canvas, Toplevel, Text, NW, Button
from cv2 import cvtColor, imread, COLOR_BGR2RGB
import PIL.ImageTk
import urllib.request
import helpers.resource_helper as rh


class BaseMenu:
    global window

    def __init__(self, caller, window, options, typeName, targetFunc, targetParams):
        self.caller = caller
        self.window = window
        self.options = options
        self.maxY = 600
        self.yModifier = self.maxY / len(options)
        self.typeName = typeName
        self.targetFunc = targetFunc
        self.targetParams = targetParams
        self.setUp()

    def setUp(self):
        imgName = f'Images\\{self.typeName}.png'
        imgPath = rh.get_resource_path(imgName)

        url = f'https://valmap.s3.amazonaws.com/{self.typeName}.png'

        with urllib.request.urlopen(url) as response, open(imgPath, 'wb') as out_file:
            data = response.read()
            out_file.write(data)

        cv_img = cvtColor(imread(imgPath), COLOR_BGR2RGB)

        height, width, ne_channels = cv_img.shape

        self.canvas = Canvas(self.window, width=width, height=height)
        self.canvas.bind("<Button 1>", self.makeChoice)

        self.canvas.pack()

        photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
        self.canvas.create_image(0, 0, image=photo, anchor=NW)

        if (self.typeName == 'MapList'):
            self.B = Button(self.window, text="Back", command=lambda: [
                self.B.destroy(), self.canvas.pack_forget(), self.caller.setUp()
            ])
            self.B.pack()

        self.window.mainloop()

    def makeChoice(self, event):
        self.canvas.pack_forget()

        for i in range(len(self.options)):
            minRange = i * self.yModifier
            maxRange = minRange + self.yModifier

            if minRange <= event.y < maxRange:
                newWindow = self.targetFunc(
                    self, self.window, self.options[i], *self.targetParams
                )

        if event.y > self.maxY:
            updateWindow = Toplevel(self.window)
            message = Text(updateWindow, height=6, width=75, wrap=WORD)
            message.insert(
                INSERT, 'Please update your application to include new resources')
            message.pack()
