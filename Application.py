import imp
import os
import re
import sys


class Application(object):
    componentDir = "./Components"

    def __init__(self):
        self.loadedComps = {}
        self.instances = {}

    def available(self):
        components = []

        cont = os.listdir(Application.componentDir)
        for path in cont:
            if not path.startswith("__") and path.endswith(".py") and (path != "Component.py"):
                components.append(path[:-3])

        return components

    def loaded(self):
        loaded = {}
        print(sys.modules)
        for component in self.components:
            if component in sys.modules:
                print("hey")
                loaded[component] = getattr(sys.modules[__name__], component)

    def load(self, moduleName):
        if moduleName not in self.loadedComps:
            module = imp.load_source(moduleName, Application.componentDir + "/" + moduleName + ".py")
            self.loadedComps[moduleName] = module

    def loadDesign(self, path):
        pass

    def saveDesign(self, path):
        pass

    def addInstance(self, componentname, x, y):
        if componentname in self.loadedComps:
            c = getattr(self.loadedComps[componentname], componentname)
            c()

    def instances(self):
        pass

    def removeInstance(self):
        pass

    def callMethod(self, id, methodname, params):
        pass

    def execute(self):
        with open("index.html","w") as html_file :
            html_file.write("""
                <!DOCTYPE html>
                <html>
                <head>
                <title></title>
                <style>
                div { width: %f %; height:  %f %; float: left; }
                </style>
                </head>
                <body background= "#000000" style="-webkit-background-size: cover; -moz-background-size: cover; -o-background-size: cover; background-size: cover;">""" % 100/self.maxRow , 100/self.maxCol)
                <div style="background-color: #0000FF;">
                <img src="/home/metin/Desktop/script/bg_3.jpg">
                </div>
                <div style="background-color: #0000FF;">
                <img src="/home/metin/Desktop/script/bg_3.jpg">
                </div>
                <div style="background-color: #0000FF;">
                <img src="/home/metin/Desktop/script/bg_3.jpg">
                </div>
                
                </body>
                </html>
                """)
