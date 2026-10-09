import socket
import time

from pynput.keyboard import Key, Controller

keyboard = Controller()
# Define the UDP IP address and port to listen on
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

negitveX = False
negitveY = False
negitveZ = False
prefame = 0
preX = 0
preY = 0
preZ = 0
print("starting in 5")
time.sleep(5)
print(f"Listening for UDP packets on {UDP_IP}:{UDP_PORT}")
while True:

    # Receive data from the socket
    data, addr = sock.recvfrom(1024)
    rot = (data.decode("utf-8"))
    rotX = int(round(float(rot.split("x", 2)[1])*60))
    rotY = int(round(float(rot.split("y", 2)[1]) * 57.25))
    rotZ = int(round(float(rot.split("z", 2)[1])*60))
    if prefame == 2:
        preX = rotX
        preY = rotY

        prefame = 0
    prefame += 1



    moveByX = rotX-preX
    moveByY = rotY-preY
    

    while moveByX > 0:
        keyboard.press("1")
        time.sleep(0.004)
        keyboard.release('1')

        moveByX -= 1
        print(str(moveByX))


    while moveByX < 0:
        keyboard.press("2")
        time.sleep(0.004)
        keyboard.release('2')

        moveByX += 1
        print(str(moveByX))




    while moveByY > 0:
        keyboard.press("3")
        time.sleep(0.004)
        keyboard.release('3')

        moveByY -= 1
        print(str(moveByY))


    while moveByY < 0:
        keyboard.press("4")
        time.sleep(0.004)
        keyboard.release('4')

        moveByY += 1
        print(str(moveByY))





    
