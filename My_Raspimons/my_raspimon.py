from sense_hat import SenseHat
from time import sleep
import vision_lib

if __name__ == '__main__':
    
    sense = SenseHat()

    #add your colors
    r = (255, 0, 0) #red
    g = (0, 255, 0) #green
    b = (0, 0, 255) #blue
    k = (0, 0, 0)   #blank (black)
    w = (255, 255, 255) #white
    c = (0, 255, 255) #cyan
    y = (255, 255, 0) #yellow
    o = (255, 128, 0) #orange
    n = (255, 128, 128) #pink
    p = (128, 0, 128) #purple
    d = (255, 0, 128) #darkPink
    l = (128, 255, 128) #lightGreen

    #add your Raspimon lists, the first is an egg

    raspimon_egg =  [(128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (255, 255, 255), (255, 255, 255), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (255, 255, 255), (255, 255, 255), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128), (128, 0, 128)]

    open_eyes = [
    k, k, d, d, d, d, k, k,
    k, d, d, w, d, w, d, k,
    d, d, d, k, d, k, d, d,
    d, d, r, d, d, d, r, d,
    p, p, d, d, k, d, d, p,
    k, r, r, d, d, d, p, k,
    r, r, r, r, p, p, p, p,
    k, k, k, k, k, k, k, k 
    ] 
    
    closed_eyes =[
    k, k, d, d, d, d, k, k,
    k, d, d, d, d, d, d, k,
    d, d, d, d, d, d, d, d,
    d, d, r, d, d, d, r, d,
    p, p, d, d, k, d, d, p,
    k, r, r, d, d, d, p, k,
    r, r, r, r, p, p, p, p,
    k, k, k, k, k, k, k, k 
    ]

    hands_up = [
    d, k, d, d, d, d, k, d,
    d, d, d, w, d, w, d, d,
    p, d, d, k, d, k, d, p,
    k, d, r, d, d, d, r, k,
    k, p, d, d, k, d, d, k,
    k, r, r, d, d, d, p, k,
    r, r, r, r, p, p, p, p,
    k, k, k, k, k, k, k, k 
    ]

    tongue_out = [
    k, k, d, d, d, d, k, k,
    k, d, d, w, d, w, d, k,
    d, d, d, k, d, k, d, d,
    d, d, r, d, d, d, r, d,
    p, p, d, d, r, d, d, p,
    k, r, r, d, d, d, p, k,
    r, r, r, r, p, p, p, p,
    k, k, k, k, k, k, k, k 
    ]

    #set the egg
    sense.set_pixels(raspimon_egg)


    #define some functions. See sample_raspimon.py for examples.



    #add a while loop to keep your Raspimon running...
