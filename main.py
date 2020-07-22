from empleado import Empleado

while True:

    print("\nMenu Principal\n\n1.- Empleados\n2.- Cursos\n3.- Temas\n4.- Videos\n5.- Temas asignados al curso\n6.- Videos asignados a un tema\n7.- Salir\n")
    #try:
    eleccion = int(input("Elige una opcion: "))

    if eleccion == 1:
            
        while True:

            print("\nMenu Empleados\n\n1.- Agregar empleado\n2.- Borrar empleado\n3.- Modificar registro de empleado\n4.- Consultar todo \n5.- Ver datalles de empleado\n6.- Volver al menu principal\n")
            eleccionEmpleado = int(input("Elige una opcion: "))

            if eleccionEmpleado == 1:
                Empleado.agregarEmpleado()

            elif eleccionEmpleado == 2:
                Empleado.borrarEmpleado()

            elif eleccionEmpleado == 3:
                #modificarEmpleado()
                pass

            elif eleccionEmpleado == 4:
                Empleado.mostrarEmpleados()

            elif eleccionEmpleado == 5:
                #buscarEmpleado()
                pass

            elif eleccionEmpleado == 6:
                print("Volviendo al menu principal...")
                break


    elif eleccion == 2:
        print("\nMenu Cursos \n\n1.- Agregar curso\n2.- Borrar curso\n3.- Modificar registro de un curso\n4.- Consultar todo el curso\n5.- Ver detalles de un curso\n6.- Volver al menu principal\n")
        eleccion = input("Elige una opcion: ")

        if eleccionCurso == 1:
            Curso.agregarCurso()

        elif eleccionCurso == 2:
            Curso.borrarCurso()

        elif eleccionCurso == 3:
            #modificarCurso()
            pass

        elif eleccionCurso == 4:
            Curso.mostrarCurso()

        elif eleccionCurso == 5:
            #BuscarCurso()
            pass

        elif eleccionCurso == 6:
            print("Volviendo al menu principal...")

    elif eleccion == 3:
        print("\nMenu Temas \n\n1.- Agregar tema\n2.- Borrar tema\n3.- Modificar tema\n4.- Consultar todo\n5.- Ver detalles de algun tema\n6.- Volver al menu principal\n")
        eleccionTema = int(input("Elige una opcion: "))

        if eleccionTema == 1:
            Tema.agregarTema()

        elif eleccionTema == 2:
            Tema.borrarTema()

        elif eleccionTema == 3:
            #modificarTema()
            pass

        elif eleccionTema == 4:
            Tema.mostrarTema()

        elif eleccionTema == 5:
            #BuscarTema()
            pass

        elif eleccionTema == 6:
            print("Volviendo al menu principal...")

    elif eleccion == 4:
        print("\nMenu Videos\n\n1.agregar video\n2.borra video\n3.modificar video\n4.consultar todo el video\n5.ver datelles de algun video\n6.volver al menu pricipal\n")
        eleccion = input("Elige una opcion: ")

        if eleccionVideo == 1:
            Video.agregarVideo()

        elif eleccionVideo == 2:
            Video.borrarVideo()

        elif eleccionVideo == 3:
            #modificarVideo()
            pass

        elif eleccionVideo == 4:
            Video.mostrarVideo()

        elif eleccionVideo == 5:
            #BuscarVideo()
            pass

        elif eleccionVideo == 6:
            print("Volviendo al menu principal...")

    elif eleccion == 5:
        print("\nMenu Temas Asignados al Curso\n\n1.agregar tema asignado al curso\n2.borrar tema asignado al curso\n3.modificar tema asignado al curso\n4.consultar todo el tema asignado al curso\n5.ver detalles de algun tema asignado al curso\n6.volver al menu principal\n")
        eleccion = input("Elige una opcion: ")

        #Agregar submenu de temas asignados al curso

    elif eleccion == 6:
        print("\nMenu Videos Asignados a un Tema\n\n1.agregar video asignado a un tema\n2.borrar un video asignado a algun tema\n3.modificar un video asignado a un tema\n4.consultar todo el video asignado a un tema\n5.ver detalles de algun video asignado a un tema\n6.volver al menu principal\n")
        eleccion = input("Elige una opcion: ")

        #Ingresar subMenu de videos asignados a un tema
        
    elif eleccion == 7:
        print("\nSaliendo...")
        break        
        
    else:
        print("\nError, opcion invalida!")
    #except:
    #    print("Error: Ingrese solo numeros enteros").

