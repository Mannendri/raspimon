from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

#makeover time! Here is a Python list. It holds  collection of string values.

names = ["Codey" , "Galbert" , "Freedy", "Voltria" , "Kat-Kat"]

names.append("Lizardia")
names.append("Toenipper!")

sense.show_message(names[6])

#Colors:

r = (255, 0, 0 ) # RED color, stored in an another data structure called a tuple.
k = (0, 0, 0) # black means zero amounts of red, green and blue

#define another color. Use one letter variable names to make it easy later
b = (0,0,255)
g = (0,255,0)
w = (255,255,255)
o = (255,128,0)
y = (255,255,0)

raspimon = [
k, k, k, k, k, k, k, k,
k, r, r, r, r, r, r, k,
k, r, k, k, k, k, r, k,
k, r, b, k, b, k, r, k,
k, r, k, k, k, k, r, k,
k, r, r, r, r, r, r, k,
k, k, r, k, r, k, k, k,
k, k, r, k, r, k, k, k
]
 
sense.set_pixels(raspimon)

#add a one-pixel mouth
sense.set_pixel(3,4,r)
sleep(2)

pikachu = [
w, k, k, w, w, w, w, k,
w, w, y, o, w, w, w, o,
w, w, w, y, y, y, y, o,
o, o, w, y, k, y, y, k,
o, o, w, r, y, y, y, o,
w, o, w, y, o, o, o, w,
w, o, y, o, y, o, y, w,
w, w, y, o, o, o, o, w
]
sense.set_pixels(pikachu)
	
	
	
	
	
	
	
 


