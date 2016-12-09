from Components.Component import *
from dominate.tags import *


class PersonalInfo(Component):
    def description(self):
        return "A collection of personal informations like profile picture ,name , bio etc. "
    
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

#def execute(self):
#       print("Profile picture of the user :" + self.profilePic)
#       print("Name of the user :" + self.name )
#       print("Connections of the user : " )
#       for i in self.connections :
#           print (i)
#       print("Biography of the user : " + self.bio)
    
    def __str__(self):
        return self.description()
    
    def __init__(self, profilePic="", name= "" , connections = "" , bio=""):
        self.profilePic = profilePic
        self.name = name
        self.connections = connections
        self.bio = bio

    def addProfilePic(self, imageLocation=None):
        if imageLocation:
            self.profilePic = (imageLocation)

    def removeProfilePic(self, imageLocation=None):
        try :
            if self.profilePic :
                self.profilePic = None
        except AttributeError :
            print ("Profile Picture is not setted try set profile picture first then remove it")
    def changeProfilePic(self,imageLocation=None):
        try :
            if self.profilePic :
                self.profilePic = imageLocation
            else :
                self.profilePic = imageLocation
        except AttributeError :
            print ("Profile Picture is not setted try set profile picture first then change it")
    def addName(self, name=None):
        if name :
            self.name = (name)
    
    def removeName(self, name=None):
        try :
            if self.name :
                self.name = None
        except AttributeError :
            print ("Name is not setted try set name first then remove it")
    def changeName(self,name=None):
        try :
            if self.name :
                self.name = None
        except AttributeError :
            print ("Name is not setted try set name first then change it")
    def addBio(self, bio=None):
        if bio:
            self.bio = (bio)
    
    def removeBio(self, bio=None):
        try :
            if self.bio :
                self.bio = None
        except AttributeError :
            print ("Biography is not setted try set biography first then remove it")
    def changeBio(self,bio=None):
        try :
            if self.bio :
                self.bio = None
        except AttributeError :
            print ("Biography is not setted try set biography first then change it")
    def addConnections(self, connections=[]):
        if connections:
            self.connections = (connections)
    
    def removeConnection(self, connection):
        try :
            if connection in self.connections :
                self.connections.remove(connection)
        except AttributeError :
            print ("Connection is not on the connections list")
    def insertConnection(self,connection= None):
        self.connections.append(connection)
    def changeConnection(self,newConnection=None,oldConnection=None):
        try :
            if self.connections :
                for connection in self.connections:
                    if connection == oldConnection :
                        self.connections.remove(connection)
                        self.connections.append(newConnection)
        except AttributeError :
            print ("Connections are not setted try set connection first then change it")
    def execute(self):
        d = div(
            div(img(src=self.profilePic, alt=self.name)),
            div(div(div(h1(str(self.name)), p(str(self.bio))))),
            div(a("circlemail", href=self.connections)),
            p("Personal Info")
        )
        return d

        # If all else fails return to primitive methods
        return """
        <div class="grid">
          <div class="landing-pic-wrapper">
            <img src= "{}" alt= {} class="img-circle" id="landing-profile-pic">
          </div>
          <div class="col-sm-8">
            <div class="landing-wrapper-bio">
              <div class="landing-bio">
                <h1 class="me">{}</h1>
                <p>{}</p>
              </div>
              <div class="social">
                <a href={}><span class="symbol">circleemail</span></a>
              </div>
             </div>
          </div>
        </div>
        """.format(self.profilePic , self.name ,self.name,self.bio,self.connections[0])