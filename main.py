import os
import time
from empleado import Empleado
from tema import Tema
from curso import Curso
from curso_tema_video import CursoTV
from video import Video
from curso_tema import Curso_Tema

def clear():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

print("****************************************") 
print("*                                      *")
print("*              ¡Bienvenido!            *")
print("*                                      *")
print("****************************************")

while True: 
    print("""
        >>> Menu Principal <<<

1.- Empleados
2.- Cursos
3.- Temas
4.- Videos
5.- Temas asignados al curso
6.- Videos asignados a un tema
7.- Salir del programa

""")
    try:
        eleccion = int(input("Elige una opcion: "))
        clear()

        if eleccion == 1: #Se despliega el submenú de Empleados
            time.sleep(.5)
            while True:
                print("\nMenu Empleados\n\n1.- Agregar empleado\n2.- Borrar empleado\n3.- Modificar registro de empleado\n4.- Consultar todo \n5.- Ver datalles de empleado\n6.- Volver al menu principal\n")
                eleccion = input("Elige una opcion: ")

                if eleccion == "1":
                    time.sleep(.5)
                    Empleado.agregarEmpleado()

                elif eleccion == "2":
                    time.sleep(.5)
                    Empleado.borrarEmpleado()

                elif eleccion == "3":
                    time.sleep(.5)
                    Empleado.modificarEmpleado()

                elif eleccion == "4":
                    time.sleep(.5)
                    Empleado.mostrarEmpleados()

                elif eleccion == "5":
                    time.sleep(.5)
                    Empleado.buscarEmpleado()

                elif eleccion == "6":
                    print("\nVolviendo al menu principal...")
                    time.sleep(1)
                    clear()
                    break

                else:
                    print("Error, Opcion invalida!!!")

        elif eleccion == 2:#Se despliega el submenú de Cursos
            while True:
                print("\nMenu Cursos \n\n1.- Agregar curso\n2.- Borrar curso\n3.- Modificar registro de un curso\n4.- Consultar todo el curso\n5.- Ver detalles de un curso\n6.- Volver al menu principal\n")
                eleccion = int(input("Elige una opcion: "))
                time.sleep(.5)

                if eleccion == 1:
                    Curso.agregarCurso()
                    time.sleep(.5)

                elif eleccion == 2:
                    Curso.borrarCurso()
                    time.sleep(.5)

                elif eleccion == 3:
                    Curso.modificarCurso()
                    time.sleep(.5)

                elif eleccion == 4:
                    Curso.mostrarCurso()
                    time.sleep(.5)

                elif eleccion == 5:
                    Curso.buscarCurso()
                    time.sleep(.5)

                elif eleccion == 6:
                    print("Volviendo al menu principal...")
                    time.sleep(1)
                    clear()
                    break

        elif eleccion == 3:#Se despliega el submenú de Temas
            while True:
                print("\nMenu Temas \n\n1.- Agregar tema\n2.- Borrar tema\n3.- Modificar tema\n4.- Consultar todo\n5.- Ver detalles de algun tema\n6.- Volver al menu principal\n")
                eleccion = int(input("Elige una opcion: "))
                time.sleep(.5)

                if eleccion == 1:
                    Tema.agregarTema()
                    time.sleep(.5)

                elif eleccion == 2:
                    Tema.borrarTema()
                    time.sleep(.5)

                elif eleccion == 3:
                    Tema.modificarTema()
                    time.sleep(.5)

                elif eleccion == 4:
                    Tema.mostrarTemas()
                    time.sleep(.5)

                elif eleccion == 5:
                    Tema.buscarTema()
                    time.sleep(.5)

                elif eleccion == 6:
                    print("Volviendo al menu principal...")
                    time.sleep(1)
                    clear()
                    break

        elif eleccion == 4:#Se despliega el submenú de Videos
            while True:
                print("\nMenu Videos\n\n1.- Agregar video\n2.- Borrar video\n3.- Modificar video\n4.- Consultar todo el video\n5.- Ver detalles de algun video\n6.- Volver al menu principal\n")
                eleccion = int(input("Elige una opcion: "))
                time.sleep(.5)

                if eleccion == 1:
                    Video.agregarVideo()
                    time.sleep(.5)

                elif eleccion == 2:
                    Video.borrarVideo()
                    time.sleep(.5)

                elif eleccion == 3:
                    Video.modificarVideo()
                    time.sleep(.5)

                elif eleccion == 4:
                    Video.mostrarVideos()
                    time.sleep(.5)

                elif eleccion == 5:
                    Video.buscarVideo()
                    time.sleep(.5)

                elif eleccion == 6:
                    print("Volviendo al menu principal...")
                    time.sleep(1)
                    clear()
                    break

                else:
                    print("Error, Opcion invalida!!!")
                    time.sleep(.5)

        elif eleccion == 5:#Se despliega el submenú de Temas asignados a un curso
            while True:
                print("\nMenu Temas Asignados al Curso\n\n1.- Agregar tema asignado al curso\n2.- Borrar tema asignado al curso\n3.- Modificar tema asignado al curso\n4.- Consultar todo\n5.- Ver detalles de algun tema asignado al curso\n6.- Volver al menu principal\n")
                eleccion = int(input("Elige una opcion: "))
                time.sleep(.5)

                if eleccion == 1:
                    Curso_Tema.agregarCurso_Tema()
                    time.sleep(.5)

                elif eleccion == 2:
                    Curso_Tema.borrarCurso_Tema()
                    time.sleep(.5)

                elif eleccion == 3:
                    Curso_Tema.modificarCurso_Tema()
                    time.sleep(.5)

                elif eleccion == 4:
                    Curso_Tema.mostrarCurso_Tema()
                    time.sleep(.5)

                elif eleccion == 5:
                    Curso_Tema.buscarCurso_Tema()
                    time.sleep(.5)

                elif eleccion == 6:
                    print("\nVolviendo al menu principal...")
                    time.sleep(1)
                    clear()
                    break

                else:
                    print("Error, Opcion invalida!!!")
                    time.sleep(.5)

        elif eleccion == 6:#Se despliega el submenú de temas videos asignados a un tema
            while True:
                print("\nMenu Videos Asignados a un Tema\n\n1.- Agregar video asignado a un tema\n2. Borrar un video asignado a algun tema\n3.- Modificar un video asignado a un tema\n4.- Consultar todo\n5.- Ver detalle de algun video asignado a un tema\n6.- Volver al menu principal\n")
                eleccion = input("Elige una opcion: ")
                time.sleep(.5)

                if eleccion == "1":
                    CursoTV.agregarCursoTV()
                    time.sleep(.5)

                elif eleccion == "2":
                    CursoTV.borrarCursoTV()
                    time.sleep(.5)

                elif eleccion == "3":
                    CursoTV.modificarCursoTV()
                    time.sleep(.5)

                elif eleccion == "4":
                    CursoTV.mostrarCursoTV()
                    time.sleep(.5)

                elif eleccion == "5":
                    CursoTV.buscarCursoTV()
                    time.sleep(.5)

                elif eleccion == "6":
                    print("\nVolviendo al menu principal...")
                    time.sleep(1)
                    clear()
                    break

                else:
                    print("Error, Opcion invalida!!!")
                    time.sleep(.5)

        elif eleccion == 7:
            print("\nSaliendo...")
            time.sleep(1)
            break        

        else:
            print("\nError, opcion invalida!")
            time.sleep(.5)
    except:
        print("Error: Ingrese solo numeros enteros")
        time.sleep(.5)

