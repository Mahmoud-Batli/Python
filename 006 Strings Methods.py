a = "I Love Python Programming"
b = "    I Love Python Programming    "
print(len(a))  # Output: 26
print(len(b))  # Output: 32

print(b.strip())  # Output: "I Love Python Programming"
print(b.rstrip())  # Output: "    I Love Python Programming"
print(b.lstrip())  # Output: "I Love Python Programming    "

c = "@#@#@#@# I Love Python Programming #@#@#@#@"
print(c.strip("@#"))  # Output: " I Love Python Programming "
print(c.rstrip("#@"))  # Output: "@#@#@#@# I Love Python Programming "
print(c.lstrip("@#"))  # Output: " I Love Python Programming #@#@#@#@"

d = "I Love 2d and 3d Graphics"
print(d.title())  # Output: "I Love 2D And 3D Graphics"
print(d.capitalize())  # Output: "I love 2d and 3d graphics"
print(d.upper())  # Output: "I LOVE 2D AND 3D GRAPHICS"
print(d.lower())  # Output: "i love 2d and 3d graphics"

e, f, g, = "1", "10", "100"
print(e.zfill(3))  # Output: "001"
print(f.zfill(3))  # Output: "010"
print(g.zfill(3))  # Output: "100"