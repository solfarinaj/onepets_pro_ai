# Code Review Feedback - pacientes app

## Seguridad
- Eliminar pacientes se ejecuta via GET en `pacientes/views.py` usando un link en `pacientes/templates/pacientes/index.html`. Esto permite borrados accidentales y evita protecciones CSRF (deberia ser POST con confirmacion).
- El uso de `permission_required('pacientes.delete_paciente')` esta bien, pero debe acompañarse con validacion de metodo para evitar borrado por enlace directo.

## Legibilidad (PEP8)
- `pacientes/forms.py` no deja una linea en blanco entre la definicion del campo `especie` y la clase `Meta`, lo que reduce legibilidad.

## Optimizacion
- La busqueda en `pacientes/views.py` usa `icontains` y una union con `|`. Para busqueda exacta y mas eficiente, conviene usar `iexact` con `Q` en una sola consulta.
- No hay paginacion; con volumen grande se debe agregar mas adelante (fuera del alcance inmediato).
