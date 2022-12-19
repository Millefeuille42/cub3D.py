from cub_vector import CubVector


class CubPlayer:
    def __init__(self, pos, prov_dir):
        self.pos = pos
        self.dir = prov_dir
        self.plan = CubVector(0, 0.66)
        self.view_offset = 0

    def move(self, angle, speed, prov_map):
        dire = CubVector(self.dir.x, self.dir.y)

        dire.rotate(angle)
        n_pos = CubVector(
            self.pos.x + dire.x / speed,
            self.pos.y + dire.y / speed
        )

        if prov_map[int(n_pos.y + dire.y / (speed / 2))][int(n_pos.x + dire.x / (speed / 2))] == 1:
            return
        self.pos.x = n_pos.x
        self.pos.y = n_pos.y

    def look_sides(self, angle):
        self.dir.rotate(angle)
        self.plan.rotate(angle)

    def look_up(self, speed):
        if self.view_offset < 100:
            self.view_offset += speed

    def look_down(self, speed):
        if self.view_offset > -100:
            self.view_offset -= speed