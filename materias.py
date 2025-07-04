materias  = []
numVeces = int(input("ingresa la cantidad de materias: "))
for i in range(numVeces):
    materia = input("ingrese la materia: ")
    materias.append(materia)
print(materias)

reprobo = []

i=0
while i < len (materias):
    nota = float(input(f"ingrese la nota de la materia{materias[i]}"))
    if nota <3:
        reprobo.append(materias[i])
        i += 0
print(reprobo)
