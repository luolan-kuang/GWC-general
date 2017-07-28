

from random import *



#Create the list of words you want to choose from.
five_syllable= ["Trees are growing tall", "People are singing", "Animals are cool", "Strawberries are fun"]
seven_syllable = ["Sitting in the water stream", "Gazing at the starry night", "Humming with the soft blue grass", "The silence is beautiful"]



#Generates a random integer.
x = randint(0, len(five_syllable)-1)
y = randint(0, len(seven_syllable)-1)

print(five_syllable[x])
print(seven_syllable[y])
print(five_syllable[x])
