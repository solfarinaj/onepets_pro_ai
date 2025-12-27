# Code Review Feedback - pacientes app

## Seguridad
- Eliminar pacientes se ejecuta via GET en `pacientes/views.py` usando un link en `pacientes/templates/pacientes/index.html`. Esto permite borrados accidentales y evita protecciones CSRF (deberia ser POST con confirmacion).
- El uso de `permission_required('pacientes.delete_paciente')` esta bien, pero debe acompañarse con validacion de metodo para evitar borrado por enlace directo.

## Legibilidad (PEP8)
- `pacientes/forms.py` no deja una linea en blanco entre la definicion del campo `especie` y la clase `Meta`, lo que reduce legibilidad.

## Optimizacion
- La busqueda en `pacientes/views.py` usa `icontains` y una union con `|`. Para busqueda exacta y mas eficiente, conviene usar `iexact` con `Q` en una sola consulta.
- No hay paginacion; con volumen grande se debe agregar mas adelante (fuera del alcance inmediato).

## Seguimiento de pruebas (Fase 10/11)
- `whitenoise` no esta instalado en el entorno local, lo que rompe los tests al cargar MIDDLEWARE. Solucion: instalar dependencia o cargar WhiteNoise de forma condicional en settings para tests.
- La prueba de fecha futura usa `date.today()`; si `timezone.localdate()` coincide con esa fecha por zona horaria, la validacion no falla. Solucion: usar `timezone.localdate()` en el test para construir una fecha realmente futura.
