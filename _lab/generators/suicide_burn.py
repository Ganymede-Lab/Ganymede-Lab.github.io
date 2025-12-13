import numpy as np
import matplotlib.pyplot as plt
import os

output_dir = "../raw_images"
os.makedirs(output_dir, exist_ok=True)

def altitude(t):
    return 4*t**2 - 80*t + 400

t = np.linspace(0, 10, 100)
h = altitude(t)

plt.figure(figsize=(10, 6))
plt.plot(t, h, label=r'Rocket Altitude: $h(t) = 4t^2 - 80t + 400$', color='#1f77b4', linewidth=2.5)

plt.axvspan(5, 8, color='orange', alpha=0.2, label='Suicide Burn Window')
plt.scatter([5, 8], [altitude(5), altitude(8)], color='red', zorder=5)
plt.text(5.1, altitude(5), f'Start Burn\n{int(altitude(5))}m', fontsize=10)
plt.text(8.1, altitude(8), f'Touchdown\n{int(altitude(8))}m', fontsize=10)

plt.title('SpaceX Falcon 9: Suicide Burn Profile', fontsize=14)
plt.xlabel('Time (seconds)', fontsize=12)
plt.ylabel('Altitude (meters)', fontsize=12)
plt.axhline(0, color='black', linewidth=1)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

output_path = os.path.join(output_dir, 'suicide_burn_plot.png')
plt.savefig(output_path)
print(f"Graph generated at: {output_path}")
