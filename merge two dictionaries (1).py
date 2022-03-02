d1 = {"a":100,"b":200, "c":300, "d":600}
d2 = {"x":50, "y":80, "z":309}
print(d1)
print(d2)
d = d1.copy()
d.update(d2)
print("Merged dictionary is:",d)