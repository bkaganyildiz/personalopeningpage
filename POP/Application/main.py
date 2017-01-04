from Application import *

app = Application()

app.load('PageBackground')
app.load('Register')
app.load('PersonalInfo')

c1 = app.addInstance('PageBackground', 0, 0)
c2 = app.addInstance('Register', 0, 1)
c3 = app.addInstance('PersonalInfo', 0, 2)
c4 = app.addInstance('Register', 0, 0)

#cl1 = app.loaded_instances[c1][0]
cl2 = app.loaded_instances[c2][0]
cl3 = app.loaded_instances[c3][0]

cl3.addName('Metin Kapı')
cl3.addBio('Yeeeeeeeeeeees!')

app.execute()

"""
from Components.PageBackground import *
from user_imgs import *
from Application import Application

#a = PageBackground(imagePath=user_data['images'][1])
#print(a.execute())

app = Application()

#print(app.available())
#print(app.loaded())
app.load("Register")
app.load("PageBackground")
app.load("PersonalInfo")
#print(app.loaded())
id_page = app.addInstance("PageBackground", 0, 0)
id_page2 = app.addInstance("PageBackground", 0, 1)
id_reg = app.addInstance("Register", 1, 0)
id_per = app.addInstance("PersonalInfo", 2, 2)
#print(app.instances())
app.callMethod(id_page, "setBackground", user_data["images"][4])
app.callMethod(id_page2, "setBackground", user_data["images"][2])

app.callMethod(id_per, "addProfilePic", "https://media.licdn.com/mpr/mpr/shrinknp_200_200/AAEAAQAAAAAAAAS3AAAAJGU2MzI0ZjM5LTViMzUtNDJiOC05MWUzLWEyYWY5MDA4NjFlOA.jpg")
app.callMethod(id_per, "addName", "Memiş Gençol")
app.callMethod(id_per, "addBio", "Boş, Beleş Adamın Teki")
app.callMethod(id_per, "addConnections", ["f", "k"])

app.execute()
app.saveDesign("/home/metin/Desktop/xxx.txt")


#app2 = Application()
#app2.loadDesign("/home/metin/Desktop/xxx.txt")
#app2.execute()
#app.load("Register")
#app.addInstance("Register", 0, 1)

#print(app.loaded())



#a = BackgroundSlider(images=user_data['images'], changeInterval=user_data['interval'], currentIndex=user_data['current'])

#a.execute()

#print(a.attributes())
#print(a.methods())
"""