size = int(input())
result = 0
for _ in range(size):
    polyhedrons = input()
    if polyhedrons == "Tetrahedron":
        result+=4
    elif polyhedrons == "Cube":
        result +=6
    elif polyhedrons == "Octahedron":
        result +=8
    elif polyhedrons == "Dodecahedron":
        result += 12
    else:
        result +=20
print(result)