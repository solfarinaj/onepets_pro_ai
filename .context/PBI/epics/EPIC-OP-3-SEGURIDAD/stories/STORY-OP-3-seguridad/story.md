# Story - Acceso y gestion en Django Admin (STORY-OP-3-seguridad)

## Historia de usuario
Como administrador, quiero ingresar al panel admin para gestionar usuarios y pacientes de forma segura.

## Descripcion funcional
- El panel admin requiere autenticacion.
- Usuarios con permisos acceden al listado de pacientes.
- El admin permite buscar pacientes por mascota o dueno.
- El admin permite gestionar usuarios (crear, editar, activar/desactivar).

## Criterios de aceptacion
- Acceso al admin solo con credenciales validas.
- Usuarios sin login son redirigidos a la pantalla de acceso.
- El admin muestra pacientes con columnas configuradas.
- El admin permite busqueda basica por mascota o dueno.
