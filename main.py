from BackgroundSlider import *
from user_imgs import *


a = BackgroundSlider(images=user_data['images'], changeInterval=user_data['interval'], currentIndex=user_data['current'])
a.insertImage("Desktop", 3)

print(a['images'])
print(a.images)

a.execute()

#print(a.attributes())
#print(a.methods())
