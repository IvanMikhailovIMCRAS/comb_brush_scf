import os 
import matplotlib.pyplot as plt
from comb_brush_scf import create_charge_brush
from comb_brush_scf import read_profile

create_charge_brush(N=100, sigma=0.05, alpha=0.1, phibulk=1e-3, n_layers=100)
os.system("./data/sfbox data/brush.in")

X = read_profile()

plt.plot(X[0], X[1])
plt.show()