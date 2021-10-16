import pygame
import math

# recursive_tree - a simple demo of using pygame to draw a tree using recursion
# Eric McCreath - 2021 - GPLv3

(XDIM,YDIM) = (800,600)
WHITE = (255,255,255)
BLACK = (0,0,0)


def recursive_circles(screen, pos, radius, rec):
    """ draw a stack of circles """
    pygame.draw.circle(screen, BLACK, pos, radius, 2)
    if rec > 0:
        new_radius = radius * 0.7
        recursive_circles(screen, (pos[0],  pos[1] - radius - new_radius), new_radius, rec-1, )

def branch_pos(pos, angle, height):
    """ calculate the position at the top of a branch starting at 'pos' with a given 'angle'
        and 'height' """
    return (pos[0] + height*math.sin(angle), pos[1] - height*math.cos(angle))

def recursive_tree(screen, pos, height, angle, rec, a1, a2):
    """ draw a tree with the main trunk being made up of 2 sub trees"""
    pygame.draw.line(screen, BLACK, pos, branch_pos(pos,angle,height))
    if rec > 0:
        recursive_tree(screen, branch_pos(pos,angle,0.7*height), height*0.8, angle + a1, rec - 1,a1,a2)
        recursive_tree(screen, branch_pos(pos,angle,0.9*height), height*0.7, angle - a2, rec - 1,a1,a2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((XDIM,YDIM))
    clock = pygame.time.Clock()

    done = False
    while not done:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        mouse_pos = pygame.mouse.get_pos()
        # pygame.draw.line(screen, BLACK,  (100,100), (200,200), 3)
        # recursive_circles(screen, (XDIM/2,YDIM-80), 80, 160)

        recursive_tree(screen, (XDIM / 2, YDIM - 10), 180.0, 0, 12, math.pi * mouse_pos[0] / XDIM,
                       math.pi * mouse_pos[1] / YDIM)

        pygame.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    main()
