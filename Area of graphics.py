import Graphics.Circle
print("CIRCLE")
r = int(input("Enter radius "))
Graphics.Circle.Circle(r)

import Graphics.Rectangle
print("RECTANGLE")
l = int(input("Enter length "))
b = int(input("Enter breadth "))
Graphics.Rectangle.Rectangle(l,b)

from Graphics.ThreeDgraphics import Cuboid
print("CUBOID")
l = int(input("Enter length "))
w = int(input("Enter width "))
h = int(input("Enter height "))
Graphics.ThreeDgraphics.Cuboid.Cuboid(l,w,h)

from Graphics.ThreeDgraphics import Sphere
print("SPHERE")
r = int(input("Enter radius "))
Graphics.ThreeDgraphics.Sphere.Sphere(r)
