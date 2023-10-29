
# https://learn.adafruit.com/adafruit-circuit-playground-express/guided-tour
# https://docs.circuitpython.org/projects/circuitplayground/en/latest/api.html
# https://docs.circuitpython.org/en/latest/shared-bindings/pulseio/index.html
# https://github.com/adafruit/Adafruit_CircuitPython_IRRemote
# https://github.com/adafruit/Adafruit_CircuitPython_IRRemote/blob/main/adafruit_irremote.py
# https://learn.adafruit.com/infrared-ir-receive-transmit-circuit-playground-express-circuit-python?view=all
# https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/neopixels
# https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/play-file
# https://learn.adafruit.com/microcontroller-compatible-audio-file-conversion

import time
import board
import rainbowio
# import neopixel
import pulseio
from adafruit_circuitplayground import cp

ir_pulses = pulseio.PulseIn(board.IR_RX, maxlen=1000, idle_state=True)
cp.pixels.brightness = 0.3

def make_a_rainbow():
    for i in range(10):
        rc_index = (i * 256 // 10)
        cp.pixels[i] = rainbowio.colorwheel(rc_index & 255)
        time.sleep(0.1)
        cp.pixels.show()
    cp.play_file("arcade_magic_lo.wav")
    for i in range(10):
        cp.pixels[i] = (0, 0, 0)
        time.sleep(0.1)
        cp.pixels.show()

while True:
    if len(ir_pulses) > 0:
        ir_pulses.pause()
        # print(len(ir_pulses))
        # print(ir_pulses[0])

        make_a_rainbow()
        ir_pulses.clear()
        ir_pulses.resume()


# Write your code here :-)
