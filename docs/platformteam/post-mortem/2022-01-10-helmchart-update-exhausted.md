> Template from: Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy. [“Site Reliability Engineering.”](https://landing.google.com/sre/book/chapters/postmortem.html).

# 2022-01-10-helmchart-update-exhausted

### Date

2022-01-10

### Authors

- Rodrigo Navarro
- Rodrigo Estrada

### Status

- No Resuelto

### Summary

A partir del incidente [2022-01-10-github-key-sha1-not-supported](2022-01-10-github-key-sha1-not-supported.md) los clusters de production-temp y production-1 no pueden actualizar los helm charts de tools, presentando el error **"Helm upgrade failed: ano │
│ ther operation (install/upgrade/rollback) is in progress**

### Impact

- Equipo de plataforma quedo sin la capacidad de actualizar la configuración de los las herramientas en los lusters de forma automatizada.

### Root Causes

- Actualizaci'on de Flux en los cluster genero conflicto con las instalaciones previas de los helm charts.

### Trigger

- Actualizacion de Flux en los clusters.

### Resolution

### Detection

- In situ.

## Action Items

## Lessons Learned

### What went well

### What went wrong

### Where we got lucky

## Timeline

- 23:40 -> Los clusters production-temp y production-1 presentaron el error en el helm controller tanto de flux-system como de flux-deployment.

## Supporting information
