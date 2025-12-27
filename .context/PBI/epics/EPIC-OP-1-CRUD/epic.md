# EPIC-OP-1-CRUD - Gestion de Pacientes

## Objetivo
Gestionar el ciclo completo de pacientes: alta, listado, busqueda, edicion y eliminacion.

## Alcance
- Registrar pacientes con validaciones basicas.
- Listar pacientes con datos clave.
- Buscar por nombre de mascota o dueno.
- Editar y eliminar pacientes existentes.

## Fuera de alcance
- Historial clinico detallado.
- Pagos o facturacion.
- Multiusuario con roles personalizados.

## Dependencias
- Model `Paciente` en `misapps/aplicacion1/models.py`.
- Vistas en `misapps/aplicacion1/views.py`.
- Formulario `PacienteForm` en `misapps/aplicacion1/forms.py`.
- Templates en `misapps/aplicacion1/templates/aplicacion1/`.

## Riesgos
- Datos inconsistentes si fallan validaciones en formulario.
