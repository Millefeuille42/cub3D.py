import constants
import pygame

from map import prov_map
from cub_color import CubColor
from cub_ray import CubRay
from cub_player import CubPlayer
from cub_vector import CubVector


actions = {}
screen: pygame.Surface
player = CubPlayer(CubVector(12.5, 10.5), CubVector(1, 0))
running = True


def render():
    global player

    ceil = CubColor(50, 50, 50)
    floor = CubColor(20, 20, 20)

    for x in range(constants.width):
        cam = 2 * x / constants.width - 1
        ray = CubRay(cam, player)
        ray.cast()
        lst = ray.calc(x, player)
        pygame.draw.line(screen, ceil.get_color(), (lst[1], 0), (lst[1], lst[2]))
        pygame.draw.line(screen, lst[0], (lst[1], lst[2]), (lst[1], lst[3]))
        pygame.draw.line(screen, floor.get_color(), (lst[1], lst[3]), (lst[1], constants.height))


def update():
    global actions

    tm = 2
    if actions[pygame.K_d]:
        player.move(90, int(20 / tm), prov_map)
    elif actions[pygame.K_a]:
        player.move(-90, int(20 / tm), prov_map)
    if actions[pygame.K_s]:
        player.move(180, int(10 / tm), prov_map)
    elif actions[pygame.K_w]:
        player.move(0, int(10 / tm), prov_map)
    if actions[pygame.K_UP]:
        player.look_up(int((constants.height / 100)) * tm)
    elif actions[pygame.K_DOWN]:
        player.look_down(int((constants.height / 100)) * tm)
    if actions[pygame.K_LEFT]:
        player.look_sides(int(constants.width / -500) * tm)
    elif actions[pygame.K_RIGHT]:
        player.look_sides(int(constants.width / 500) * tm)


def init_keys():
    actions[pygame.K_w] = False
    actions[pygame.K_a] = False
    actions[pygame.K_s] = False
    actions[pygame.K_d] = False
    actions[pygame.K_UP] = False
    actions[pygame.K_DOWN] = False
    actions[pygame.K_LEFT] = False
    actions[pygame.K_RIGHT] = False


def game():
    global running
    global screen

    FPS = pygame.time.Clock()

    init_keys()
    pygame.init()
    pygame.display.set_caption("cub3D")
    screen = pygame.display.set_mode((constants.width, constants.height))

    running = True
    while running:
        FPS.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                actions[event.key] = event.type == pygame.KEYDOWN
        update()
        render()
        pygame.display.update()


game()