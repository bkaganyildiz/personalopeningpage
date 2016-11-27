from Components.Component import *


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
        return """
                <div>
                <h1>Sign Up for Free</h1>
                <div>
                <div class="field-wrap">
                <label>
                First Name<span class="req">*</span>
                </label>
                <input type=%s required autocomplete="off"/>
                </div>
                <div class="field-wrap">
                <label>
                Last Name<span class="req">*</span>
                </label>
                <input type= %s required autocomplete="off"/>
                </div>
                </div>
                <div>
                <div class="field-wrap">
                <label>
                Email Address<span class="req">*</span>
                </label>
                <input type= %s required autocomplete="off"/>
                </div>
                <div class="field-wrap">
                <label>
                Set A Password<span class="req">*</span>
                </label>
                <input type= %s required autocomplete="off"/>
                </div>
                </div>
                <div>
                <button type="submit" class="button button-block"/>Get Started</button>
                </div>
                </form>

                </div>
                """ % (self.firstName , self.lastName ,self.mail,self.password)
