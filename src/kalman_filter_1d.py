"""
One-dimensional Kalman filter example for noisy scalar measurements.

This module implements a minimal 1D Kalman filter to estimate a constant
underlying value from noisy measurements, using NumPy for random number
generation. It demonstrates the standard predict–update cycle of the Kalman
filter and prints both the raw measurements and the corresponding filtered
estimates to the console.
"""
import numpy as np
import matplotlib.pyplot as plt

class KalmanFilter1D:
    """
    One-dimensional Kalman filter with scalar state, covariance,
    process noise variance, and measurement noise variance.
    """
    
    def __init__(self, process_var, measurement_var):
        self.x = 0
        self.P = 1
        self.Q = process_var
        self.R = measurement_var

    def predict(self):
        self.P = self.P + self.Q

    def update(self, measurement):
        K = self.P / (self.P + self.R)

        self.x = self.x + K * (measurement - self.x)
        self.P = (1 - K) * self.P

        return self.x


def simulate():
    """
    Generate synthetic noisy measurements of a constant true value, run the
    Kalman filter over them, and return both the measurements and the
    filtered estimates.
    """
    np.random.seed(42)
    
    true_value = 5
    measurements = true_value + np.random.normal(0, 1, 50)
    
    kf = KalmanFilter1D(0.01, 1)
    
    estimates = []

    for z in measurements:
        kf.predict()
        estimate = kf.update(z)
        
        estimates.append(estimate)

    return measurements, estimates


if __name__ == "__main__":
    measurements, estimates = simulate()

    for m, e in zip(measurements, estimates):
        print(f"measurement={m:.2f} estimate={e:.2f}")
    
    plt.plot(measurements, label="Measurements", alpha=0.6)
    plt.plot(estimates, label="Kalman estimate")

    plt.legend()
    plt.title("Kalman Filter Estimation")
    plt.savefig("kalman_estimate.png")