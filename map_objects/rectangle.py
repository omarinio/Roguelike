class Rectangle:
    def __init__(self, x, y, w, h):
        self.x_start = x
        self.y_start = y
        self.x_end = x + w
        self.y_end = y + h

    def center(self):
        center_x = int((self.x_start + self.x_end) / 2)
        center_y = int((self.y_start + self.y_end) / 2)

        return center_x, center_y

    def intersect(self, rect2):
        return (self.x_start <= rect2.x_end and self.x_end >= rect2.x_start and
                self.y_start <= rect2.y_end and self.y_end >= rect2.y_start)
