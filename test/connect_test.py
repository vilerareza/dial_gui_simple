import socket

def connect():

    # Initiate connection
    try:
        s = socket.socket()
        s.settimeout(10)
        s.connect(('127.0.0.1', 65003))
        s.recv(1024)
        print ('inSocket connected')
        return True
    except Exception as e:
        print (f'inSocket connection error: {e}')
        return False

connect()