from BackgroundSlider import *


a = BackgroundSlider(images=["1", "2", "3", "4", "5"], changeInterval=10)
a.insertImage("Desktop", 3)

print(a['images'])
print(a.images)

#print(a.attributes())
#print(a.methods())
