"""
1D sensor fusion example with noisy sinusoidal data.

This module generates a one-dimensional sinusoidal "true" signal, simulates two
independent noisy sensors with different noise levels, and fuses their
measurements by averaging. It then prints a few sample triplets of
(sensor1, sensor2, fused) values to illustrate how combining multiple noisy
measurements can reduce overall noise.
"""
import numpy as np


def generate_signal(n=100):
    """
    Generate a sinusoidal signal of length ``n`` over a fixed time interval.
    """
    t = np.linspace(0, 5, n)
    signal = np.sin(t)

    return signal


def noisy_sensor(signal, noise_std):
    """
    Add Gaussian noise with standard deviation ``noise_std`` to a clean
    input signal to emulate a noisy sensor.
    """
    noise = np.random.normal(0, noise_std, len(signal))

    return signal + noise


def fuse(sensor_a, sensor_b):
    """
    Fuse two sensor signals by taking their pointwise arithmetic mean.
    """
    return (sensor_a + sensor_b) / 2


def main():
    """
    Run a demonstration: generate the true signal, simulate two noisy
    sensors, fuse their readings, and print the first few samples.
    """
    np.random.seed(42)

    true_signal = generate_signal()

    sensor1 = noisy_sensor(true_signal, 0.3)
    sensor2 = noisy_sensor(true_signal, 0.6)

    fused = fuse(sensor1, sensor2)

    for i in range(10):
        print(
            f"s1={sensor1[i]:.3f} "
            f"s2={sensor2[i]:.3f} "
            f"fused={fused[i]:.3f}"
        )


if __name__ == "__main__":
    main()