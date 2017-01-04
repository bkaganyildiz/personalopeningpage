from dominate.tags import *


class PersonalInfo(object):
    _description = "A collection of personal information like profile picture, name, bio etc."
    _attributes = [
        ('profilePic', 'string'),
        ('name', 'string'),
        ('connections', 'list'),
        ('bio', 'string'),
    ]
    _methods = [
        ('addProfilePic', 'Set profile picture to a URL or path'),
        ('removeProfilePic', 'Remove current profile picture'),
        ('changeProfilePic', 'Change profile picture to another URL or path'),
        ('addName', 'Set profile name'),
        ('removeName', 'Remove current profile name'),
        ('changeName', 'Change profile name to another name'),
        ('addBio', 'Set profile biography'),
        ('removeBio', 'Remove profile biography'),
        ('changeBio', 'Update profile biography'),
        ('addConnections', 'Set connection links from a list'),
        ('removeConnection', 'Remove connection by name'),
        ('insertConnection', 'Insert new connection to the end of the connections list'),
        ('changeConnection', 'Update connection by name'),
    ]

    def description(self):
        return self._description

    def attributes(self):
        return self._attributes

    def __getitem__(self, item):
        for attribute in self._attributes:
            if attribute[0] == item:
                return getattr(self, item)

        raise AttributeError(self.__class__.__name__ + " object has no attribute '" + item + "'")

    def __setitem__(self, key, value):
        for attribute in self._attributes:
            if attribute[0] == key:
                setattr(self, key, value)
                return

        raise AttributeError(self.__class__.__name__ + " object has no attribute '" + key + "'")

    def methods(self):
        return self._methods


#def execute(self):
#       print("Profile picture of the user :" + self.profilePic)
#       print("Name of the user :" + self.name )
#       print("Connections of the user : " )
#       for i in self.connections :
#           print (i)
#       print("Biography of the user : " + self.bio)

    def __str__(self):
        return self.description()

    def __init__(self, profilePic="", name= "", connections=None, bio=""):
        self.profilePic = profilePic
        self.name = name
        if connections:
            self.connections = connections
        else:
            self.connections = []
        self.bio = bio

    def addProfilePic(self, imageLocation=None):
        if imageLocation:
            self.profilePic = imageLocation

    def removeProfilePic(self):
        try :
            if self.profilePic :
                self.profilePic = ""
        except AttributeError :
            print("Profile Picture is not set try set profile picture first then remove it")

    def changeProfilePic(self, imageLocation=None):
        try :
            self.profilePic = imageLocation
        except AttributeError :
            print ("Profile Picture is not set try set profile picture first then change it")

    def addName(self, name=None):
        if name :
            self.name = name

    def removeName(self):
        try :
            if self.name :
                self.name = ""
        except AttributeError :
            print ("Name is not set try set name first then remove it")

    def changeName(self, name=None):
        try :
            if self.name :
                self.name = name
        except AttributeError :
            print ("Name is not set try set name first then change it")

    def addBio(self, bio=None):
        if bio:
            self.bio = bio

    def removeBio(self):
        try :
            if self.bio :
                self.bio = ""
        except AttributeError :
            print ("Biography is not set try set biography first then remove it")

    def changeBio(self, bio=None):
        try :
            if self.bio :
                self.bio = bio
        except AttributeError :
            print ("Biography is not set try set biography first then change it")

    def addConnections(self, connections=None):
        if connections:
            self.connections = connections

    def removeConnection(self, connection):
        try :
            if connection in self.connections :
                self.connections.remove(connection)
        except AttributeError :
            print ("Connection is not in the connections list")

    def insertConnection(self, connection=None):
        if connection:
            self.connections.append(connection)

    def changeConnection(self, newConnection=None, oldConnection=None):
        try :
            if self.connections :
                for connection in self.connections:
                    if connection == oldConnection :
                        self.connections.remove(connection)
                        self.connections.append(newConnection)
        except AttributeError :
            print ("Connections are not set try set connection first then change it")

    def execute(self):
        d = div(
            div(img(src=self.profilePic, alt=self.name)),
            div(div(div(h1(str(self.name)), p(str(self.bio))))),
            div(a("circlemail", href=self.connections)),
            p("Personal Info")
        )
        return d
