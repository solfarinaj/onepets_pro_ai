# Implementation Plan - Registro de Pacientes (STORY-OP-1-registro)

## Logica de negocio
Objetivo: garantizar que dueno y mascota no sean iguales.

Propuesta (Form):
- Mantener la validacion en `PacienteForm.clean()`.
- Comparar `dueno` y `mascota` en minusculas y sin espacios extra.
- Si son iguales, lanzar `ValidationError` y bloquear el guardado.

Propuesta (Modelo, opcional):
- Implementar `clean()` en `Paciente` con la misma regla.
- Llamar `full_clean()` en `save()` o en la vista antes de guardar.
- Esto asegura la regla aun si se crean registros sin el formulario.

Decision recomendada:
- Usar ambas capas si queres defensa en profundidad (form + modelo).

## Interfaz
Objetivo: que el campo `especie` sea un desplegable y no texto libre.

Opcion A (Model + Form):
- Definir un listado fijo de especies en `Paciente` (choices).
- Cambiar `especie = models.CharField(..., choices=ESPECIES)`.
- En el formulario, usar `forms.Select` (o dejar que Django lo haga por default).
- Actualizar tests si cambian los valores permitidos.

Opcion B (Solo Form):
- Mantener el modelo como `CharField`.
- Cambiar el widget en `PacienteForm` para que `especie` use `forms.Select`.
- Definir opciones en el form (por ejemplo: Perro, Gato, Ave, Roedor, Reptil, Otro).

Decision recomendada:
- Opcion A si queres consistencia en base de datos.
- Opcion B si queres flexibilidad sin migracion inmediata.

## Seguridad
Objetivo: permitir borrar pacientes solo a usuarios admin.

Pasos recomendados:
1) Proteger la vista `eliminar_paciente` con `@user_passes_test(lambda u: u.is_staff)` o `@permission_required('pacientes.delete_paciente')`.
2) En templates, ocultar el boton "Eliminar" para usuarios no admin.
3) Validar en servidor (no solo UI) y devolver 403 si no tiene permisos.
4) Opcional: configurar permisos por grupo para roles futuros.
