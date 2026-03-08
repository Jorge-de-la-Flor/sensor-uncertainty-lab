"""
Sensor noise simulation using a simple sinusoidal signal.

This module generates a one-dimensional ground-truth signal, simulates noisy
sensor measurements by adding Gaussian noise, and visualizes both the true and
noisy signals using Matplotlib. The resulting plot is saved to
``sensor_noise.png`` instead of being shown interactively, which makes the
script suitable for headless environments such as WSL.
"""
import numpy as np
import matplotlib.pyplot as plt


def generate_true_signal(length=200):
    """
    Create a time vector and corresponding sinusoidal ground-truth signal
    """
    
    t = np.linspace(0, 10, length)
    signal = np.sin(t)

    return t, signal


def simulate_sensor(signal, noise_std=0.2):
    """
    Add Gaussian noise to a clean signal to emulate a noisy sensor
    measurement.
    """
    noise = np.random.normal(0, noise_std, size=len(signal))
    measurement = signal + noise

    return measurement


def main():
    """
    Orchestrate signal generation, noise simulation, and plotting, and save
    the resulting figure to disk.
    """
    np.random.seed(42)

    t, true_signal = generate_true_signal()
    measurement = simulate_sensor(true_signal)

    plt.plot(t, true_signal, label="True signal")
    plt.plot(t, measurement, label="Noisy measurement", alpha=0.6)

    plt.legend()
    plt.title("Sensor Noise Simulation")
    # plt.show()  # In WSL we don't have UI
    plt.savefig("sensor_noise.png")


if __name__ == "__main__":
    main()