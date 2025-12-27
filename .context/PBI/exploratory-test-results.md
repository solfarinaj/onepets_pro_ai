# Fase 10 - Exploratory Test Results

## Alcance
Analisis basado en estandares de industria para el formulario actual (nombre, peso, especie).

## Caso borde 1: Nombre con emojis o simbolos
Observacion:
- La validacion actual solo exige al menos una letra.
- Un nombre como "Roco 🐶" pasaria si tiene letras, y uno como "@@@" se bloquea.

Riesgo:
- Emojis y simbolos pueden causar problemas de integridad, reportes o integraciones.

Recomendacion:
- Definir una regla de formato (regex) para permitir letras, espacios y apostrofes simples.
- Bloquear emojis y simbolos no alfabeticos si el negocio requiere datos estrictos.

## Caso borde 2: Peso maximo
Observacion:
- La validacion actual solo impide pesos <= 0.

Riesgo:
- Pesos extremos (ej. 500 kg) distorsionan reportes y decisiones clinicas.

Recomendacion:
- Definir un rango razonable global (ej. 0.1 a 150 kg) o por especie.
- Agregar validacion de maximo en el formulario y/o modelo.

## Caso borde 3: Doble envio del formulario
Observacion:
- El flujo actual no previene doble envio en el cliente.
- No existe una regla de unicidad por dueno+mascota en base de datos.

Riesgo:
- Registros duplicados por doble click o refresh.

Recomendacion:
- Agregar validacion de duplicados (dueno+mascota) en backend.
- Deshabilitar boton de envio tras el primer submit.
- Usar redireccion Post/Redirect/Get (ya aplicado) y mensajes de exito para evitar reenvio.

## Conclusion
El formulario cumple validaciones basicas, pero se recomienda fortalecer formato de nombres, limites de peso y prevencion de duplicados para un estandar profesional.
