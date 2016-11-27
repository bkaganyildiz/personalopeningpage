from Components.PageBackground import *
from user_imgs import *
from Application import Application

a = PageBackground(imagePath=user_data['images'][1])
print(a.execute())

#app = Application()
#app.available()

#print(app.loaded())



#a = BackgroundSlider(images=user_data['images'], changeInterval=user_data['interval'], currentIndex=user_data['current'])

#a.execute()

#print(a.attributes())
#print(a.methods())
