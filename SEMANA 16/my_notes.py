#Abrir archivo para escritura
Archivo = open('my_notes.txt', 'w')
#Escribir 3 lineas
Archivo.write('Hoy me sentí muy felíz al despertar')
Archivo.write('Desayuné un delicioso bolón con queso')
Archivo.write('Y almorcé un delicioso ceviche de camarón')
#Cerrar el archivo despues de escribir
Archivo.close()

#Abrir archivo para lectura
Archivo = open('my_notes.txt', 'r')
#Indicar que se lee linea a linea y eliminar saltos de linea
print(Archivo.readline().strip())
print(Archivo.readline().strip())
print(Archivo.readline().strip())
#Cerrar el archivo
Archivo.close()
