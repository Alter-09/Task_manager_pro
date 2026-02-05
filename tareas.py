from funciones import cargar_tareas, guardar_tareas, mostrar_tareas, agregar_tarea, completar_tarea, eliminar_tarea

"""Gestor de Tareas - Task Master Pro
Este script permite a los usuarios gestionar sus tareas diarias
a través de una interfaz de línea de comandos. Las tareas se almacenan
en un archivo JSON para persistencia."""

def menu():
    tareas = cargar_tareas()

    while True:
        print("""
TASK MASTER PRO
1. Ver tareas
2. Agregar tarea
3. Completar tarea
4. Eliminar tarea
5. Salir
        """)

        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()


