from gpiozero import Button
import time

button = Button(12)

while True:
    if button.is_pressed:
        print(time.time())
        