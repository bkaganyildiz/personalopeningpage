import os
import re
import sys


class Application(object):
    componentDir = "./Components"

    def __init__(self):
        self.components = []

    def available(self):
        cont = os.listdir(Application.componentDir)

        #regexm = re.compile("^(?!Component.py)(.*\.py)$")
        #cont = list( filter(regexm.match, cont))

        for path in cont:
            if path.endswith(".py") and (path != "Component.py"):
                self.components.append(path[:-3])

    def loaded(self):
        loaded = {}
        print(sys.modules)
        for component in self.components:
            if component in sys.modules:
                print("hey")
                loaded[component] = getattr(sys.modules[__name__], component)

    def load(self):
        pass

    def loadDesign(self, path):
        pass

    def saveDesign(self, path):
        pass

    def addInstance(self, componentname, x, y):
        pass

    def instances(self):
        pass

    def removeInstance(self):
        pass

    def callMethod(self, id, methodname, params):
        pass

    def execute(self):
        pass
