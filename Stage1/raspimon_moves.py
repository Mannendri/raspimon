from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

#colors
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
sense.set_pixels(open_eyes)

#Create animation below
sleep(.5)
sense.flip_h()
sleep(.5)
sense.flip_h()
sleep(.5)
sense.flip_h()
sleep(1)
sense.flip_v()
sleep(.5)
sense.flip_v()
sleep(.5)
sense.set_pixels(open_eyes)
sleep(.9)
sense.set_pixels(closed_eyes)
sleep(.2)
sense.set_pixels(open_eyes)
sleep(.9)
sleep(.9)
sense.set_pixels(closed_eyes)
sleep(.2)
sense.set_pixels(open_eyes)
sleep(.9)
sense.set_pixels(hands_up)
sleep(1)
sense.set_pixels(tongue_out)
sleep(.5)
sense.set_pixels(open_eyes)


print('Done')

