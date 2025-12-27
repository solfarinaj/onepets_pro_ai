# Story - Registro de pacientes (STORY-OP-1-registro)

## Historia de usuario
Como operador, quiero registrar pacientes con datos basicos y validaciones claras, para mantener un control confiable de cada mascota.

## Descripcion funcional
- El sistema muestra un formulario de alta de pacientes.
- El operador completa los campos obligatorios y opcionales.
- Al guardar, el sistema valida los datos y crea el registro.
- El listado permite buscar por nombre de mascota o dueno.

## Campos del formulario
Obligatorios:
- Dueno.
- Mascota.
- Especie.
- Peso.
- Unidad de peso (k o g).
- Esterilizado.

Opcional:
- Fecha de nacimiento.

## Reglas y validaciones
- Dueno y mascota no pueden ser iguales.
- Peso debe ser mayor que 0.
- Fecha de nacimiento no puede ser futura.
- No se permiten campos obligatorios vacios.

## Criterios de aceptacion
- Registro exitoso crea un paciente y lo muestra en el listado.
- Si el peso es 0 o menor, se rechaza el registro.
- Si dueno y mascota son iguales, se rechaza el registro.
- Si la fecha de nacimiento es futura, se rechaza el registro.
- La busqueda por nombre encuentra pacientes por mascota o dueno.
