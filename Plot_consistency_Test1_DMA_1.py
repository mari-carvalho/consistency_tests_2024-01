#Plot_consistency
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.font_manager import FontProperties
import pandas as pd
import numpy as np
 

matplotlib.rcParams['font.family'] = "Arial" # change the default font # mudança da fonte 
matplotlib.rcParams['xtick.direction'] = 'in' # change the ticks direction # mudança da direção dos marcadores ao longo dos eixos de um gráfico que indicam valores específicos 
matplotlib.rcParams['ytick.direction'] = 'in'
font = FontProperties() # cria uma instância de propriedades de fontes, tamanho, estilo e família
font.set_family('sans-serif') # 'serif', 'sans-serif', 'cursive', 'fantasy', or 'monospace' # família da fonte 
font.set_name('Arial') # nome da fonte 
font.set_weight('bold') # 'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black' # peso da fonte 
font.set_style('normal') #'normal', 'italic' or 'oblique' # estilo da fonte, negrito, itálico, normal, etc 
font.set_size('x-large') # xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large' # tamanho da fonte 
plt.rcParams['figure.dpi'] = 300 # resolução padrão para as figuras exibidas na tela 
plt.rcParams['savefig.dpi'] = 300 # resolução padrão para as figuras salvas em arquivos PNG, PDF ou SVG 
opt = {'fillstyle':'full','markersize':5,'markeredgewidth':0.5} # aparência dos marcadores, fillstyle: full - estilo de preenchimento markersize: 5 - tamanho do marcador markeredgewidth: 0.5 largura da borda do marcador 
plt.rcParams['figure.facecolor'] = (1.0,1.0,1.0,0.0) # cor de fundo da figura como transparente 
plt.rcParams['axes.facecolor'] = '0.95' # cor de fundo dos eixos como uma tonalidade de cinza claro 
#plt.rcParams['figure.figsize'] = (4,4) # tamanho da figura padrão em polegadas 

x_array = []
y_array = []
#Gráficos com apenas DMA:
data1=pd.read_excel('DMA.xlsx', sheet_name='dmaof_5_altamash', header=0, usecols='C,I', engine='openpyxl') # header=0 indica que a primeira linha do arquivo deve ser usada como cabeçalho, nomes de colunas e os dados reais começam da segunda linha em diante 
x1=data1['T [K]'] # extrai as colunas correspondentes por seus nomes para o DataFrame data1  
y1=data1['dT(T0T)'] # data1 indica o DataFrame data1 que foi criado ao ler o arquivo Excel
x1=np.array(x1) # coloca esses dados do DataFrame data1 para dentro de matrizes 
y1=np.array(y1)

data1=pd.read_excel('DMA.xlsx', sheet_name='dmaof_10_altamash', header=0, usecols='C,I', engine='openpyxl') # header=0 indica que a primeira linha do arquivo deve ser usada como cabeçalho, nomes de colunas e os dados reais começam da segunda linha em diante 
x2=data1['T [K]'] # extrai as colunas correspondentes por seus nomes para o DataFrame data1  
y2=data1['dT(T0T)'] # data1 indica o DataFrame data1 que foi criado ao ler o arquivo Excel
x2=np.array(x2) # coloca esses dados do DataFrame data1 para dentro de matrizes 
y2=np.array(y2)

for i in range(2):
    if i == 0:
        x_array.append(x1)
        y_array.append(y1)
    else: 
        x_array.append(x2)
        y_array.append(y2)

print('x_array', x_array)
print('y_array', y_array)

plt.figure(figsize=(4,4))

# Vetor de símbolos
symbols = ['o', 's', '^', 'D', 'v', '>', '<', 'P', 'X', 'H']  # Exemplos de símbolos

# Vetor de cores
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']  # Exemplos de cores

for i in range(len(x_array)):
    x = x_array[i]
    y = y_array[i]
    for j in range(len(symbols)):
        symbol=symbols[i]
        color=colors[i]
        plt.plot(x,y,marker=symbol, color=color, linestyle='none')

plt.xlabel('Temperature [K]',fontproperties=font)
plt.ylabel('$\Delta$T/(T$_0$T)',fontproperties=font)
#plt.legend(loc="upper left")

plt.savefig('test1_EMIM_10.png',format='png',bbox_inches='tight',
                dpi=300,transparent=False)
plt.show()     