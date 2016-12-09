#! /usr/bin/python
from Application import *
from socket import *
from threading import *

class Agent(Thread) :
    def __init__(self,sock,app) :
        Thread.__init__(self)
        self.sock = sock
        self._app = app
    def run(self) :
        l = self.sock.recv(1024)
        while l:
            c = l.decode('UTF-8').strip('\n').split(' ')
            if (c[0]=='available') :
                self.sock.send((str(self._app.available())+'\n').encode('UTF-8'))
            elif (c[0]=='loaded') :
                self.sock.send((str(self._app.loaded())+'\n').encode('UTF-8'))
            elif (c[0]=='load') :
                self.sock.send((str(self._app.load(c[1]))+'\n').encode('UTF-8'))
            elif (c[0]=='loadDesign') :
                self.sock.send((str(self._app.loadDesign(c[1]))+'\n').encode('UTF-8'))
            elif (c[0]=='saveDesign') :
                self.sock.send((str(self._app.saveDesign(c[1]))+'\n').encode('UTF-8'))
            elif (c[0]=='addInstance') :
                try :
                    self.sock.send((str(self._app.addInstance(c[1],int(c[2]),int(c[3])))+'\n').encode('UTF-8'))
                except FileNotFoundError :
                    self.sock.send('Component not Found : Error !'.encode('UTF-8'))
            elif (c[0]=='instances') :
                self.sock.send((str(self._app.instances())+'\n').encode('UTF-8'))
            elif (c[0]=='removeInstance') :
                self.sock.send((str(self._app.removeInstance(c[1]))+'\n').encode('UTF-8'))
            elif (c[0]=='callMethod') :
                self.sock.send((str(self._app.callMethod(c[1],c[2],[int(x) for x in c[3:]]))+'\n').encode('UTF-8'))
            else :
                self.sock.send((str(self._app.execute())+'\n').encode('UTF-8'))
            l = self.sock.recv(1024)
class CacheServ :
    def __init__(self,ipport) :
        self._l = Lock()
        self.sock = socket(AF_INET,SOCK_STREAM)
        self.sock.bind(('',ipport))
        self.sock.listen(1)
    def start(self) :
        conn , addr = self.sock.accept()
        while conn :
            app = Application()
            a = Agent(conn,app)
            a.start()
            conn , addr = self.sock.accept()
if (__name__ == '__main__') :
    serv = CacheServ(20002)
    serv.start()
