import numpy as np


def generate_signal(n=100):
    t = np.linspace(0, 5, n)
    signal = np.sin(t)

    return signal


def noisy_sensor(signal, noise_std):
    noise = np.random.normal(0, noise_std, len(signal))

    return signal + noise


def fuse(sensor_a, sensor_b):
    return (sensor_a + sensor_b) / 2


def main():
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