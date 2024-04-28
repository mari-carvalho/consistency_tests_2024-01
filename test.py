import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

# Dados de exemplo
x = np.linspace(1, 10, 100)
y = np.exp(x) * 10**3

# Criando o gráfico
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y * 10^3')
plt.title('Gráfico com eixo y em escala logarítmica e valores inteiros no eixo y')

# Configurando o eixo y em escala logarítmica
plt.gca().set_yscale('log')
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useOffset=False))

plt.grid(True)
plt.show()