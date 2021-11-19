from machine import Pin
import neopixel

n = 12 # Antallet af pixels, som er 12 Pixels i vores LED ring)
p = 15 # Pin

np = neopixel.NeoPixel(Pin(p), n)

def set_color(r, g, b):
    for i in range(n):
        np[i] = (r, g, b)
    np.write()
    
