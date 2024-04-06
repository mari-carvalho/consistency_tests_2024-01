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


#Gráficos com apenas DEA:
data1=pd.read_excel('DEA.xlsx', sheet_name='deahso4_1_gupta', header=0, usecols='C,I', engine='openpyxl') # header=0 indica que a primeira linha do arquivo deve ser usada como cabeçalho, nomes de colunas e os dados reais começam da segunda linha em diante 
x1=data1['T [K]'] # extrai as colunas correspondentes por seus nomes para o DataFrame data1  
y1=data1['dT(T0T)'] # data1 indica o DataFrame data1 que foi criado ao ler o arquivo Excel
x1=np.array(x1) # coloca esses dados do DataFrame data1 para dentro de matrizes 
y1=np.array(y1)

plt.figure(figsize=(4,4))

plt.plot(x1,y1,'^', **opt, markerfacecolor='none', markeredgecolor='#d98218') #emimbf4_10_xiao

plt.xlabel('Temperature [K]',fontproperties=font)
plt.ylabel('$\Delta$T/(T$_0$T)',fontproperties=font)
#plt.legend(loc="upper left")

plt.savefig('test1_EMIM_10.png',format='png',bbox_inches='tight',
                dpi=300,transparent=False)
plt.show()