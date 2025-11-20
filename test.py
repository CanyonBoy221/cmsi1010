from dataclasses import dataclass
import math


@dataclass
class Point3D:
    x: float
    y: float
    z: float

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def distance_to_origin(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)


# Example
p = Point3D(5.0, 2.5, -3.8)
print(p)
print(p.distance_to_origin())
