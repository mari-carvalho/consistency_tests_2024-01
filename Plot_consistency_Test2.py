#Plot_consistency
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.font_manager import FontProperties
import pandas as pd
import numpy as np
 

matplotlib.rcParams['font.family'] = "Arial" # change the default font
matplotlib.rcParams['xtick.direction'] = 'in' # change the ticks direction
matplotlib.rcParams['ytick.direction'] = 'in'
font = FontProperties()
font.set_family('sans-serif') # 'serif', 'sans-serif', 'cursive', 'fantasy', or 'monospace'
font.set_name('Arial')
font.set_weight('bold') # 'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'
font.set_style('normal') #'normal', 'italic' or 'oblique'
font.set_size('x-large') # xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
opt = {'fillstyle':'full','markersize':5,'markeredgewidth':0.5, 'markeredgecolor':'k'}
plt.rcParams['figure.facecolor'] = (1.0,1.0,1.0,0.0)
plt.rcParams['axes.facecolor'] = '0.95'
#plt.rcParams['figure.figsize'] = (4,4)


#Gráficos com apenas EMIM e 10 wt%

data4=pd.read_excel('Consistency_exl.xlsx', sheet_name='EMIMCl10Xiao', header=0, usecols='J,K', engine='openpyxl')
x4=data4['1/T']
y4=data4['ln(P)']
x4=np.array(x4)
x4=1000*x4
y4=np.array(y4)

data6=pd.read_excel('Consistency_exl.xlsx', sheet_name='EMIMCl10Chu', header=0, usecols='J,K', engine='openpyxl')
x6=data6['1/T']
y6=data6['ln(P)']
x6=np.array(x6)
x6=1000*x6
y6=np.array(y6)

data10=pd.read_excel('Consistency_exl.xlsx', sheet_name='EMIMSCN10Long', header=0, usecols='J,K', engine='openpyxl')
x10=data10['1/T']
y10=data10['ln(P)']
x10=np.array(x10)
x10=1000*x10
y10=np.array(y10)

# pure water
x15=[0.00338, 0.00364]
x15=np.array(x15)
y15=-8813*x15 + 33.136
x15=1000*x15

plt.figure(figsize=(4,4))

plt.plot(x4,y4,'o', **opt, color='grey')
plt.plot(x6,y6,'o', **opt, color='red')
plt.plot(x10,y10,'<', **opt, color='magenta')
plt.plot(x15,y15, linewidth=1.0, color='black') 

plt.xlabel('1/T x $10^3$',fontproperties=font)
plt.ylabel('ln(P)',fontproperties=font)
#plt.legend(loc="upper left")

plt.savefig('test2_EMIM_bad.png',format='png',bbox_inches='tight',
                dpi=300,transparent=False)
plt.show()