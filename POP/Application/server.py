#! /usr/bin/python
from Application import *
from socket import *
from threading import *
MSG_SUCCESSFUL = "OK \n".encode('UTF-8')
MSG_FAIL = "FAIL \n".encode('UTF-8')
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
                try :
                    self.sock.send((str(self._app.available())+'\n').encode('UTF-8'))
                except :
                    self.sock.send(MSG_FAIL)
            elif (c[0]=='loaded') :
                try :
                    self.sock.send((str(self._app.loaded())+'\n').encode('UTF-8'))
                except :
                    self.sock.send(MSG_FAIL)
            elif (c[0]=='load') :
                try :
                    self._app.load(c[1])
                    self.sock.send(MSG_SUCCESSFUL)
                except:
                    self.sock.send(MSG_FAIL)
            elif (c[0]=='loadDesign') :
                try :
                    self._app.loadDesign(c[1])
                    self.sock.send(MSG_SUCCESSFUL)
                except:
                    self.sock.send(MSG_FAIL)
            elif (c[0]=='saveDesign') :
                try :
                    self._app.saveDesign(c[1])
                    self.sock.send(MSG_SUCCESSFUL)
                except:
                    self.sock.send(MSG_FAIL)
            elif (c[0]=='addInstance') :
                try :
                    self.sock.send((self._app.addInstance(c[1],int(c[2]),int(c[3])) + "\n").encode("UTF-8"))
                except:
                    self.sock.send(MSG_FAIL)
            elif (c[0]=='instances') :
                try :
                    self.sock.send((str(self._app.instances())+'\n').encode('UTF-8'))
                except :
                    self.sock.send(MSG_FAIL)
            elif (c[0]=='removeInstance') :
                try :
                    self._app.removeInstance(c[1])
                    self.sock.send(MSG_SUCCESSFUL)
                except:
                    self.sock.send(MSG_FAIL)
            elif (c[0]=='callMethod') :
                try :

                    returner = self._app.callMethod(c[1],c[2],*c[3:])
                    if(returner == None) :
                        self.sock.send(MSG_SUCCESSFUL)
                    else :
                        self.sock.send((returner+'\n').encode('UTF-8'))
                except :
                    self.sock.send(MSG_FAIL)
            elif (c[0] == 'execute') :
                self.sock.send((str(self._app.execute())+'\n').encode('UTF-8'))
            else:
                self.sock.send(MSG_FAIL)
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
    serv = CacheServ(20000)
    serv.start()
