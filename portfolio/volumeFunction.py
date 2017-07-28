#asking user imput
print("Hello, I'm going to calculate the volume of the three numbers you give me.")
length = int(input("What do you want the length to be?"))
width = int(input("What do you want the width to be?"))
height = int(input("What do you want the height to be?"))

#volume function
def volume(length, width, height):
    result = (length * width * height)
    return result

def main():
    print(volume(length, width, height))

main()
