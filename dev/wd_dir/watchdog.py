from dev.wd_dir import Client_handler
from dev.wd_dir import Subprocess_handler

a = Subprocess_handler.Subprocess()
a.start()
a.run_subprocess()

v = Client_handler.Client()
v.start()
v.open_connect()

while True:
    message = v.recive_message()
    if not message:
        break
    else:
        a.managing_the_subprocess(message)
