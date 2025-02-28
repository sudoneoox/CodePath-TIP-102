from typing import Dict


def detect_temporal_anomaly(time_points, k):
    time_delta: Dict = {}

    for i, time in enumerate(time_points):
        if time in time_delta:
            if i - time_delta[time] <= k:
                return True
        time_delta[time] = i

    return False


time_points1 = [1, 2, 3, 1]
k1 = 3

time_points2 = [1, 0, 1, 1]
k2 = 1

time_points3 = [1, 2, 3, 1, 2, 3]
k3 = 2

print(detect_temporal_anomaly(time_points1, k1))
print(detect_temporal_anomaly(time_points2, k2))
print(detect_temporal_anomaly(time_points3, k3))
