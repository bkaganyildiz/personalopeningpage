import abc

class Component(object, metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def description(self):
        pass

    @abc.abstractclassmethod
    def attributes(self):
        pass

    @abc.abstractclassmethod
    def __getitem__(self, item):
        pass

    @abc.abstractclassmethod
    def __setitem__(self, key, value):
        pass

    @abc.abstractclassmethod
    def methods(self):
        pass

    @abc.abstractclassmethod
    def execute(self):
        pass
