from empleado import Empleado
from tema import Tema
from curso import Curso
from curso_tema_video import CursoTV
from video import Video

while True:

    print("\nMenu Principal\n\n1.- Empleados\n2.- Cursos\n3.- Temas\n4.- Videos\n5.- Temas asignados al curso\n6.- Videos asignados a un tema\n7.- Salir\n")
    #try:
    eleccion = int(input("Elige una opcion: "))

    if eleccion == 1: #Se despliega el submenú de Empleados
        while True:
            print("\nMenu Empleados\n\n1.- Agregar empleado\n2.- Borrar empleado\n3.- Modificar registro de empleado\n4.- Consultar todo \n5.- Ver datalles de empleado\n6.- Volver al menu principal\n")
            eleccion = input("Elige una opcion: ")

            if eleccion == "1":
                Empleado.agregarEmpleado()

            elif eleccion == "2":
                Empleado.borrarEmpleado()

            elif eleccion == "3":
                Empleado.modificarEmpleado()

            elif eleccion == "4":
                Empleado.mostrarEmpleados()

            elif eleccion == "5":
                Empleado.buscarEmpleado()

            elif eleccion == "6":
                print("\nVolviendo al menu principal...")
                break

            else:
                print("Error, Opcion invalida!!!")

    elif eleccion == 2:#Se despliega el submenú de Cursos
        while True:
            print("\nMenu Cursos \n\n1.- Agregar curso\n2.- Borrar curso\n3.- Modificar registro de un curso\n4.- Consultar todo el curso\n5.- Ver detalles de un curso\n6.- Volver al menu principal\n")
            eleccion = int(input("Elige una opcion: "))

            if eleccion == 1:
                Curso.agregarCurso()

            elif eleccion == 2:
                Curso.borrarCurso()

            elif eleccion == 3:
                Curso.modificarCurso()

            elif eleccion == 4:
                Curso.mostrarCurso()

            elif eleccion == 5:
                #BuscarCurso()
                pass

            elif eleccion == 6:
                print("Volviendo al menu principal...")
                break

    elif eleccion == 3:#Se despliega el submenú de Temas
        while True:
            print("\nMenu Temas \n\n1.- Agregar tema\n2.- Borrar tema\n3.- Modificar tema\n4.- Consultar todo\n5.- Ver detalles de algun tema\n6.- Volver al menu principal\n")
            eleccion = int(input("Elige una opcion: "))

            if eleccion == 1:
                Tema.agregarTema()

            elif eleccion == 2:
                Tema.borrarTema()

            elif eleccion == 3:
                Tema.modificarTema()

            elif eleccion == 4:
                Tema.mostrarTemas()

            elif eleccion == 5:
                Tema.buscarTema()

            elif eleccion == 6:
                print("Volviendo al menu principal...")
                break

    elif eleccion == 4:#Se despliega el submenú de Videos
        while True:
            print("\nMenu Videos\n\n1.- Agregar video\n2.- Borrar video\n3.- Modificar video\n4.- Consultar todo el video\n5.- Ver detalles de algun video\n6.- Volver al menu principal\n")
            eleccion = int(input("Elige una opcion: "))

            if eleccion == 1:
                Video.agregarVideo()

            elif eleccion == 2:
                Video.borrarVideo()

            elif eleccion == 3:
                Video.modificarVideo()

            elif eleccion == 4:
                Video.mostrarVideos()

            elif eleccion == 5:
                Video.buscarVideo()

            elif eleccion == 6:
                print("Volviendo al menu principal...")
                break

            else:
                print("Error, Opcion invalida!!!")

    elif eleccion == 5:#Se despliega el submenú de Temas asignados a un curso
        print("\nMenu Temas Asignados al Curso\n\n1.agregar tema asignado al curso\n2.borrar tema asignado al curso\n3.modificar tema asignado al curso\n4.consultar todo el tema asignado al curso\n5.ver detalles de algun tema asignado al curso\n6.volver al menu principal\n")
        eleccion = input("Elige una opcion: ")

        #Agregar submenu de temas asignados al curso

    elif eleccion == 6:#Se despliega el submenú de temas videos asignados a un tema
        while True:
            print("\nMenu Videos Asignados a un Tema\n\n1.- Agregar video asignado a un tema\n2. Borrar un video asignado a algun tema\n3.- Modificar un video asignado a un tema\n4.- Consultar todo\n5.- Ver detalle de algun video asignado a un tema\n6.- Volver al menu principal\n")
            eleccion = input("Elige una opcion: ")

            if eleccion == "1":
                CursoTV.agregarCursoTV()

            elif eleccion == "2":
                CursoTV.borrarCursoTV()

            elif eleccion == "3":
                CursoTV.modificarCursoTV()

            elif eleccion == "4":
                CursoTV.mostrarCursoTV()

            elif eleccion == "5":
                CursoTV.buscarCursoTV()

            elif eleccion == "6":
                print("\nVolviendo al menu principal...")
                break

            else:
                print("Error, Opcion invalida!!!")

    elif eleccion == 7:
        print("\nSaliendo...")
        break        

    else:
        print("\nError, opcion invalida!")
    #except:
    #    print("Error: Ingrese solo numeros enteros").

