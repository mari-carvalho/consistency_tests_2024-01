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


#Gráficos com apenas EMIM:
data1=pd.read_excel('EMIM.xlsx', sheet_name='emimbf4_10_xiao', header=0, usecols='C,I', engine='openpyxl') # header=0 indica que a primeira linha do arquivo deve ser usada como cabeçalho, nomes de colunas e os dados reais começam da segunda linha em diante 
x1=data1['T [K]'] # extrai as colunas correspondentes por seus nomes para o DataFrame data1  
y1=data1['dT(T0T)'] # data1 indica o DataFrame data1 que foi criado ao ler o arquivo Excel
x1=np.array(x1) # coloca esses dados do DataFrame data1 para dentro de matrizes 
y1=np.array(y1)

data2=pd.read_excel('EMIM.xlsx', sheet_name='emimbf4_10_kim', header=0, usecols='C,I', engine='openpyxl')
x2=data2['T [K]']
y2=data2['dT(T0T)']
x2=np.array(x2)
y2=np.array(y2)

data3=pd.read_excel('EMIM.xlsx', sheet_name='emimbf4_10_mardani', header=0, usecols='C,I', engine='openpyxl')
x3=data3['T [K]']
y3=data3['dT(T0T)']
x3=np.array(x3)
y3=np.array(y3)

data7=pd.read_excel('EMIM.xlsx', sheet_name='emimcl_10_xiao', header=0, usecols='C,I', engine='openpyxl')
x7=data7['T [K]']
y7=data7['dT(T0T)']
x7=np.array(x7)
y7=np.array(y7)

data8=pd.read_excel('EMIM.xlsx', sheet_name='emimcl_10_long', header=0, usecols='C,I', engine='openpyxl')
x8=data8['T [K]']
y8=data8['dT(T0T)']
x8=np.array(x8)
y8=np.array(y8)

data9=pd.read_excel('EMIM.xlsx', sheet_name='emimcl_10_chu', header=0, usecols='C,I', engine='openpyxl')
x9=data9['T [K]']
y9=data9['dT(T0T)']
x9=np.array(x9)
y9=np.array(y9)

data11=pd.read_excel('EMIM.xlsx', sheet_name='emimetso4_10_zare', header=0, usecols='C,I', engine='openpyxl')
x11=data11['T [K]']
y11=data11['dT(T0T)']
x11=np.array(x11)
y11=np.array(y11)

data12=pd.read_excel('EMIM.xlsx', sheet_name='emimhso4_10_zare', header=0, usecols='C,I', engine='openpyxl')
x12=data12['T [K]']
y12=data12['dT(T0T)']
x12=np.array(x12)
y12=np.array(y12)

data13=pd.read_excel('EMIM.xlsx', sheet_name='emimclo4_10_long', header=0, usecols='C,I', engine='openpyxl')
x13=data13['T [K]']
y13=data13['dT(T0T)']
x13=np.array(x13)
y13=np.array(y13)

data14=pd.read_excel('EMIM.xlsx', sheet_name='emimscn_10_long', header=0, usecols='C,I', engine='openpyxl')
x14=data14['T [K]']
y14=data14['dT(T0T)']
x14=np.array(x14)
y14=np.array(y14)

data15=pd.read_excel('EMIM.xlsx', sheet_name='emimac_10_long', header=0, usecols='C,I', engine='openpyxl')
x15=data15['T [K]']
y15=data15['dT(T0T)']
x15=np.array(x15)
y15=np.array(y15)

data17=pd.read_excel('EMIM.xlsx', sheet_name='emimno3_10_long', header=0, usecols='C,I', engine='openpyxl')
x17=data17['T [K]']
y17=data17['dT(T0T)']
x17=np.array(x17)
y17=np.array(y17)

data21=pd.read_excel('EMIM.xlsx', sheet_name='emimdhp_10_sulaimon', header=0, usecols='C,I', engine='openpyxl')
x21=data21['T [K]']
y21=data21['dT(T0T)']
x21=np.array(x21)
y21=np.array(y21)

data22=pd.read_excel('EMIM.xlsx', sheet_name='emimi_10_li', header=0, usecols='C,I', engine='openpyxl')
x22=data22['T [K]']
y22=data22['dT(T0T)']
x22=np.array(x22)
y22=np.array(y22)

plt.figure(figsize=(4,4))

plt.plot(x1,y1,'^', **opt, markerfacecolor='none', markeredgecolor='#d98218') #emimbf4_10_xiao
plt.plot(x2,y2,'P', **opt,  markerfacecolor='#d98218', markeredgecolor='k') #emimbf4_10_kim
plt.plot(x3,y3,'*', **opt, color='#d98218') #emimbf4_10_mardani
plt.plot(x7,y7,'o', **opt, color='#ffbb33') #emimcl_10_xiao
plt.plot(x8,y8,'o', **opt, color='#cc9629') #emimcl_10_long 
plt.plot(x9,y9,'o', **opt, color='#99701f') #emimcl_10_chu
plt.plot(x11,y11,'s', **opt, color='#5e2c85') #emimetso4_10_zare
plt.plot(x12,y12,'p', **opt, color='#9151c2') #emimhso4_10_zare
plt.plot(x13,y13,'d', **opt, color='#bf2a6d') #emimclo4_10_long
plt.plot(x14,y14,'h', **opt, color='#bf2a6d')  #emimscn_10_long
plt.plot(x15,y15,'H', **opt, color='#1c8077') #emimac_10_long
plt.plot(x17,y17,'p', **opt, color='#b8481c') #emimno3_10_long
plt.plot(x21,y21,'>', **opt, color='#188f52') #emimdhp_10_sulaimon
plt.plot(x22,y22,'<', **opt, color='#0d5932') #emimi_10_li

plt.xlabel('Temperature [K]',fontproperties=font)
plt.ylabel('$\Delta$T/(T$_0$T)',fontproperties=font)
#plt.legend(loc="upper left")

plt.savefig('test1_EMIM_10.png',format='png',bbox_inches='tight',
                dpi=300,transparent=False)
plt.show()