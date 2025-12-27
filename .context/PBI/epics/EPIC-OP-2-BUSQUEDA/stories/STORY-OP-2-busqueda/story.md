# Story - Busqueda en listado de pacientes (STORY-OP-2-busqueda)

## Historia de usuario
Como operador, quiero buscar pacientes por nombre de mascota o dueno para encontrarlos rapidamente en el listado.

## Descripcion funcional
- El listado principal incluye un campo de busqueda (query param `q`).
- Si `q` tiene valor, se filtra por mascota o dueno con coincidencia parcial.
- Si `q` esta vacio, se muestran todos los pacientes.
- Si no hay resultados, se muestra un mensaje de lista vacia.

## Criterios de aceptacion
- Busqueda por mascota encuentra coincidencias parciales.
- Busqueda por dueno encuentra coincidencias parciales.
- Busqueda sin resultados muestra mensaje de vacio.
- Busqueda vacia muestra todos los registros.
