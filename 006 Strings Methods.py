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

print(a.split())  # Output: ['I', 'Love', 'Python', 'Programming']
print(a.split(" ", 2))  # Output: ['I', 'Love', 'Python Programming']
print(a.rsplit(" ", 2))  # Output: ['I Love', 'Python', 'Programming']

h = "Center"
print(h.center(10))  # Output: "  Center  "
print(h.center(10, "#"))  # Output: "##Center##"
print(h.rjust(10))  # Output: "    Center"
print(h.rjust(10, "#"))  # Output: "####Center"
print(h.ljust(10))  # Output: "Center    "
print(h.ljust(10, "#"))  # Output: "Center####"

i = "I Love Python and Python is Great"
print(i.count("Python"))  # Output: 2
print(i.count("Python", 10))  # Output: 1
print(i.count("Python", 0, 15))  # Output: 1

print(i.swapcase())  # Output: "i lOVE pYTHON AND pYTHON IS gREAT"
print(i.replace("Python", "Java"))  # Output: "I Love Java and Java is Great"
print(i.startswith("I Love"))  # Output: True
print(i.endswith("is Great"))  # Output: True

print(i.index("Python"))  # Output: 7
print(i.index("Python", 0, 20))  # Output: 7
#print(i.index("Python", 0, 5)) # Raises ValueError
print(a.find("Python"))  # Output: 7
print(a.find("Python", 0, 20))  # Output: 7
print(a.find("Python", 0, 5))  # Output: -1

j = """First Line
Second Line
Third Line"""
print(j.splitlines())  # Output: ['First Line', 'Second Line', 'Third Line']

k = "first line\nsecond line\rthird line"
print(k.splitlines())  # Output: ['first line', 'second line', 'third line']

l = "Hello\tWorld\tI\tLove\tPython"
print(l.expandtabs())  # Output: "Hello   World   I       Love    Python"
print(l.expandtabs(2))  # Output: "Hello World I Love Python"

m = "I Love Python Programming"
print(m.istitle())  # Output: True
print(m.isupper())  # Output: False
print(m.islower())  # Output: False

n = "12345"
print(n.isdigit())  # Output: True
print(n.isspace())  # Output: False

o = "Mahmoud_Batli"
print(o.isidentifier())  # Output: True
o = "MahmoudBatli"
print(o.isidentifier())  # Output: True
o = "1Mahmoud-Batli"
print(o.isidentifier())  # Output: False

p = "AAAbbbccc"
print(p.isalpha())  # Output: True

q = "AAAbbbccc123"
print(q.isalnum())  # Output: True

r = "One Two Three One Four One"
print(r.replace("One", "1"))  # Output: "1 Two Three 1 Four 1"
print(r.replace("One", "1", 2))  # Output: "1 Two Three 1 Four One"

list = ["I", "Love", "Python"]
print(" ".join(list))  # Output: "I Love Python"
print("-".join(list))  # Output: "I-Love-Python"
print("".join(list))  # Output: "ILovePython"

