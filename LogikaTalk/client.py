import socket
import threading
SERVER_NAME ='5.tcp.eu.ngrok.io'
PORT = 18507
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((SERVER_NAME,PORT))
name = input("ім'я")
client.send(name.encode())

def sent_text():
    while True:
        text = input()
        if text == "exit":
            client.close()
            break
        client.send(text.encode())

threading.Thread(target=sent_text).start()

while True:
    try:
        text = client.recv(1024).decode().strip()
        if text:
            print(text)
    except:
        break