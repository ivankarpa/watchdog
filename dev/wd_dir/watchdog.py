import client_handler
import subprocess_handler
import time

s = subprocess_handler.Subprocess()
s.start()

c = client_handler.Client()
c.start()
c.open_connect()




while True:
    message = c.receive_message()

    if message == "disconnect":
        s.managing_the_subprocess('kill')
        break
    else:
        s.managing_the_subprocess(message)

    if not c.check_connection():
        c.open_connect()
