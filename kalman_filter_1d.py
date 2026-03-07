import numpy as np


class KalmanFilter1D:
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