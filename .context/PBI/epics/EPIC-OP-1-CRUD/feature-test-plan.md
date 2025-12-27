# Plan de Pruebas - Registro de Pacientes (Fase 5)

## Alcance
Validar el flujo de registro de pacientes segun RF-01 y reglas de negocio del SRS.

## Supuestos
- Existe acceso al modulo de pacientes.
- El operador puede iniciar el registro y ver mensajes de validacion.

## Criterios de prioridad y severidad
- Prioridad: Alta, Media, Baja.
- Severidad: Critica, Mayor, Menor.

## Casos de prueba

### TC-REG-01 Registro exitoso con datos validos
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
2) Completar los campos con los datos de prueba.
3) Guardar el registro.

Resultado esperado:
- Registro creado con fecha de registro automatica.
- Paciente visible en listado.

Prioridad: Alta
Severidad: Mayor

### TC-REG-02 Peso igual a 0.0
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

### TC-REG-03 Dueno y mascota con el mismo nombre
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

### TC-REG-04 Especie invalida (menos de 2 caracteres)
Precondiciones:
- Registro de paciente en proceso.

Datos de prueba:
- Dueno: "Carla Diaz"
- Mascota: "Toby"
- Especie: "A"
- Peso: "6"
- Unidad: "k"
- Esterilizado: "no"

Pasos:
1) Iniciar registro y confirmar.
2) Completar datos con especie "A".
3) Intentar guardar.

Resultado esperado:
- El sistema muestra error de validacion de especie.
- No se crea el registro.

Prioridad: Media
Severidad: Menor

### TC-REG-05 Duplicado por combinacion dueno + mascota
Precondiciones:
- Existe un paciente "Sofia Gomez" + "Nina" registrado.

Datos de prueba:
- Dueno: "Sofia Gomez"
- Mascota: "Nina"
- Especie: "Gato"
- Peso: "4.2"
- Unidad: "k"
- Esterilizado: "si"

Pasos:
1) Iniciar registro y confirmar.
2) Completar datos con la combinacion existente.
3) Intentar guardar.

Resultado esperado:
- El sistema detecta duplicado y bloquea el registro.
- No se crea un nuevo paciente.

Prioridad: Alta
Severidad: Mayor

### TC-REG-06 Fecha de nacimiento con formato invalido
Precondiciones:
- Registro de paciente en proceso.

Datos de prueba:
- Dueno: "Mario Ruiz"
- Mascota: "Kira"
- Especie: "Perro"
- Fecha nacimiento: "2020-05-12"
- Peso: "18"
- Unidad: "k"
- Esterilizado: "no"

Pasos:
1) Iniciar registro y confirmar.
2) Ingresar fecha con formato invalido.
3) Intentar guardar.

Resultado esperado:
- El sistema muestra mensaje de formato invalido y registra fecha como desconocida o solicita correccion.

Prioridad: Baja
Severidad: Menor
