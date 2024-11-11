import pygame
import sys

# Load in the image
sourceImage = pygame.image.load(sys.argv[1])
# Determine how large the image is
(w,h) = sourceImage.get_size()

# Create a window of the correct size
Window = pygame.display.set_mode((w,h))
# Display the original image on the screen
Window.blit(sourceImage, (0,0))
pygame.display.update()

# Initalize other variables the image to be edited
# updated keeps track of if a new box needs to be drawn (true when now box needs to be drawn)
updated = True
# start keeps track of when a new box is being created by the user (true when a new box is getting created)
start = True


# Allow the user to edit the image until they close the tab
exit_flag = False
while not exit_flag:

    # record the mouse position if the user is clicking on the mouse
    if pygame.mouse.get_pressed()[0]:
        updated = False
        #x and y is position at any given time, becomes the final position
        (x,y) = pygame.mouse.get_pos()
        #save the value that the user started at if it is 
        if start:
            x1 = x
            y1 = y

        start = False

    # draw the image if it has not been updated in the previous iteration of the loop
    if (not pygame.mouse.get_pressed()[0]) and (not updated):
        
        # Determine the left and right x-cordinate of the box that the user created
        if x1 < x:
            leftX = x1
            rightX = x
        else:
            leftX = x
            rightX = x1
        
        # Determine the top and bottom y-cordinate of the box that the user created
        if y1 < y:
            topY = y1
            bottomY = y
        else:
            topY = y
            bottomY = y1

        #Draw each column of the negative for the box
        for i in range (leftX, rightX, 1):
            #Draw pixel in each row of the negative for the box
            for j in range (topY, bottomY, 1):
                #Find the original colours
                (r, g, b, _) = Window.get_at((i, j))

               # Find the negative of the colours for the pixel and update the pixel
                r = 255 - r
                g = 255 - g
                b = 255 - b
                Window.set_at((i,j), (r, g, b))
        # Let the computer know that the box is complete and should not be drawn if during the next irriteration
        updated = True
        # Let the computer know that the next box is new
        start = True
    
    pygame.display.update()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit_flag = True