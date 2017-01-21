import importlib
import json
import os
import imp
from dominate import document
from dominate.tags import *
import copy
import pickle


class Application(object):
    componentDir = "./Application/Components"
    instanceCounter = 1

    def __init__(self):
        self.loadedComponents = {}
        self.loaded_instances = {}
        self.maxRow = 1
        self.maxCol = 1

    def __getstate__(self):
        dump_loaded_instances = {}
        for key, value in self.loaded_instances.items():
            dump_loaded_instances[key] = (value[1], value[2], value[3], pickle.dumps(value[0]))

        dump_loadedComponents = []
        for key, value in self.loadedComponents.items():
            dump_loadedComponents.append(value.__name__)
        print dump_loadedComponents
        return (self.maxRow, self.maxCol, dump_loadedComponents, dump_loaded_instances)

    def __setstate__(self, state):
        self.maxRow, self.maxCol, dump_loadedComponents, dump_loaded_instances =  state

        self.loadedComponents = {}
        self.loaded_instances = {}
        for key in dump_loadedComponents:
            self.load(key)

        for key, instance in dump_loaded_instances.items():
            #self.addInstance(instance[0],instance[1],instance[2], id=key)

            self.loaded_instances[key] = (pickle.loads(instance[3]), instance[0],instance[1],instance[2])

    def available(self):
        components = []

        print(os.path.dirname(__file__))
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
        try:
            fp = open(path, "r")
        except:
            fp = path

        for line in fp:
            component = json.loads(line)
            self.load(component[0])
            self.addInstance(component[0], component[1], component[2])

    def saveDesign(self, path):
        with open(path, "w") as save_file:
            for value in self.instances().values():
                save_file.write(json.dumps(value) + "\n")



    def addInstance(self, componentname, x, y, id=None):
        if componentname in self.loadedComponents:
            if id:
                instanceId = id
            else:
                instanceId = str(Application.instanceCounter)
            Application.instanceCounter += 1

            c = getattr(self.loadedComponents[componentname], componentname)()
            for key, instance in (self.loaded_instances).items():
                print(self.loaded_instances)
                if x == instance[2] and y == instance[3]:
                    del self.loaded_instances[key]
                    break

            self.loaded_instances[instanceId] = (c, componentname, x, y)

            if x > self.maxRow - 1:
                self.maxRow = x + 1
            if y > self.maxCol - 1:
                self.maxCol = y + 1

            return instanceId
        raise Exception("Module Not Loaded")


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
        with open("POPapp/templates/index2.html", "w") as html_file:
            html_file.write("{%" + ' extends '+'"POPapp/templates/index.html" '+  "%}\n")
            html_file.write("{%" + " block content " + "%}\n")
            
            d = div()

            doms = []
            for i in range(0, self.maxRow):
                dd = []
                for j in range(0, self.maxCol):
                    dd.append(div(cls="grid"))
                doms.append(dd)


            for i in self.loaded_instances.keys():
                r = self.loaded_instances[i][2]
                c = self.loaded_instances[i][3]


                doms[r][c] = self.callMethod(i, "execute", None)
                doms[r][c]['class'] = "grid"


            for i in range(0, self.maxRow):
                for j in range(0, self.maxCol):
                    d.add(doms[i][j])
            html_file.write(d.render())
            html_file.write("\n{%" + " endblock content " + "%}")
            return (d.render())
