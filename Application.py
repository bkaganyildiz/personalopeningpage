import imp
import importlib
import os
import re
import sys


class Application(object):
    componentDir = "./Components"
    instanceCounter = 1

    def __init__(self):
        self.loadedComponents = {}
        self.instances = {}
        self.maxRow = 1
        self.maxCol = 1

    def available(self):
        components = []

        cont = os.listdir(Application.componentDir)
        for path in cont:
            if not path.startswith("__") and path.endswith(".py") and (path != "Component.py"):
                components.append(path[:-3])

        return components

    def loaded(self):
        loadedMods = {}
        for moduleName, module in self.loadedComponents.items():
            description = getattr(module, moduleName)().description()
            loadedMods[moduleName] = description

        return  loadedMods

    def load(self, moduleName):
        if moduleName not in self.loadedComponents:
            #module = importlib.import_module(moduleName, Application.componentDir + "/" + moduleName + ".py")
            module = imp.load_source(moduleName, Application.componentDir + "/" + moduleName + ".py")
            self.loadedComponents[moduleName] = module

    def loadDesign(self, path):
        pass

    def saveDesign(self, path):
        pass

    def addInstance(self, componentname, x, y):
        if componentname in self.loadedComponents:
            instanceId = Application.instanceCounter
            Application.instanceCounter += 1

            c = getattr(self.loadedComponents[componentname], componentname)()
            self.instances[instanceId] = (c, x, y)

            if x > self.maxRow - 1:
                self.maxRow = x + 1
            if y > self.maxCol - 1:
                self.maxCol = y + 1

            return instanceId
        return 0


    def instances(self):
        pass

    def removeInstance(self):
        pass

    def callMethod(self, id, methodname, params):
        pass

    def execute(self):
        pass
