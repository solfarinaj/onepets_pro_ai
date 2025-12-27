# EPIC-OP-2-BUSQUEDA - Busqueda de Pacientes

## Objetivo
Permitir que el operador encuentre pacientes rapidamente usando el buscador existente en el listado principal.

## Alcance
- Busqueda por nombre de mascota o dueno usando un campo unico.
- Filtro de resultados con coincidencia parcial (icontains).
- Visualizacion de resultados en el listado principal.

## Fuera de alcance
- Filtros avanzados (especie, fecha, peso).
- Ordenamiento y paginacion.
- Busqueda por ID en la interfaz.

## Dependencias
- Vista `index` en `misapps/aplicacion1/views.py`.
- Template `misapps/aplicacion1/templates/aplicacion1/index.html`.

## Riesgos
- Resultados vacios deben mostrar mensaje claro al usuario.
