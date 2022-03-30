import math

height = int(input('Enter Height: '))
radius = int(input('Enter Radius: '))

def volume(h, r):
    volume = math.pi * r**2 * h
    return volume
    
print(volume(height,radius))
