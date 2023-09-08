from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics.texture import Texture
from kivy.core.image import Image as CoreImage
import math

import socket
import selectors
import threading

Builder.load_file('dialbox.kv')


class DialBox(BoxLayout):

    manager = ObjectProperty(None)
    dial_image = ObjectProperty(None)
    host = '0.0.0.0'
    port = 65003
    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sel = selectors.DefaultSelector()
    stop_flag = False
    conn = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.listen_thread()

    def __accept_wrapper(self,sock):
        # accept new connections
        self.conn, addr = sock.accept()
        self.cam_addr = addr[0]
        print ('accepted connection from ', addr)
        self.conn.setblocking(False)
        #events = selectors.EVENT_READ
        #self.sel.register(conn,events, data = addr)
        self.status = 'Connected'
        print (self.conn)

    def listen_thread(self):
    
        #if not (self.t_listen.is_alive()):
        self.t_listen = threading.Thread(target = self.__listen)
        self.t_listen.daemon = True
        self.t_listen.start()
        print(str(self.t_listen.is_alive()))

    def __listen(self):
        self.lsock.bind((self.host,self.port))
        self.lsock.listen()
        print('listening on, ', (self.host,self.port))
        self.lsock.setblocking(False)
        self.sel.register(self.lsock, selectors.EVENT_READ, data = None)
        while not self.stop_flag:
            events = self.sel.select(timeout = None) #this blocks
            for key, _ in events:
                if key.data is None:
                    self.__accept_wrapper(key.fileobj)
                    

    def on_image_touch_move(self, *args):
        if args[0].collide_point(*args[1].pos):

            if args[0] == self.dial_image:
                #print (self.dial_image.center_x, self.dial_image.center_y)
                #print (*args[1].pos)
                x, y = args[1].pos
                delta_x = self.dial_image.center_x - x
                delta_y = self.dial_image.center_y - y
                theta = math.atan2(delta_y, delta_x) #*(180/math.pi)
                theta = int(theta*(180/math.pi) + 180)
                print (theta)
                self.dial_image.angle = theta

                # Send data to socket
                try:
                    self.conn.send(theta.to_bytes(2, 'big'))
                except Exception as e:
                    pass
                    # print (e)

    def on_image_release(self, *args):
        if args[0].collide_point(*args[1].pos):

            if args[0] == self.dial_image:
                # Close button pressed. Change button appearance
                print (self.dial_image.center_x, self.dial_image.center_y)
            
            