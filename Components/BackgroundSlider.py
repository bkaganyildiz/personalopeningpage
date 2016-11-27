import threading
from time import sleep

from Components.Component import *


class BackgroundSlider(Component):
    def description():
        return "A collection of background images which changes in a set time"

    def attributes(self):
        att = []

        for attribute in dir(self):
            if not callable(getattr(self, attribute)):
                att.append((attribute, type(getattr(self, attribute)).__name__))

        return att

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def methods(self):
        att = []

        for attribute in dir(self):
            if callable(getattr(self, attribute)):
                att.append((attribute, type(getattr(self, attribute)).__name__))

        return att

    def execute(self):
        print("starting at index {} image will change in every {} second".format(self.currentIndex, self.changeInterval))

        slideThread = threading.Thread(target=self.slide)
        slideThread.start()
        slideThread.join()

    def slide(self):
        while(True):
            print("Current BG image is: {}".format(self.images[self.currentIndex]))
            self.currentIndex = (self.currentIndex + 1) % len(self.images)
            sleep(self.changeInterval)

    def __str__(self):
        return self.description()

    def __init__(self, images=None, changeInterval=0, currentIndex=0):
        if images:
            self.images = images
            self.currentIndex = currentIndex
            self.changeInterval = changeInterval

    def addImage(self, imageLocation=None):
        if imageLocation:
            self.images.append(imageLocation)

    def removeImage(self, imageLocation=None):
        if imageLocation in self.images:
            self.images.remove(imageLocation)

    def insertImage(self, imageLocation=None, position=0):
        if imageLocation:
            self.images.insert(position, imageLocation)

    def printHTML(self):
        return '<body background="{}" style="-webkit-background-size: cover;\
  -moz-background-size: cover;\
  -o-background-size: cover;\
  background-size: cover;">'.format(self.images[self.currentIndex])