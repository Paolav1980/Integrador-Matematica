
#Esta funcion va a convertir los número ingresados (DNI) en un string,
#  separandolo digito por digito
#lo guardamos en un nuevo conjunto 
#Con la funcion set(), Python crea un conjunto ( sin duplicados, 
# desordenado y mutable) Tiene incorporado Intersection . Union - diference

def obtener_conjunto_digitos(dni):
    return set(str(dni))

#Ingreso de cantidad de elementos (Documentos)
cantidad = int(input("Indique la cantidad de DNI que debe ingresar: "))

documentos = [] #creamos la lista para guardar los documentos 

for i in range(cantidad): 
    #solicitamos al usuario que nos indique cuantos DNI desea registrar

    dni = input(f"Ingrese el DNI {i+1}:  ")

    # una vez que tenemos la cantidad de conjuntos, vamos a 
    # ir sumando hasta llegar al total de conjuntos deseados)
    documentos.append(dni)
     #guardamos cada uno de los DNI en la lista documentos con el comando 
     # append


#llamamos a la funcion obtenerconjuntodigitos con un parámetro 
#Obtner conjuntos de dígitos únicos 

conjuntos = [obtener_conjunto_digitos(dni) for dni in documentos]

# Mostrar los conjuntos - Asignaremos una letra a cada conjunto 
#va a estar generado por la tabla ASCII , con la función
#chr que convierte numeros en su letra correspondiente chr (65) es A

print("n/conjuntos de dígitos únicos: ")

for i, conjunto in enumerate(conjuntos):
    print(f"Conjunto : {chr(65+i)}: {conjunto}")

# Unión de todos los elementos de los conjuntos 
# * desenpaqueta una lista 
# Set une los elementos 
union_total = set.union(*conjuntos)
print("Unión total:", union_total)

#  Intersección total

interseccion_total = set.intersection(*conjuntos)
print("Intersección total:", interseccion_total)

# Diferencia entre A y B, B y C,... hasta - 1, luego no tendria con qué comparar 

print("\nDiferencias entre pares:")
for i in range(len(conjuntos) - 1):
    diferencia = conjuntos[i] - conjuntos[i + 1]
    print(f"Diferencia {chr(65+i)} - {chr(66+i)}: {diferencia}")

# Diferencia simétrica entre A y B
# El operador ^ realiza la diferencia simétrica 
print("\nDiferencia simétrica entre A y B:", conjuntos[0] ^ conjuntos[1])

# Condiciones lógicas
print("\nEvaluaciones lógicas:")

if all(len(c) >= 5 for c in conjuntos): # verifica si todos los conjuntos tienen al menos 5 digitos diferentes.
    print("Alta diversidad numérica")

digito_comun = set.intersection(*conjuntos)
if digito_comun:
    print("Dígito(s) común(es):", digito_comun)

if len(digito_comun) == 1:
    print("Dígito representativo:", list(digito_comun)[0])
else:
    print("No hay un único dígito representativo")

pares = sum(1 for c in conjuntos if len(c) % 2 == 0)
impares = len(conjuntos) - pares
if pares > impares:
    print("Grupo par")