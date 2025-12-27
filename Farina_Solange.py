
# ===========================================================
# Autor: Solange Fariña
# -----------------------------------------------------------
# Sistema de gestión de pacientes veterinarios - OnePets
# ===========================================================

import datetime

# --- VARIABLES GLOBALES ---

pacientes = []        # Lista donde se almacenan los pacientes
contador_id = [1]     # Contador para generar IDs automáticos


# ===========================================================
# MENÚ PRINCIPAL
# ===========================================================

def mostrar_menu():
    print("\nBienvenido al sistema de gestión de pacientes OnePets")
    print("==============================================================")
    print("1. Crear paciente nuevo")
    print("2. Listar pacientes")
    print("3. Buscar paciente")
    print("4. Actualizar paciente")
    print("5. Eliminar paciente")
    print("6. Salir")
    print("==============================================================")


# ===========================================================
# FUNCIÓN PRINCIPAL QUE CONTROLA EL PROGRAMA
# ===========================================================
def inicio():
    while True:
        mostrar_menu()
        opcion = input("Elija una opción (1 al 6): ").strip()

        if opcion == "1":
            crear_paciente()
        elif opcion == "2":
            listar_pacientes()
        elif opcion == "3":
            buscar_paciente()
        elif opcion == "4":
            actualizar_paciente()
        elif opcion == "5":
            eliminar_paciente()
        elif opcion == "6":
            print("Gracias por usar OnePets. Hasta pronto.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


# ===========================================================
# UTILIDADES DE VALIDACIÓN
# ===========================================================

def contiene_letra(cadena):
    """Verifica si una cadena contiene al menos una letra."""
    return any(char.isalpha() for char in cadena)

def validar_nombre(campo_nombre, valor):
    """Valida que el nombre no esté vacío y contenga al menos una letra."""
    if not valor.strip():
        print(f"El {campo_nombre} no puede estar vacío.")
        return False
    if not contiene_letra(valor):
        print(f"El {campo_nombre} debe contener al menos una letra.")
        return False
    return True

def validar_especie(valor):
    """Valida que la especie tenga al menos 2 caracteres y contenga una letra."""
    if not valor.strip():
        print("La especie no puede estar vacía.")
        return False
    if len(valor) < 2:
        print("La especie debe tener al menos 2 caracteres.")
        return False
    if not contiene_letra(valor):
        print("La especie debe contener al menos una letra.")
        return False
    return True


# ===========================================================
# FUNCIÓN: CREAR NUEVO PACIENTE
# ===========================================================
# Solicita confirmación INMEDIATA al elegir la opción 1.
# Solo si confirma, se piden los datos del paciente.
# Incluye validaciones robustas y prevención de duplicados.
# ===========================================================

def crear_paciente():
    # Confirmación inmediata al iniciar la operación
    confirmacion = input("\n¿Está seguro de que desea crear un nuevo paciente? (s/n): ").strip().lower()
    if confirmacion not in ("s", "si", "sí"):
        print("Operación cancelada. Regresando al menú principal.")
        return

    print("\n--- CREAR NUEVO PACIENTE ---")

    nombre_dueno = input("Nombre del dueño: ").strip()
    if not validar_nombre("nombre del dueño", nombre_dueno):
        return

    nombre_mascota = input("Nombre de la mascota: ").strip()
    if not validar_nombre("nombre de la mascota", nombre_mascota):
        return
    
    if nombre_dueno.lower().strip() == nombre_mascota.lower().strip():
        print("El nombre del dueño y el nombre de la mascota no pueden ser iguales.")
        return

    especie = input("Especie (Perro, Gato, etc.): ").strip()
    if not validar_especie(especie):
        return

    # Verificación de duplicados (dueño + mascota, insensible a mayúsculas)
    for p in pacientes:
        if (p["dueno"].lower() == nombre_dueno.lower() and 
            p["mascota"].lower() == nombre_mascota.lower()):
            print("Este paciente ya está registrado.")
            return


    # Fecha de nacimiento (opcional)
    fecha_nac_str = input("Ingrese la fecha de nacimiento (dd/mm/aaaa) o deje vacío si se desconoce: ").strip()
    if fecha_nac_str:
        try:
            fecha_nacimiento = datetime.datetime.strptime(fecha_nac_str, "%d/%m/%Y").date()
        except ValueError:
            print("Formato de fecha inválido. Se guardará como desconocida.")
            fecha_nacimiento = None
    else:
        fecha_nacimiento = None

    # Peso (acepta coma o punto)
    while True:
        peso_str = input("Peso de la mascota (en kilogramos o gramos, ej: 26.5 o 2600): ").strip()
        peso_str = peso_str.replace(",", ".")  # convierte coma a punto
        try:
            peso = float(peso_str)
            if peso <= 0:
                print("El peso debe ser mayor que 0.")
                continue
            # Advertencia para valores extremos
            if peso > 100000:  # más de 100 kg si en gramos, o 100000 g
                print("⚠️  Advertencia: El peso ingresado es muy alto. ¿Está seguro?")
                conf = input("¿Confirmar peso? (s/n): ").strip().lower()
                if conf not in ("s", "si", "sí"):
                    continue
            break
        except ValueError:
            print("Ingrese un número válido para el peso (use coma o punto).")

    # Unidad de peso
    while True:
        unidad_peso = input("¿El peso está en (k)ilogramos o (g)ramos?: ").strip().lower()
        if unidad_peso in ("k", "g"):
            break
        else:
            print("Por favor, ingrese 'k' para kilogramos o 'g' para gramos.")

    # Esterilización (boolean)
    while True:
        esterilizado = input("¿Está esterilizado? (s/n): ").strip().lower()
        if esterilizado in ("s", "si", "sí"):
            esterilizado = True
            break
        elif esterilizado in ("n", "no"):
            esterilizado = False
            break
        else:
            print("Responda solo con 's' o 'n'.")

    # Fecha de registro
    fecha_registro = datetime.date.today()

    # Crear el registro de paciente
    paciente = {
        "id": contador_id[0],
        "dueno": nombre_dueno,
        "mascota": nombre_mascota,
        "especie": especie,
        "fecha_nacimiento": fecha_nacimiento,
        "peso": peso,
        "unidad_peso": unidad_peso,
        "esterilizado": esterilizado,
        "fecha_registro": fecha_registro
    }

    pacientes.append(paciente)
    print(f"Paciente '{nombre_mascota}' registrado con ID {contador_id[0]} el {fecha_registro}.")
    contador_id[0] += 1


# ===========================================================
# FUNCIÓN: LISTAR TODOS LOS PACIENTES
# ===========================================================

def listar_pacientes():
    print("\n--- LISTADO DE PACIENTES ---")

    if not pacientes:
        print("No hay pacientes registrados.")
    else:
        print(f"Total: {len(pacientes)} paciente(s)\n")
        print("{:<4} {:<12} {:<12} {:<10} {:<12} {:<10} {:<12}".format(
            "ID", "Dueño", "Mascota", "Especie", "Edad", "Peso", "Registro"))
        print("-" * 70)

        for p in pacientes:
            # Calcular edad si hay fecha de nacimiento
            if p["fecha_nacimiento"]:
                hoy = datetime.date.today()
                edad_anios = hoy.year - p["fecha_nacimiento"].year - (
                    (hoy.month, hoy.day) < (p["fecha_nacimiento"].month, p["fecha_nacimiento"].day)
                )
                edad_str = f"{edad_anios} años"
            else:
                edad_str = "Desconocida"

            peso_str = f"{p['peso']} {'kg' if p['unidad_peso']=='k' else 'g'}"
            fecha_str = p["fecha_registro"].strftime("%d/%m/%Y")

            print("{:<4} {:<12} {:<12} {:<10} {:<12} {:<10} {:<12}".format(
                p["id"], p["dueno"], p["mascota"], p["especie"], edad_str, peso_str, fecha_str
            ))


# ===========================================================
# FUNCIÓN: BUSCAR PACIENTE
# ===========================================================

def buscar_paciente():
    print("\n--- BUSCAR PACIENTE ---")

    if not pacientes:
        print("No hay pacientes registrados.")
        return

    print("1. Buscar por ID")
    print("2. Buscar por nombre de mascota")
    opcion = input("Elija una opción (1 o 2): ").strip()

    encontrado = False

    if opcion == "1":
        id_buscar = input("Ingrese el ID del paciente: ")
        for p in pacientes:
            if str(p["id"]) == id_buscar:
                mostrar_detalle(p)
                encontrado = True
                break

    elif opcion == "2":
        nombre_buscar = input("Ingrese el nombre de la mascota: ").strip().lower()
        for p in pacientes:
            if p["mascota"].lower() == nombre_buscar:
                mostrar_detalle(p)
                encontrado = True
                break

    else:
        print("Opción inválida. Debe elegir 1 o 2.")

    if not encontrado:
        print("Paciente no encontrado.")


# ===========================================================
# FUNCIÓN AUXILIAR PARA MOSTRAR UN PACIENTE
# ===========================================================

def mostrar_detalle(p):
    if p["fecha_nacimiento"]:
        hoy = datetime.date.today()
        edad_anios = hoy.year - p["fecha_nacimiento"].year - (
            (hoy.month, hoy.day) < (p["fecha_nacimiento"].month, p["fecha_nacimiento"].day)
        )
        edad_str = f"{edad_anios} años"
    else:
        edad_str = "Desconocida"

    peso_str = f"{p['peso']} {'kg' if p['unidad_peso']=='k' else 'g'}"
    est = "Sí" if p["esterilizado"] else "No"
    fecha_reg = p["fecha_registro"].strftime("%d/%m/%Y")
    fecha_nac = p["fecha_nacimiento"].strftime("%d/%m/%Y") if p["fecha_nacimiento"] else "No registrada"

    print("\nPaciente encontrado:")
    print(f"ID: {p['id']}")
    print(f"Dueño: {p['dueno']}")
    print(f"Mascota: {p['mascota']}")
    print(f"Especie: {p['especie']}")
    print(f"Fecha de nacimiento: {fecha_nac}")
    print(f"Edad: {edad_str}")
    print(f"Peso: {peso_str}")
    print(f"Esterilizado: {est}")
    print(f"Fecha de registro: {fecha_reg}")


# ===========================================================
# FUNCIÓN: ACTUALIZAR PACIENTE
# ===========================================================

def actualizar_paciente():
    print("\n--- ACTUALIZAR PACIENTE ---")

    if not pacientes:
        print("No hay pacientes registrados.")
        return

    listar_pacientes()
    try:
        id_buscar = int(input("Ingrese el ID del paciente a actualizar: "))
    except ValueError:
        print("Ingrese un número válido.")
        return

    for p in pacientes:
        if p["id"] == id_buscar:
            print(f"Modificando paciente: {p['mascota']}")
            print("1) Nombre dueño\n2) Nombre mascota\n3) Especie\n4) Peso\n5) Fecha nacimiento\n6) Estado esterilización")
            opcion = input("Seleccione campo a modificar: ").strip()

            if opcion == "1":
                nuevo_dueno = input("Nuevo nombre del dueño: ").strip()
                if validar_nombre("nombre del dueño", nuevo_dueno):
                    p["dueno"] = nuevo_dueno
                else:
                    print("Actualización cancelada.")
                    return
            elif opcion == "2":
                nueva_mascota = input("Nuevo nombre de la mascota: ").strip()
                if validar_nombre("nombre de la mascota", nueva_mascota):
                    p["mascota"] = nueva_mascota
                else:
                    print("Actualización cancelada.")
                    return
            elif opcion == "3":
                nueva_especie = input("Nueva especie: ").strip()
                if validar_especie(nueva_especie):
                    p["especie"] = nueva_especie
                else:
                    print("Actualización cancelada.")
                    return
            elif opcion == "4":
                nuevo_peso_str = input("Nuevo peso (coma o punto): ").replace(",", ".")
                try:
                    nuevo_peso = float(nuevo_peso_str)
                    if nuevo_peso <= 0:
                        print("El peso debe ser mayor que 0.")
                    else:
                        if nuevo_peso > 100000:
                            print("⚠️  Advertencia: El peso ingresado es muy alto.")
                            conf = input("¿Confirmar? (s/n): ").strip().lower()
                            if conf in ("s", "si", "sí"):
                                p["peso"] = nuevo_peso
                            else:
                                print("Peso no actualizado.")
                        else:
                            p["peso"] = nuevo_peso
                except ValueError:
                    print("Peso inválido, no se modificó.")
            elif opcion == "5":
                nueva_fecha = input("Nueva fecha de nacimiento (dd/mm/aaaa): ").strip()
                if nueva_fecha:
                    try:
                        p["fecha_nacimiento"] = datetime.datetime.strptime(nueva_fecha, "%d/%m/%Y").date()
                    except ValueError:
                        print("Formato inválido, no se modificó.")
                else:
                    p["fecha_nacimiento"] = None
            elif opcion == "6":
                p["esterilizado"] = input("¿Esterilizado? (s/n): ").strip().lower() in ("s", "si", "sí")
            else:
                print("Opción no válida.")
                return

            p["fecha_registro"] = datetime.date.today()
            print("Paciente actualizado correctamente.")
            return

    print("No se encontró un paciente con ese ID.")


# ===========================================================
# FUNCIÓN: ELIMINAR PACIENTE
# ===========================================================

def eliminar_paciente():
    print("\n--- ELIMINAR PACIENTE ---")

    if not pacientes:
        print("No hay pacientes registrados.")
        return

    listar_pacientes()
    try:
        id_buscar = int(input("Ingrese el ID del paciente a eliminar: "))
    except ValueError:
        print("Ingrese un número válido.")
        return

    for p in pacientes:
        if p["id"] == id_buscar:
            confirmacion = input(f"¿Está seguro de eliminar a '{p['mascota']}'? (s/n): ").strip().lower()
            if confirmacion in ("s", "si", "sí"):
                pacientes.remove(p)
                print(f"Paciente '{p['mascota']}' eliminado correctamente.")
            else:
                print("Eliminación cancelada.")
            return

    print("No se encontró un paciente con ese ID.")


# ===========================================================
# EJECUCIÓN DEL PROGRAMA
# ===========================================================
inicio()
