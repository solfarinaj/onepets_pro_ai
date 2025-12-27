# Casos de Prueba - Registro y Busqueda de Pacientes

## Alcance
Casos basados en el formulario de registro y reglas de negocio del sistema.

## Criterios de prioridad y severidad
- Prioridad: Alta, Media, Baja.
- Severidad: Critica, Mayor, Menor.

## TC-REG-01 Happy Path: Registro exitoso
Objetivo:
- Verificar que el registro se completa con datos validos.

Precondiciones:
- No existe un paciente con la combinacion dueno + mascota.

Datos de prueba:
- Dueno: "Ana Lopez"
- Mascota: "Roco"
- Especie: "Perro"
- Fecha nacimiento: "12/05/2020"
- Peso: "12.5"
- Unidad: "k"
- Esterilizado: "si"

Pasos:
1) Iniciar registro y confirmar.
2) Completar todos los campos con los datos de prueba.
3) Guardar el registro.

Resultado esperado:
- Registro creado con fecha de registro automatica.
- Paciente visible en listado.

Prioridad: Alta
Severidad: Mayor

## TC-REG-02 Error: Peso menor o igual a 0
Objetivo:
- Validar que el sistema rechaza pesos invalidos.

Precondiciones:
- Registro de paciente en proceso.

Datos de prueba:
- Dueno: "Luis Perez"
- Mascota: "Mika"
- Especie: "Gato"
- Peso: "0.0"
- Unidad: "k"
- Esterilizado: "no"

Pasos:
1) Iniciar registro y confirmar.
2) Completar datos y colocar peso "0.0".
3) Intentar guardar.

Resultado esperado:
- El sistema rechaza el peso y muestra mensaje de error.
- No se crea el registro.

Prioridad: Alta
Severidad: Mayor

## TC-REG-03 Error: Dueno y mascota con el mismo nombre
Objetivo:
- Validar regla de negocio de nombres iguales.

Precondiciones:
- Registro de paciente en proceso.

Datos de prueba:
- Dueno: "Luna"
- Mascota: "Luna"
- Especie: "Perro"
- Peso: "8"
- Unidad: "k"
- Esterilizado: "si"

Pasos:
1) Iniciar registro y confirmar.
2) Completar datos con dueno y mascota iguales.
3) Intentar guardar.

Resultado esperado:
- El sistema rechaza el registro por regla de negocio.
- No se crea el paciente.

Prioridad: Media
Severidad: Mayor

## TC-REG-04 Error: Fecha de nacimiento en el futuro
Objetivo:
- Validar que no se aceptan fechas futuras.

Precondiciones:
- Registro de paciente en proceso.

Datos de prueba:
- Dueno: "Mario Ruiz"
- Mascota: "Kira"
- Especie: "Perro"
- Fecha nacimiento: "31/12/2099"
- Peso: "18"
- Unidad: "k"
- Esterilizado: "no"

Pasos:
1) Iniciar registro y confirmar.
2) Ingresar fecha de nacimiento futura.
3) Intentar guardar.

Resultado esperado:
- El sistema bloquea el registro y muestra mensaje de fecha invalida.
- No se crea el paciente.

Prioridad: Media
Severidad: Menor

## TC-BUS-01 Busqueda: Encontrar paciente por nombre
Objetivo:
- Verificar busqueda por nombre de mascota o dueno.

Precondiciones:
- Existe un paciente registrado: Dueno "Sofia Gomez", Mascota "Nina".

Datos de prueba:
- Criterio de busqueda: "Nina".

Pasos:
1) Ir al modulo de busqueda.
2) Elegir busqueda por nombre.
3) Ingresar "Nina" y ejecutar la busqueda.

Resultado esperado:
- El sistema muestra el paciente correspondiente.
- Los datos coinciden con el registro almacenado.

Prioridad: Media
Severidad: Menor
