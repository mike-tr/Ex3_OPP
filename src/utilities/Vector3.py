import math


class Vector3:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return str(float(self.x)) + "," + str(float(self.y)) + "," + str(float(self.z))

    def to_tuple2d(self) -> (float, float):
        return self.x, self.y

    def to_tuple3d(self) -> (float, float, float):
        return self.x, self.y, self.z

    def sqrt_magnitude(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    def magnitude(self):
        return math.sqrt(self.sqrt_magnitude())

    def distance(self, other):
        return (self - other).magnitude()

    def normalize(self):
        return self / self.magnitude()

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vector3(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other):
        return Vector3(self.x / other, self.y / other, self.z / other)
