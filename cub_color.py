def shade_color(intensity, dist, way, color):
    if color >= 255 - 20:
        color = 255 - 20
    if way:
        ret = ((color / 255.0) + 0.1) * (intensity * (dist / 255.0))
    else:
        ret = ((color / 255.0) + 0.1) * (intensity * (255.0 / dist))

    ret = color + 20 if ret > color + 20 else ret
    ret = 0 if ret < 0 else ret

    return int(ret)


class CubColor:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        self.shadedR = 0
        self.shadedG = 0
        self.shadedB = 0

    def shade(self, intensity, dist, way):
        self.shadedR = shade_color(intensity, dist, way, self.r)
        self.shadedG = shade_color(intensity, dist, way, self.g)
        self.shadedB = shade_color(intensity, dist, way, self.b)
        return [self.shadedR, self.shadedG, self.shadedB]

    def get_color(self):
        return [self.r, self.g, self.b]
