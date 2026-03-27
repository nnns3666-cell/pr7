class BoundingBox2D:
    def __init__(self):
        self._points = []

    def add_point(self, x, y):
        self._points.append((x, y))

    def _min_x(self):
        return min(p[0] for p in self._points)

    def _max_x(self):
        return max(p[0] for p in self._points)

    def _min_y(self):
        return min(p[1] for p in self._points)

    def _max_y(self):
        return max(p[1] for p in self._points)

    def left_x(self):
        return self._min_x()

    def right_x(self):
        return self._max_x()

    def bottom_y(self):
        return self._min_y()

    def top_y(self):
        return self._max_y()

    def width(self):
        return self._max_x() - self._min_x()

    def height(self):
        return self._max_y() - self._min_y()

box = BoundingBox2D()
box.add_point(-2, -3)
box.add_point(4, 5)
print(box.left_x(), box.right_x())
print(box.bottom_y(), box.top_y())
print(box.width(), box.height())
