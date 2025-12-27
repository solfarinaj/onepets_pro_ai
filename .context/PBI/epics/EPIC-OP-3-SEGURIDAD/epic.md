# EPIC-OP-3-SEGURIDAD - Usuarios y Panel Administrativo

## Objetivo
Gestionar el acceso de usuarios y administrar pacientes usando el panel administrativo de Django.

## Alcance
- Acceso al panel admin para usuarios autorizados.
- Gestion de usuarios y permisos desde Django Admin.
- Gestion de pacientes en el admin (listado y busqueda basica).

## Fuera de alcance
- Autoregistro de usuarios.
- Recuperacion de password desde la app.
- Roles personalizados fuera de Django admin.

## Dependencias
- Registro de `Paciente` en `misapps/aplicacion1/admin.py`.
- Autenticacion de Django Admin.

## Riesgos
- Acceso no autorizado si no se controlan credenciales.
