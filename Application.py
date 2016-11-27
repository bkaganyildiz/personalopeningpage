import importlib
import os
import imp
from dominate import document
from dominate.tags import *


class Application(object):
    componentDir = "./Components"
    instanceCounter = 1

    def __init__(self):
        self.loadedComponents = {}
        self.loaded_instances = {}
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
            self.loaded_instances[instanceId] = (c, componentname, x, y)

            if x > self.maxRow - 1:
                self.maxRow = x + 1
            if y > self.maxCol - 1:
                self.maxCol = y + 1

            return instanceId
        return 0


    def instances(self):
        ret = {}

        for key, value in self.loaded_instances.items():
            ret[key] = (value[1], value[2], value[3])

        return ret

    def removeInstance(self, id):
        del self.loaded_instances[id]

    def callMethod(self, id, methodname, *params):
        c = self.loaded_instances[id][0]
        method = getattr(c, methodname)

        if params == (None,):
            return method()
        else:
            return method(*params)

    def execute(self):
        with open("index.html", "w") as html_file:
            d = document()
            with d.head:
                style(".grid{{ width: {}%; height: {}%; float: left; }}".format(100 / self.maxRow,
                                                                                         100 / self.maxCol))

            _body = body()
            d.add(_body)


            for i in self.loaded_instances.keys():
                dom = self.callMethod(i, "execute", None)
                dom['class'] = "grid"
                _body.add(dom)

            html_file.write(d.render())
