# Resumen Ejecutivo - OnePets Pro (Fase 2)

## Vision del producto
OnePets Pro es un sistema CRUD para clinicas veterinarias pequenas que permite registrar, consultar y mantener el historial basico de pacientes. El objetivo es reducir errores de carga, estandarizar la informacion y agilizar la atencion diaria.

## Problema
Los registros manuales y planillas dispersas generan datos incompletos, duplicados y dificiles de recuperar. Esto impacta la operacion diaria, el seguimiento de pacientes y la comunicacion con clientes.

## Solucion propuesta
Implementar un sistema web en Django que centralice el registro de pacientes con validaciones, busquedas rapidas y actualizacion segura de datos.

## Publico objetivo
- Clinicas veterinarias pequenas o medianas.
- Personal administrativo y veterinarios.

## Alcance de la Fase 2 (Requerimientos)
- Definir funcionalidades clave basadas en el script actual.
- Establecer campos obligatorios del formulario de registro.
- Documentar reglas de negocio y validaciones.

## Funcionalidades clave
- Crear paciente con validaciones y confirmacion inicial.
- Listar pacientes con resumen de datos.
- Buscar paciente por ID o nombre de mascota.
- Actualizar datos del paciente.
- Eliminar paciente con confirmacion.

## Campos del formulario de registro
Obligatorios:
- Nombre del dueno.
- Nombre de la mascota.
- Especie.
- Peso.
- Unidad de peso (k o g).
- Esterilizado (si/no).

Opcionales:
- Fecha de nacimiento.

## Reglas de negocio principales
- No se permiten campos obligatorios vacios.
- Dueno y mascota no pueden tener el mismo nombre.
- No se permiten duplicados por combinacion dueno + mascota.
- Peso debe ser mayor que 0.
- Fecha de nacimiento debe respetar formato dd/mm/aaaa.

## Metricas de exito
- Reduccion de duplicados y registros incompletos.
- Menor tiempo para encontrar pacientes.
- Registro consistente de datos criticos.

## Supuestos y restricciones
- Base de datos SQLite.
- Interfaz web con HTML y Bootstrap 5.
- Mantener comportamiento alineado al script base.
