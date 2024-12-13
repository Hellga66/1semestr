class Vector:
    def __init__(self, vector):
        try:
            x, y, z = vector.strip('{}').split(',')
            self.x = float(x)
            self.y = float(y)
            self.z = float(z)
        except ValueError:
            raise ValueError
        assert isinstance(self.x, (int, float))
        assert isinstance(self.y, (int, float))
        assert isinstance(self.z, (int, float))

    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(f"{{{self.x + other.x}, {self.y + other.y}, {self.z + other.z}}}")
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(f"{{{self.x - other.x}, {self.y - other.y}, {self.z - other.z}}}")
        return TypeError

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(other, (int, float)):
            return Vector(f"{{{self.x * other}, {self.y * other}, {self.z * other}}}")
        return TypeError

    def __repr__(self):
        return f"{{{self.x}, {self.y}, {self.z}}}"






set_of_points=list(Vector(x) for x in input().split())
center_of_mass=Vector('{0,0,0}')
for i in range(len(set_of_points)):
    center_of_mass+=set_of_points[i]*(1/len(set_of_points))


print(center_of_mass)

