import socket
import pyautogui
import cv2
import numpy as np
import PIL

server_ip = "127.0.0.1"
server_portTL = 1000
server_portBL = 2000

server_portTR = 3000
server_portBR = 4000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

cap = cv2.VideoCapture(0)

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (768, 432))

    h, w, channels = frame.shape



    Lframe = frame[0:h, 0:int(w/2)]
    Rframe = frame[0:h, int(w/2):w]

    TLframe = Lframe[0:int(h/2), 0:int(w/2)]
    BLframe = Lframe[int(h/2):h, 0:int(w/2)]

    TRframe = Rframe[0:int(h/2), 0:int(w/2)]
    BRframe = Rframe[int(h/2):h, 0:int(w/2)]


    _, encoded_TRframe = cv2.imencode(".jpg", TRframe)
    _, encoded_BRframe = cv2.imencode(".jpg", BRframe)

    _, encoded_TLframe = cv2.imencode(".jpg", TLframe)
    _, encoded_BLframe = cv2.imencode(".jpg", BLframe)

    print("top left: "+str(len(encoded_TLframe))+", bottom left:"+str(len(encoded_BLframe))+", top right: "+str(len(encoded_TRframe))+", bottom right: "+str(len(encoded_BRframe)))
    
    if len(encoded_TLframe) <= 65507 and len(encoded_BLframe) <= 65507 and len(encoded_TRframe) <= 65507 and len(encoded_BRframe) <= 65507:
        client_socket.sendto(encoded_TLframe, (server_ip, server_portTL))
        client_socket.sendto(encoded_BLframe, (server_ip, server_portBL))

        client_socket.sendto(encoded_TRframe, (server_ip, server_portTR))
        client_socket.sendto(encoded_BRframe, (server_ip, server_portBR))



    else:
        print("Frame(s) too large, skipping")


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()

cap.release()