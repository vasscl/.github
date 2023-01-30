> Template from: Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy. [“Site Reliability Engineering.”](https://landing.google.com/sre/book/chapters/postmortem.html).

# 2022-01-07-production-temp-api-404

### Date

2022-01-07

### Authors

- Rodrigo Navarro
- Rodrigo Estrada

### Status

- Resuelto

### Summary

Aproximadamente a las 12:00 AM todas las API's del cluster **production-temp** bajo el dominio **api.cencosudx.io** comenzaron a responder con estado **404**

### Impact

- Usuarios de la aplicación **Mi Mall** comenzaron a tener problemas con el pago automático del estacionamiento y las cercas de control de acceso no se abrían.
- La mayor parte de la aplicación **Mi Mall** no estaba operativa

### Root Causes

- Actualización automática de la versión del api gateway **Kong Ingress** a traves del controlador de helm de flux
- Versión del helm chart no estaba fija permitiendo actualizaciones de minors

### Trigger

- PR para solucionar un issue grave en la comunidad de kong ingress

### Resolution

- Actualización de kong-ingress a la última versión

### Detection

- Sistema de alertas en discord
- Llamada de PagerDuty mediante uso de canal de incidentes en Discord

## Action Items

- Revisión de estado general de todos los recursos
- Revisión de todos los eventos de las últimas horas
- Revisión de los cambios realizados en el cluster
- Revisión de nuestros sistemas de despliegue de aplicaciones
  - Actualización de versión con problemas al encontrar inconsistencias en el log
  - Revisión de pr de la comunidad de kong ingress
- Lunes 01/08 -> Implementación de Instana

## Lessons Learned

- Subestimamos el monitoreo y noes demoramos demasiado en implementarlo debido a una discusión de presupuesto. El monitoreo debe ir desde el primer día de producción.
- Helm chart es complejo en caso de emergencia. Es mejor fijar versiones y depender de un sistema dinámico de alertas de vulnerabilidades para desplegar las actualizaciones minor en forma controlada. Los parches pueden seguir automáticos.

### What went well

- Las alertas
- Las gestión de incidentes por turnos

### What went wrong

- Falta de monitoreo

### Where we got lucky

- Nada, todo fue sistemático

## Timeline

- 12:40 -> Recibimos el incidente
- 13:30 -> Hipótesis de causas
- 13:45 -> plan de solución
- 14:00 -> Solución en producción y probada
## Supporting information
