# Casos de Prueba - Seguridad y Admin (STORY-OP-3-seguridad)

## Criterios de prioridad y severidad
- Prioridad: Alta, Media, Baja.
- Severidad: Critica, Mayor, Menor.

## TC-SEC-01 Acceso bloqueado sin login
Precondiciones:
- No hay sesion activa.

Pasos:
1) Ir a /admin/.

Resultado esperado:
- El sistema redirige a la pantalla de login del admin.

Prioridad: Alta
Severidad: Mayor

## TC-SEC-02 Login valido en admin
Precondiciones:
- Existe un usuario administrador con credenciales validas.

Pasos:
1) Ir a /admin/.
2) Ingresar credenciales validas.

Resultado esperado:
- El usuario accede al dashboard de admin.

Prioridad: Alta
Severidad: Critica

## TC-SEC-03 Login invalido en admin
Precondiciones:
- Existe un usuario administrador.

Pasos:
1) Ir a /admin/.
2) Ingresar credenciales invalidas.

Resultado esperado:
- El sistema muestra error de autenticacion y no permite acceso.

Prioridad: Alta
Severidad: Mayor

## TC-SEC-04 Listado de pacientes en admin
Precondiciones:
- Existe al menos un paciente registrado.
- Usuario administrador autenticado.

Pasos:
1) Ir a /admin/.
2) Entrar a la seccion de Pacientes.

Resultado esperado:
- Se muestra listado con columnas ID, mascota, dueno, especie y fecha_registro.

Prioridad: Media
Severidad: Menor

## TC-SEC-05 Busqueda en admin por mascota o dueno
Precondiciones:
- Existe paciente con mascota "Nina".
- Usuario administrador autenticado.

Pasos:
1) Ir a /admin/.
2) Entrar a Pacientes.
3) Usar el buscador con "Nina".

Resultado esperado:
- Se muestran resultados que coinciden con mascota o dueno.

Prioridad: Media
Severidad: Menor
