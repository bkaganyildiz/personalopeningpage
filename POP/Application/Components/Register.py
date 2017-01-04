from Components.Component import *
from dominate.tags import *
import json


class Register(Component):
    _description = "Register Page"
    _attributes = [
        ('firstName', 'string'),
        ('lastName', 'string'),
        ('mail', 'string'),
        ('password', 'string')
    ]
    _methods = [
        ('setFirstName', 'Set First Name'),
        ('setLastName', 'Set Last Name'),
        ('setMail', 'Set Mail Address'),
        ('setPassword', 'Set Password'),

        ('changeFirstName', 'Change First Name'),
        ('changeLastName', 'Change Last Name'),
        ('changeMail', 'Change Mail Address'),
        ('changePassword', 'Change Password'),
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

    def __str__(self):
        return self.description()

    def __init__(self, firstName="", lastName= "" , mail = "" , password=""):
        self.firstName = firstName
        self.lastName = lastName
        self.mail = mail
        self.password = password

    def setFirstName(self, firstName="") :
        self.firstName = firstName

    def changeFirstName(self, firstName="") :
        self.firstName = firstName

    def setLastName(self, lastName="") :
        self.lastName = lastName

    def changeLastName(self, lastName = "") :
        self.lastName = lastName

    def setMail(self, mail="") :
        self.mail = mail

    def changeMail(self, mail="") :
        self.mail = mail

    def setPassword(self, password="") :
        self.password = password

    def changePassword(self, password="") :
        self.password = password

    def register(self):
        try:
            users_file = open("users.txt", "r+")
            users_raw = users_file.read()
        except IOError:
            users_file = open("users.txt", "w")
            users_raw = json.dumps({'users':[]})

        users = json.loads(users_raw)

        for user in users['users']:
            if user['mail'] == self.mail:
                users_file.close()
                raise Exception('User exists')

        user = {
            'firstName' : self.firstName,
            'lastName' : self.lastName,
            'mail' : self.mail,
            'password' : self.password,
        }
        users['users'].append(user)

        users_file.write(json.dumps(users))
        users_file.close()

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
