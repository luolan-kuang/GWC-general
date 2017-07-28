from PIL import Image



# RGB values for recoloring.
colorPallete1 = [(0, 51, 76), (217, 26, 33), (112, 150, 158), (252, 227, 166)]
colorPallete2 = [(135, 206, 250), (127, 255, 212), (230, 230, 250), (255, 250, 240)]
colorPallete3 = [(0, 0, 0), (119, 136, 153), (211, 211, 211), (255, 255, 255)]

# Import image.

my_image = Image.open("teacupPig.jpg") #change IMAGENAME to the path on your computer to the image you're using

image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.

image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.



recolored = [] #list that will hold the pixel data for the new image.



#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.


print("Choose a color pallete.")
print("Type '1' for color pallete 1, type '2' for color pallete 2, or type '3' for color pallete 3.")
user_input = input()
if user_input == "1":
    for pixel in image_list:
        if (pixel[0] + pixel[1] + pixel[2] < 182):
            pixel = colorPallete1[0]
            recolored.append(colorPallete1[0])
        elif (182 <= pixel[0] + pixel[1] + pixel[2] < 364):
            pixel = colorPallete1[1]
            recolored.append(colorPallete1[1])
        elif (364 <= pixel[0] + pixel[1] + pixel[2] < 546):
            pixel = colorPallete1[2]
            recolored.append(colorPallete1[2])
        elif (pixel[0] + pixel[1] + pixel[2] >= 546):
            pixel = colorPallete1[3]
            recolored.append(colorPallete1[3])
elif user_input == "2":
    for pixel in image_list:
        if (pixel[0] + pixel[1] + pixel[2] < 182):
            pixel = colorPallete2[0]
            recolored.append(colorPallete2[0])
        elif (182 <= pixel[0] + pixel[1] + pixel[2] < 364):
            pixel = colorPallete2[1]
            recolored.append(colorPallete2[1])
        elif (364 <= pixel[0] + pixel[1] + pixel[2] < 546):
            pixel = colorPallete2[2]
            recolored.append(colorPallete2[2])
        elif (pixel[0] + pixel[1] + pixel[2] >= 546):
            pixel = colorPallete2[3]
            recolored.append(colorPallete2[3])
elif user_input == "3":
    for pixel in image_list:
        if (pixel[0] + pixel[1] + pixel[2] < 182):
            pixel = colorPallete3[0]
            recolored.append(colorPallete3[0])
        elif (182 <= pixel[0] + pixel[1] + pixel[2] < 364):
            pixel = colorPallete3[1]
            recolored.append(colorPallete3[1])
        elif (364 <= pixel[0] + pixel[1] + pixel[2] < 546):
            pixel = colorPallete3[2]
            recolored.append(colorPallete3[2])
        elif (pixel[0] + pixel[1] + pixel[2] >= 546):
            pixel = colorPallete3[3]
            recolored.append(colorPallete3[3])
else:
    print("Invalid option")





# Create a new image using the recolored list. Display and save the image.

new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.

new_image.putdata(recolored) #Adds the data from the recolored list to the image.

new_image.show() #show the new image on the screen

new_image.save("recolored2.jpg", "jpeg") #save the new image as "recolored.jpg"
