README en [inglés](README.md)

# Modelado de Ruido de Sensores

Este repositorio explora modelos probabilísticos simples para el ruido de sensores, común en robótica y sistemas de percepción integrados.

Los ejemplos demuestran cómo se pueden modelar, filtrar y fusionar mediciones ruidosas para mejorar la estimación del estado.

## Contenido

- imu_noise_simulation.py

Simula el ruido gaussiano en lecturas de sensores inerciales.

- kalman_filter_1d.py

Implementación mínima de un filtro Kalman 1D para la estimación de señales.

- sensor_fusion_demo.py

Combina múltiples sensores ruidosos para estimar una señal latente.

## Objetivo

Estos experimentos ilustran conceptos relevantes para:

- Percepción robótica
- Estimación probabilística del estado
- Modelado de la incertidumbre de los sensores
