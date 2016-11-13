from Component import *


class BackgroundSlider(Component):
    _vars = ["images"]
    def description(self):
        return "A collection of background images which changes in a set time"

    def __dir__(self):
        att = []

        for attribute in self._vars:
            att.append((attribute, type(attribute).__name__))

        return att

    def __getitem__(self, item):
        if item in self._vars:
            return getattr(self, item)
        raise AttributeError()

    def __setitem__(self, key, value):
        if key in self._vars:
            setattr(self, key, value)
        else:
            raise AttributeError()

    def methods(self):
        att = []

        for attribute in self.__dict__:
            if callable(attribute):
                att.append((attribute, type(attribute).__name__))

        return att

    def execute(self):
        pass

    def __str__(self):
        return self.description()

    def __init__(self, images = []):
        self.images = images


a = BackgroundSlider(images=["1", "2", "3", "4", "5"])


print(dir(a))

#print(a.__dir__())
#print(a.methods())
#print(a.__dict__)
