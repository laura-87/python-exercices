course = "Python Programming"
print(len(course))
print(course[0])
print(course[-2])
print(course[0:3])
print(course[1:3])
print(course[:3])
print(course[0:])
print(course[:])

print(id(course))
print(id(course[0]))

# \"
# \'
# \\
# \n  salto de linea
# """ str de multiple linea

message = "Python \n\"Programming\""
print(message)

first = "Laura"
last = "Alvear"
#full = first + " " + last
full = f"{first} {last}"
print(course.upper())
print(course.lower())
print(course.title())

full = " algo con un espacio al inicio"
print(full.strip())# quita los espacios al inicio, sirve para los inputs

print(course.find("gr")) #devuelve la posicion del primer caracter requerido
print(course.replace("P", "_"))
print("Programming" in course)






