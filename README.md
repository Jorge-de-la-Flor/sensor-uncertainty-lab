README in [Spanish](README.es.md)

# Sensor Noise Modeling

This repository explores simple probabilistic models for sensor noise
commonly encountered in robotics and embedded perception systems.

The examples demonstrate how noisy measurements can be modeled,
filtered, and fused to improve state estimation.

## Contents

- imu_noise_simulation.py

    Simulates Gaussian noise in inertial sensor readings.

- kalman_filter_1d.py

    Minimal implementation of a 1D Kalman filter for signal estimation.

- sensor_fusion_demo.py

    Combines multiple noisy sensors to estimate a latent signal.

## Purpose

These experiments illustrate concepts relevant to:

- robotics perception
- probabilistic state estimation
- sensor uncertainty modeling
