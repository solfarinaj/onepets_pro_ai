# Fase 10 - Exploratory Test Results

## Alcance
Revision experta del formulario actual (nombre, peso, especie) y validaciones existentes.

## Hallazgos (edge cases no cubiertos)

1) Nombres con caracteres especiales o combinaciones no alfabeticas
- Ejemplo: "@@@", "---", "123-###".
- Riesgo: Se puede ingresar texto sin significado si se permite cualquier caracter con una sola letra.
- Sugerencia: agregar una regla de expresion regular para aceptar solo letras, espacios y apostrofes simples.

2) Peso con limites maximos por especie o rango razonable
- Ejemplo: 5000 kg para un perro o 3000 kg para un gato.
- Riesgo: Datos extremos afectan reportes y calculos.
- Sugerencia: definir rangos razonables por especie y rechazar valores fuera de rango.

3) Especie fuera del catalogo permitido
- Ejemplo: Especie vacia o no incluida en el listado (si se fuerza el select).
- Riesgo: Datos inconsistentes si la lista de especies no se controla en backend.
- Sugerencia: validar en backend que el valor de especie pertenezca al catalogo permitido.

## Conclusion
El formulario actual cubre validaciones basicas, pero faltan controles de formato y rangos para evitar datos atipicos. Se recomienda incorporar reglas de formato para nombres y rangos maximos/minimos por especie.
