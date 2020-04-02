
import pygame
import random as rd

# iniitializing pygame
pygame.init()

# setting up colors for background and othe objects
black = (0, 0, 0)
white = (255, 255, 255)

# define the pygame window size
screen = pygame.display.set_mode([500, 500])

# set screen background color
screen.fill(black)

# push changes to the display
pygame.display.update()

# counter to monitor screen status
running = True

# Randomly set the no of stars present on screen that are used to draw line
star_count = rd.randrange(50, 70)

for i in range(10):

    screen.fill(black)
    # to make screen blank after each round

    # list to store randomly geneated x and y position of each star
    rdm_xpos_list = []
    rdm_ypos_list = []

    for i in range(star_count):
        
        # for each star generate a random x&y pos
        rdm_xpos = rd.randrange(0, 500)
        rdm_ypos = rd.randrange(0, 500)

        # store star position in list
        rdm_xpos_list.append(rdm_xpos)
        rdm_ypos_list.append(rdm_ypos)

        # draw star to the screen
        pygame.draw.circle(screen, white,
                            (rdm_xpos, rdm_ypos), 1, 1)
    # push changes to the screen
    pygame.display.update()

    # wait for some time 
    pygame.time.wait(250)

    # set numnber of static stars i.e to make sure universe doen't appear to be 
    # devoid of stars when we warp
    rand_star_count2 = rd.randrange(30,50)

    # draw static stars to the screen
    for q in range(rand_star_count2):
        rdm_xpos = rd.randrange(0, 500)
        rdm_ypos = rd.randrange(0, 500)
        pygame.draw.circle(screen, white,
                           (rdm_xpos, rdm_ypos), 1, 1)
    
    # push changes to the screen
    pygame.display.update()

    # randomly geneate a number to set counter for specifying line direction 
    # on the screen with respect to X-pos of the star
    randx_counter = rd.randrange(200, 270)

    # draw lines from star positions to give warp effect
    for i in range(star_count):
        if(rdm_xpos_list[i] <= randx_counter):
            pygame.draw.line(screen, white, (rdm_xpos_list[i], rdm_ypos_list[i]), (
                rdm_xpos_list[i]-40, rdm_ypos_list[i]+55), 6)
        else:
            pygame.draw.line(screen, white, (rdm_xpos_list[i], rdm_ypos_list[i]), (
                rdm_xpos_list[i]+40, rdm_ypos_list[i]+55), 6)
        pygame.time.wait(2)
        pygame.display.update()
    
# monitor window status is window open or has been closed 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#stop the simulation
pygame.quit()

# references - 
# https://thecodingtrain.com/CodingChallenges/001-starfield.html
# https://editor.p5js.org/codingtrain/sketches/1wLHIck3T
# https://realpython.com/pygame-a-primer/
# https://sites.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/index.html
# https://www.youtube.com/watch?v=SmxMw37pqJ8
# http://www.petercollingridge.co.uk/tutorials/3d/pygame/
# https://stackoverflow.com/
# https://pythonprogramming.net/opengl-rotating-cube-example-pyopengl-tutorial/
