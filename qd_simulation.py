# Quantum Dot Emission Simulator
import numpy as np
import matplotlib.pyplot as plt

qd_sizes = np.arange(2, 6, 0.5)  
emission_energy = 1240 / (qd_sizes**2)  

plt.figure(figsize=(8, 4))
plt.plot(qd_sizes, emission_energy, 'bo-')
plt.xlabel("Quantum Dot Size (nm)")
plt.ylabel("Emission Energy (eV)")
plt.title("Smaller Quantum Dots Emit Higher-Energy (Bluer) Light")
plt.grid(True)
plt.show()
