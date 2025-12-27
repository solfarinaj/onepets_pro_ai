# Casos de Prueba - Busqueda (STORY-OP-2-busqueda)

## Criterios de prioridad y severidad
- Prioridad: Alta, Media, Baja.
- Severidad: Critica, Mayor, Menor.

## TC-BUS-01 Buscar por nombre de mascota
Precondiciones:
- Existe paciente con mascota "Nina".

Pasos:
1) Ir al listado principal.
2) Ingresar "Nina" en el buscador.
3) Ejecutar la busqueda.

Resultado esperado:
- Se muestra el paciente con mascota "Nina".

Prioridad: Alta
Severidad: Mayor

## TC-BUS-02 Buscar por nombre de dueno
Precondiciones:
- Existe paciente con dueno "Sofia Gomez".

Pasos:
1) Ir al listado principal.
2) Ingresar "Sofia" en el buscador.
3) Ejecutar la busqueda.

Resultado esperado:
- Se muestran pacientes cuyo dueno contiene "Sofia".

Prioridad: Alta
Severidad: Mayor

## TC-BUS-03 Busqueda sin resultados
Precondiciones:
- Existe listado con pacientes.

Pasos:
1) Ir al listado principal.
2) Ingresar "ZZZ" en el buscador.
3) Ejecutar la busqueda.

Resultado esperado:
- Se muestra el mensaje de lista vacia: "No se encontraron pacientes que coincidan con la busqueda".

Prioridad: Media
Severidad: Menor

## TC-BUS-04 Busqueda vacia muestra todos
Precondiciones:
- Existen pacientes registrados.

Pasos:
1) Ir al listado principal.
2) Dejar el buscador vacio.
3) Ejecutar la busqueda.

Resultado esperado:
- Se muestran todos los pacientes.

Prioridad: Media
Severidad: Menor

## TC-BUS-05 Busqueda insensible a mayusculas
Precondiciones:
- Existe paciente con mascota "Nina".

Pasos:
1) Ir al listado principal.
2) Ingresar "nina" en el buscador.
3) Ejecutar la busqueda.

Resultado esperado:
- Se muestra el paciente con mascota "Nina".

Prioridad: Media
Severidad: Menor
