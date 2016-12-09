from Components.Component import *
from dominate.tags import *


class Register(Component):
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

    def __str__(self):
        return self.description()
    
    def __init__(self, firstName=None, lastName= None , mail = None , password=None):
        self.firstName = firstName
        self.lastName = lastName
        self.mail = mail
        self.password = password
    
    def setFirstName(self,firstName=None) :
        self.firstName = firstName
    def changeFirstName(self,firstName=None) :
        self.firstName = firstName
    def setLastName(self,lastName=None) :
        self.lastName = lastName
    def changeLastName(self,lastName = None) :
        self.lastName = lastName
    def setMail(self,mail=None) :
        self.mail = mail
    def changeMail(self,mail=None) :
        self.mail = mail
    def setPassword(self,password=None) :
        self.password = password
    def changePassword(self,password=None) :
        self.password = password
    
    def execute(self):
        h = div(
            h1("Sign Up For Free"),
            div(label("First Name", span(), "*"), input(type=self.firstName, autocomplete="off")),
            div(label("Last Name", span(), "*"), input(type=self.lastName, autocomplete="off")),
            div(label("Email Address", span(), "*"), input(type=self.mail, autocomplete="off")),
            div(label("Set A Password", span(), "*"), input(type=self.password, autocomplete="off")),
            button("Get Started", type="Submit")
        )
        return h

        # If all else fails return to primitive methods
        return """
        <div class="grid">
          <h1>Sign Up For Free</h1>
          <div>
            <label>First Name
              <span></span>*
            </label>
            <input autocomplete="off" type="{}">
          </div>
          <div>
            <label>Last Name
              <span></span>*
            </label>
            <input autocomplete="off" type="{}">
          </div>
          <div>
            <label>Email Address
              <span></span>*
            </label>
            <input autocomplete="off" type="{}">
          </div>
          <div>
            <label>Set A Password
              <span></span>*
            </label>
            <input autocomplete="off" type="{}">
          </div>
          <button type="Submit">Get Started</button>
        </div>
        """.format(self.firstName , self.lastName ,self.mail,self.password)
