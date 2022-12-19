import constants

from cub_vector import CubVector
from cub_color import CubColor
from map import prov_map


class CubRay:
    def __init__(self, cam, player):
        self.origin = CubVector(player.pos.x, player.pos.y)
        self.dir = CubVector(
            player.dir.x + player.plan.x * cam,
            player.dir.y + player.plan.y * cam
        )
        self.mpos = CubVector(int(player.pos.x), int(player.pos.y))
        self.dist = CubVector(
            1 if self.dir.x == 0 else 0,
            1 if self.dir.y == 0 else 0
        )
        if self.dir.x != 0 and self.dir.y != 0:
            self.dist.x = abs(1 / self.dir.x)
            self.dist.y = abs(1 / self.dir.y)
        self.step = CubVector(1, 1)
        self.sdist = CubVector(
            (self.mpos.x + 1.0 - player.pos.x) * self.dist.x,
            (self.mpos.y + 1.0 - player.pos.y) * self.dist.y
        )
        if self.dir.x < 0:
            self.step.x = -1
            self.sdist.x = (player.pos.x - self.mpos.x) * self.dist.x
        if self.dir.y < 0:
            self.step.y = -1
            self.sdist.y = (player.pos.y - self.mpos.y) * self.dist.y
        self.hit = 0
        self.side = 0

    def cast(self):
        while self.hit == 0:
            if self.sdist.x < self.sdist.y:
                self.side = 0
                self.sdist.x += self.dist.x
                self.mpos.x += self.step.x
            else:
                self.side = 1
                self.sdist.y += self.dist.y
                self.mpos.y += self.step.y
            if prov_map[int(self.mpos.y)][int(self.mpos.x)] == 1:
                self.hit = 1

    def calc(self, x, player):
        wall = CubColor(255, 55, 0)

        if self.side == 0:
            dist = (self.mpos.x - player.pos.x + (1 - self.step.x) / 2) / self.dir.x
        else:
            dist = (self.mpos.y - player.pos.y + (1 - self.step.y) / 2) / self.dir.y

        if dist == 0:
            line_height = 0
        else:
            line_height = int(constants.height / dist)

        start = int(-line_height / 2 + constants.height / 2 + player.view_offset)
        end = int(line_height / 2 + constants.height / 2 + player.view_offset)

        return [wall.shade(5, dist, False), x, start, end]