from pixi import *
import sprites


# make a bunch of bunnies
staticsprites = [sprites.CircleSprite(stage, randint(50,950),randint(50,600)) for x in range(200)]
sprites = [sprites.CircleSprite(stage, 50+(x*15)%100,(20+x*2)%30) for x in range(5)]


print("Hello, world")

s = input("Does this work?")
