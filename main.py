from Components.PageBackground import *
from user_imgs import *
from Application import Application

#a = PageBackground(imagePath=user_data['images'][1])
#print(a.execute())
"""
app = Application()
#print(app.available())
#print(app.loaded())
app.load("Register")
app.load("PageBackground")
app.load("PersonalInfo")
#print(app.loaded())
app.addInstance("PageBackground", 0, 0)
app.addInstance("Register", 1, 0)
app.addInstance("PersonalInfo", 2, 2)
#print(app.instances())
app.callMethod(1, "setBackground", "/home/metin/Desktop/script/bg_2.jpg")

app.callMethod(3, "addProfilePic", "https://media.licdn.com/mpr/mpr/shrinknp_200_200/AAEAAQAAAAAAAAS3AAAAJGU2MzI0ZjM5LTViMzUtNDJiOC05MWUzLWEyYWY5MDA4NjFlOA.jpg")
app.callMethod(3, "addName", "Memiş Gençol")
app.callMethod(3, "addBio", "Boş, Beleş Adamın Teki")
app.callMethod(3, "addConnections", ["f", "k"])

app.execute()
app.saveDesign("/home/metin/Desktop/xxx.txt")
"""

app2 = Application()
app2.loadDesign("/home/metin/Desktop/xxx.txt")
app2.execute()
#app.load("Register")
#app.addInstance("Register", 0, 1)

#print(app.loaded())



#a = BackgroundSlider(images=user_data['images'], changeInterval=user_data['interval'], currentIndex=user_data['current'])

#a.execute()

#print(a.attributes())
#print(a.methods())
