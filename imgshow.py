import cv2
import pygame
import os, os.path
import matplotlib.image as mpimg
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)



class UpdatedImage:
    def __init__( self, filename, w, h ):
        self.filename    = filename
        self.last_update = 0         # trigger initial load
        self.image       = None      # final surface
        self.w = w
        self.h = h
        # self.reLoadImage()           # make sure we load once, first
    
    def drawAt( self, window, position ):
        """ Draw the image to the screen at the given position """
        window.blit( self.image, position )

    def reLoadImage( self ):
        """ Load in the image iff it has changed on disk """
        current_file_time = os.path.getmtime( self.filename )
        if ( current_file_time > self.last_update):
            try:
                self.last_update = current_file_time
                img_crop = mpimg.imread( self.filename )
                img_crop_re = cv2.resize(img_crop, dsize=(self.h, self.w), interpolation=cv2.INTER_LINEAR)
                img_crop_ro = cv2.rotate(img_crop_re, cv2.ROTATE_180)
                img_crop_flip = cv2.flip(img_crop_ro,0)
                self.image = pygame.surfarray.make_surface(img_crop_flip)
            except:
                pass
    def changename(self, filename):
        self.filename = filename


if __name__ == "__main__":
    pygame.init()
    w = 720
    h = 960
    screen = pygame.display.set_mode((w, h))
    # image from Iris
    crop_image = UpdatedImage("/home/liam/Desktop/iris_openhouse/logos/cow.jpg", w, h)

    # absat logo
    absatraw = pygame.image.load("/home/liam/Desktop/iris_openhouse/logos/absatlogo.png")
    absatlogo = pygame.transform.scale(absatraw, (absatraw.get_width()*0.1, absatraw.get_height()*0.1))

    # ualberta logo
    uabraw = pygame.image.load("/home/liam/Desktop/iris_openhouse/logos/ua_logo.png")
    uablogo = pygame.transform.scale(uabraw, (uabraw.get_width()*0.17, uabraw.get_height()*0.17))

    error_img = cv2.rotate(cv2.flip(cv2.resize(mpimg.imread("/home/liam/Desktop/iris_openhouse/logos/error.jpg"), dsize=(h, w), interpolation=cv2.INTER_LINEAR), 0), cv2.ROTATE_90_CLOCKWISE)
    error_image = pygame.surfarray.make_surface(error_img)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False

        screen.fill((30,30,30))
        try:
            crop_image.reLoadImage()
            crop_image.drawAt( screen, (0, 0) )
            screen.blit(absatlogo, (0, h-absatlogo.get_height()))
            screen.blit(uablogo, ( (w/2 - uablogo.get_width()/2), h - uablogo.get_height()))
        except Exception as e:
            # print(e)
            screen = pygame.display.set_mode((h,w))
            screen.blit(error_image, (0, 0))
        else:
            if screen.get_size() != (w, h):
                screen = pygame.display.set_mode((w, h))
        
        pygame.display.flip()