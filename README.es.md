[English](README.md) | Español

# Modelado de Ruido de Sensores

Experimentos mínimos que ilustran el ruido probabilístico de sensores y la estimación de estado en sistemas robóticos.

Este repositorio explora modelos probabilísticos simples para el ruido de sensores, común en robótica y sistemas de percepción integrados.

Los ejemplos demuestran cómo se pueden modelar, filtrar y fusionar mediciones ruidosas para mejorar la estimación del estado.

## Contenido

El directorio `src/` contiene tres experimentos mínimos:

- `imu_noise_simulation.py`

Simula ruido gaussiano en lecturas de sensores inerciales.

- `kalman_filter_1d.py`

Implementación mínima de un filtro Kalman 1D para la estimación de señales.

- `sensor_fusion_demo.py`

Combina múltiples sensores ruidosos para estimar una señal latente.

## Propósito

Estos experimentos ilustran conceptos de ingeniería relevantes para:

- Percepción robótica
- Estimación probabilística del estado
- Modelado de la incertidumbre del sensor

## Motivación

Comprender la incertidumbre del sensor y el comportamiento basado en el estado es fundamental
para la robótica y los sistemas ciberfísicos, donde las mediciones reales son ruidosas y el comportamiento del sistema debe estructurarse bajo incertidumbre.

## Método

El repositorio implementa simulaciones probabilísticas simples del ruido del sensor
y procesos de estimación del estado comunes en la robótica y los sistemas de percepción embebidos.

Los experimentos incluyen:

- Simulación de ruido gaussiano en sensores inerciales
- Filtrado de Kalman para la estimación de señales
- Fusión básica de sensores en mediciones ruidosas

Estas implementaciones simplificadas buscan ilustrar las ideas centrales de la estimación probabilística del estado en sistemas ciberfísicos.

Estos ejemplos son intencionalmente minimalistas y están diseñados para resaltar el comportamiento conceptual de los filtros probabilísticos en lugar de los procesos de procesamiento de sensores de producción.

## Ejecución de los ejemplos

Clonar el repositorio y ejecutar cualquiera de los scripts:

```bash
git clone https://github.com/Jorge-de-la-Flor/sensor-uncertainty-lab
cd sensor-uncertainty-lab
python kalman_filter_1d.py
```

Cada script genera mediciones simuladas de sensores con ruido y visualiza el proceso de estimación de estado resultante.

## Ejemplo de salida

![Ejemplo de estimación de Kalman](assets/kalman_estimate.png)
![Ejemplo de simulación de ruido del sensor](assets/sensor_noise.png)

## Árbol del proyecto

```bash
sensor-uncertainty-lab
├─ .python-version
├─ README.es.md
├─ README.md
├─ assets
│ ├─ kalman_estimate.png
│ └─ sensor_noise.png
├─ pyproject.toml
├─ src
│ ├─ imu_noise_simulation.py
│ ├─ kalman_filter_1d.py
│ └─ sensor_fusion_demo.py
└─ uv.lock
```

## Requisitos

Los ejemplos utilizan:

- Python 3.12+
- NumPy
- Matplotlib

## Instalación

Instale las dependencias necesarias:

- usando `pip`

```bash
pip install numpy matplotlib
```

- usando `uv`

```bash
uv add numpy matplotlib
```

## Referencias

- Welch, G. y Bishop, G. (2006).
*Introducción al filtro de Kalman.*

- Thrun, S., Burgard, W. y Fox, D. (2005).
*Robótica probabilística.*
