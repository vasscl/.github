> Template from: Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy. [“Site Reliability Engineering.”](https://landing.google.com/sre/book/chapters/postmortem.html).

# 2022-01-10-github-key-sha1-not-supported

### Date

2022-01-10

### Authors

- Rodrigo Navarro
- Rodrigo Estrada

### Status

- Resuelto

### Summary

A las 09:01 PM todos los clusters que usan FluxV2 quedaron sin la capacidad de clonar repositorios arrojando el error **unable to clone 'ssh://git@github.com/Cencosud-x/x-clusters.git': unknown error: ERROR: You're using an RSA key with SHA-1, which is no longer allowed. Please use a newer client or a different key type.**

### Impact

- Equipos de producto quedaron sin la capacidad de actualizar sus manifiestos de despliegue automatizados.
- Equipo de plataforma quedo sin la capacidad de actualizar la configuración de los clusters de forma automatizada.

### Root Causes

- Github dejó de dar soporte a las llaves RSA SHA-1.

### Trigger

- Github deprecation key support.

### Resolution

- Actualización de la version de Flux Terraform module a la version 0.8.1.
- Generar nuevas claves cambiando el algoritmo de encriptación de RSA a ECDSA P256.

### Detection

- Sistema de alertas en discord
- Llamada de PagerDuty mediante uso de canal de incidentes en Discord

## Action Items

- Revisión de estado general de todos los recursos
- Reinstalaciñon de flux en los clusters.

## Lessons Learned

- Revisar las notas de deprecación de todos los sistemas que utilizamos para hacer el levantamiento correspondiente y resolver antes de que suceda.
- Se generó un calendario de actualización de versiones y deprecaciones de systemas y herramientas.

### What went well

- Las alertas
- Las gestión de incidentes por turnos

### What went wrong

- Falta de monitoreo

### Where we got lucky

- Nada, todo fue sistemático

## Timeline

- 21:01 -> Recibimos el incidente.
- 23:00 -> Se ejecutó la actualización del cluster staging-1.
- 23:10 -> Se probó la solución en el cluster de satging-1.
- 23:40 -> Se ejecutó la acutalización de los clusters production-temp y production-1.

## Supporting information
