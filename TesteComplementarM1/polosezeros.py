import numpy as np
import matplotlib.pyplot as plt


zeros = np.array([1.0 + 0.0003j, 1.0 - 0.0003j, 1.0])
poles = np.array([0.8273, 0.7734 + 0.4283j, 0.7734 - 0.4283j])


fig, ax = plt.subplots(figsize=(8, 8))


ax.plot(np.real(zeros), np.imag(zeros), 
        'o',               
        markersize=10, 
        label='Zeros', 
        markeredgewidth=2, 
        markerfacecolor='none') 

ax.plot(np.real(poles), np.imag(poles), 
        'x',                
        markersize=10, 
        label='Polos', 
        markeredgewidth=2)


for i, p in enumerate(poles):
    if np.iscomplex(p):
        print(f"p{i+1} = {p.real:.4f} + j({p.imag:.4f})")
    else:
        print(f"p{i+1} = {p.real:.4f}")


unit_circle = plt.Circle((0, 0), 1, color='gray', linestyle='--', fill=False, linewidth=1.5)
ax.add_artist(unit_circle)

ax.set_title('Gráfico de Polos e Zeros no Plano-Z', fontsize=16)
ax.set_xlabel('Eixo Real', fontsize=12)
ax.set_ylabel('Eixo Imaginário', fontsize=12)
ax.axhline(0, color='black', linewidth=0.5) # Eixo x
ax.axvline(0, color='black', linewidth=0.5) # Eixo y
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend()
ax.set_aspect('equal', adjustable='box') 


ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

plt.show()

