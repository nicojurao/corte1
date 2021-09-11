"""
int
float
str
list => array mutable
tupl => array inmutable
dict => objeto
"""

numero1=10 #int
numero2=10.1 #float
nombre="nico" #str

#listas o arreglos
materias=["bases de datos 1","deporte formativo", "ingles 2"]
lista_numeros=[1,2,3,4,5,6,7,8,9,0]
matriz_ejemplo=[[1,2],[3,4]]

materias[0]="lenguaje de 4ta"
print(materias[0]) 
print(matriz_ejemplo[1][0])
print(materias[0],materias[1])
print(matriz_ejemplo)

lista_sin_ordenar=[3,6,8,5,2,4]
print(lista_sin_ordenar)
lista_sin_ordenar.sort(reverse=True)
print(lista_sin_ordenar)

