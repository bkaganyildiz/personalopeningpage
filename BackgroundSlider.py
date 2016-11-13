from Component import *


class BackgroundSlider(Component):
    def description(self):
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
        pass

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