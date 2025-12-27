# Especificaciones Funcionales - OnePets Pro (Fase 2)

## 1. Alcance funcional
El sistema debe permitir el registro, consulta, actualizacion y eliminacion de pacientes veterinarios con reglas de validacion basadas en el script Farina_Solange.py.

## 2. Roles
- Operador: personal que registra y gestiona pacientes.

## 3. Flujo principal
1) El operador accede al modulo de pacientes.
2) Registra un paciente nuevo con confirmacion previa.
3) Consulta listados o busca pacientes.
4) Actualiza o elimina registros segun necesidad.

## 4. Requerimientos funcionales

### RF-01 Crear paciente
- El sistema debe solicitar confirmacion antes de iniciar el registro.
- Debe capturar los campos:
  - Nombre del dueno (obligatorio).
  - Nombre de la mascota (obligatorio).
  - Especie (obligatorio).
  - Fecha de nacimiento (opcional).
  - Peso (obligatorio).
  - Unidad de peso (obligatorio: k o g).
  - Esterilizado (obligatorio: si/no).
- Debe registrar la fecha de registro automaticamente.
- Debe impedir duplicados por combinacion dueno + mascota (insensible a mayusculas).

### RF-02 Listar pacientes
- El sistema debe mostrar todos los pacientes registrados.
- Debe incluir: ID, dueno, mascota, especie, edad, peso y fecha de registro.
- Si no hay pacientes, debe informar que la lista esta vacia.

### RF-03 Buscar paciente
- El sistema debe permitir busqueda por:
  - ID del paciente.
  - Nombre de la mascota.
- Si no se encuentra, debe notificarlo.

### RF-04 Mostrar detalle de paciente
- El sistema debe mostrar:
  - ID, dueno, mascota, especie.
  - Fecha de nacimiento (o no registrada).
  - Edad calculada si existe fecha de nacimiento.
  - Peso con unidad.
  - Estado de esterilizacion.
  - Fecha de registro.

### RF-05 Actualizar paciente
- El sistema debe permitir modificar:
  - Nombre del dueno.
  - Nombre de la mascota.
  - Especie.
  - Peso.
  - Fecha de nacimiento.
  - Estado de esterilizacion.
- Debe actualizar la fecha de registro al guardar cambios.

### RF-06 Eliminar paciente
- El sistema debe solicitar confirmacion antes de eliminar.
- Debe borrar el registro si la confirmacion es positiva.

## 5. Validaciones y reglas de negocio
- Nombre del dueno y mascota:
  - No vacios.
  - Deben contener al menos una letra.
- Especie:
  - No vacia.
  - Minimo 2 caracteres.
  - Debe contener al menos una letra.
- Nombre dueno y mascota no pueden ser iguales.
- Peso:
  - Numerico.
  - Mayor que 0.
  - Acepta punto o coma como separador decimal.
- Fecha de nacimiento:
  - Formato dd/mm/aaaa.
  - Si invalida, se registra como desconocida.

## 6. Datos y formatos
- Fecha de registro: dd/mm/aaaa.
- Edad: calculada en anos a partir de fecha de nacimiento.
- Unidad de peso: k (kilogramos) o g (gramos).

## 7. Mensajes clave
- Confirmaciones para crear y eliminar.
- Notificaciones cuando no hay registros.
- Alertas por datos invalidos.

## 8. Fuera de alcance
- Historial clinico detallado.
- Pagos o facturacion.
- Multiusuario y permisos.
