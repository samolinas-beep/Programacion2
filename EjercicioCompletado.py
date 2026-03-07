tareas = []

while True:
    print("\n--- Lista de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Marcar tarea como completada")
    print("5. Salir")

    opcion = input("Opcion: ")

    if opcion == "1":
        tarea = input("Nueva Tarea: ")
        tareas.append({"texto": tarea, "completada": False})
        print("Agregada")

    elif opcion == "2":
        if not tareas:
            print("No hay tareas")
        else:
            for i, t in enumerate(tareas, 1):
                estado = "✔" if t["completada"] else "✘"
                print(f"{i}. [{estado}] {t['texto']}")

    elif opcion == "3":
        idx = int(input("# a eliminar: "))
        if 1 <= idx <= len(tareas):
            tareas.pop(idx - 1)
            print("Tarea eliminada")
        else:
            print("Número inválido")

    elif opcion == "4":
        idx = int(input("# de tarea completada: "))
        if 1 <= idx <= len(tareas):
            tareas[idx - 1]["completada"] = True
            print("Tarea marcada como completada ✔")
        else:
            print("Número inválido")

    elif opcion == "5":
        break