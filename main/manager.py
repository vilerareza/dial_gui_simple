import socket
import selectors
import threading

from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from functools import partial

Builder.load_file('manager.kv')


class Manager(BoxLayout):

    image_box = ObjectProperty()

    conn = socket.socket()
    sel = selectors.DefaultSelector()
    stop_flag = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect_thread()

    def stop(self):
        pass

    def connect_thread(self):
        #if not (self.t_listen.is_alive()):
        self.t_connect = threading.Thread(target = self.__connect)
        self.t_connect.daemon = True
        self.t_connect.start()

    def __connect(self):
        # Initiate connection
        try:
            self.conn.connect(('127.0.0.1', 65003))
            self.conn.setblocking(False)
            print ('socket connected')
            self.sel.register(self.conn, selectors.EVENT_READ, data = None)
            while not self.stop_flag:
                events = self.sel.select(timeout = None) #this blocks
                for key, mask in events:
                    self.__service_connection(key, mask)

        except Exception as e:
            print (f'inSocket connection error: {e}')
            return False
        
    def __service_connection (self, key, mask):
        # Receive data
        sock = key.fileobj
        data = int.from_bytes(sock.recv(1024), 'big')
        Clock.schedule_once(partial(self.update_image, data), 0)

    def update_image(self, data=0, *args):
        if data >=0 and data <90:
            print ('1')
            self.image_box.source = 'images/1.png'
            #self.image_box.reload()
        elif data >=90 and data <180:
            print ('2')
            self.image_box.source = 'images/2.png'
        elif data >=180 and data <270:
            print ('3')
            self.image_box.source = 'images/3.png'
        elif data >=270 and data <360:
            print ('4')
            self.image_box.source = 'images/4.png'