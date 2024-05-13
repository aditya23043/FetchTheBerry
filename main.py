from machine import Pin, ADC, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import utime
import random

xAxis = ADC(Pin(27))
yAxis = ADC(Pin(26))
button = Pin(22, Pin.IN, Pin.PULL_UP)

WIDTH = 128
HEIGHT = 64

i2c = I2C(0, scl = Pin(17), sda = Pin(16), freq = 1500000)
display = SSD1306_I2C(WIDTH, HEIGHT, i2c)

x = 64
y = 41
score = 0
time = 0

dot = [random.randint(2,126), random.randint(16,62)]
invert = 1

start_time = utime.time()

while True:
    
    display.fill(0)
    display.text(f"Score:{score}", 2, 3, 1)
    display.hline(0, 13, 128, 1)
    display.rect(dot[0]-1, dot[1]-1, 2, 2, 1)
    
    xVal = xAxis.read_u16()
    yVal = yAxis.read_u16()
    butVal = button.value()
    
    display.rect(x-2, y-2, 4, 4, 1)
    
    # Movement
    velocity = 1
    if xVal > 60000 and y < 62:
        y += velocity
    elif xVal < 400 and y > 15:
        y -= velocity
    if yVal > 60000 and x > 2:
        x -= velocity
    elif yVal < 400 and x < 126:
        x += velocity
        
    if x-4 < dot[0] and dot[0] < x+8 and y-4 < dot[1] and dot[1] < y+8:
        dot = [random.randint(2,126), random.randint(16,62)]
        score += 1

        
                        
    # Edge detection (overflow)
#     if x >= 130:
#         x = 2
#     elif x < 0:
#         x = 127
#     if y >= 66:
#         y = 2
#     elif y < 0:
#         y = 65
    
    # Reset
    if butVal == 0:
        x = 64
        y = 32
        score = 0
        dot = [random.randint(2,126), random.randint(16,62)]
        display.invert(invert)
        invert = 1 - invert
        utime.sleep(0.2)
        start_time = utime.time()x`

    display.text(f"Time:{int(utime.time() - start_time)}", 70, 3, 1)
#     display.vline(67, 0, 13, 4)
        
    display.show()
