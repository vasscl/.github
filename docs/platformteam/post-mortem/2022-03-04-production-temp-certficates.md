> Template from: Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy. [“Site Reliability Engineering.”](https://landing.google.com/sre/book/chapters/postmortem.html).

# 2022-03-04-production-temp-kong-certificate

### Date

2022-03-04

### Authors

- Rodrigo Navarro
- Diego Mondini

### Status

- Resuelto

### Summary

Aproximadamente a las 08:00 AM se actualizo el ingress de kong pasando de un ingress nginx a un ingress-gce autoadministrado por Google. Al realizar esta actualizacion los certificados asociados quedaron actualizados, sin embargo la cadena de certificados no pudo ser resuelta por letsencrypt, dejando los challenge en un estado de pending devolviendo 404 sobre la url de confirmacion.

### Impact

- Las api expuestas por el cluster quedaron inaccesibles a traves del protocolo TLS. dejando a varios productos sin acceso ya que estan conectados exclusivamente por https.

### Root Causes

- No determinada, no se sabe porque Kong estaba resolviendo 404 para los challenges y el cert manager no pudo resolver.

### Trigger

- Actualizacion del ingress de Kong.

### Resolution

- Migrar las cargas de trabajo desde el cluster de production-temp al cluster de production-1

### Detection

- Sistema de alertas en discord.
- Cambio in situs del ingress.

## Action Items

- Migrate workloads to production-1 cluster.

## Lessons Learned

- Homologate cluster configuration to avoid custom changes that could break updates.

### What went well

- Migration was easy to accomplish.

### What went wrong

- Identify the miss function of cert manager took more time that expected, we could iomprove this making possible hot swapping for clusters.

### Where we got lucky

## Timeline

- 8:00 -> Replace ingress object for Kong.
- 10:00 -> cert manager Challenges failed with 404 (this is normal) but order was never successfull.
- 10:30 -> Start the migration to the production-1 cluster.
- 10:45 -> Workloads stopped by issue went back to normal as migration continuous.
- 13:00 -> End migration.
- 14:00 -> All systems up and running without issues.

## Supporting information

- Is normal that cert manager challenges fail with 404, but after 5 intents the challenge is resolved.
