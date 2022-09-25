import os.path
import numpy
import cv2
import pygame
import matplotlib.image as mpimg
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)



class UpdatedImage:
    def __init__( self, filename ):
        self.filename    = filename
        self.last_update = 0         # trigger initial load
        self.image       = None      # final surface
        self.reLoadImage()           # make sure we load once, first
    
    def drawAt( self, window, position ):
        """ Draw the image to the screen at the given position """
        window.blit( self.image, position )

    def reLoadImage( self ):
        """ Load in the image iff it has changed on disk """
        current_file_time = os.path.getmtime( self.filename )
        if ( current_file_time > self.last_update ):
            self.last_update = current_file_time
            img_crop = mpimg.imread( self.filename )
            x = numpy.arange(10)
            y = numpy.arange(20)
            X, Y = numpy.meshgrid(x, y)
            img_crop_re = cv2.resize(img_crop, dsize=(200,200), interpolation=cv2.INTER_CUBIC)
            img_crop_ro = cv2.rotate(img_crop_re, cv2.ROTATE_90_COUNTERCLOCKWISE)
            img_crop_flip = cv2.flip(img_crop_ro,0)
            self.image = pygame.surfarray.make_surface(img_crop_flip)


if __name__ == "__main__":

    pygame.init()
    w = 1200
    h = 720
    screen = pygame.display.set_mode((w, h))
    crop_image = UpdatedImage( "cow.jpg" )

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        screen.fill((30,30,30))
        crop_image.reLoadImage()
        crop_image.drawAt( screen, ( 850, 360 ) )
        pygame.display.flip()