from dataclasses import dataclass
from typing import Callable
import matplotlib.pyplot as plt


@dataclass
class Pod:
    name: str
    velocity_at: Callable[[float], float]

    def trajectory(self, total_time, dt):
        distance = 0
        points = [(0, 0)]
        for t in range(0, total_time, dt):
            v_t = self.velocity_at(t)
            v_t_plus_dt = self.velocity_at(t + dt)
            distance += ((v_t + v_t_plus_dt) / 2) * dt
            points.append((t + dt, distance))
        return points


racers = [
    Pod("Solid Performer", lambda t: t if t < 20 else 20),
    Pod("Slow Starter", lambda t: 0 if t < 30 else max(25, (t - 30) / 2)),
    Pod("To Infinity and Beyond", lambda t: t * 0.75),
    Pod("Jerky", lambda t: 15 if (t // 10) % 2 == 0 else -5),
    Pod("Goated", lambda t: 10 + 0.5 * t + 0.01 * t**30)
]


def print_trajectories(pods, total_time, dt):
    for pod in pods:
        print(f"Trajectory for {pod.name}:")
        for t, d in pod.trajectory(total_time, dt):
            print(f"  At t={t}s: {d}m")
        print()


def plot_trajectories(pods, total_time, dt):
    plt.figure(figsize=(10, 6))
    for pod in pods:
        times, distances = zip(*pod.trajectory(total_time, dt))
        plt.plot(times, distances, label=pod.name)
    plt.xlabel("Time (s)")
    plt.ylabel("Distance (m)")
    plt.title("Pod Racing Trajectories")
    plt.legend()
    plt.grid()
    plt.show()


plot_trajectories(racers, total_time=120, dt=1)
