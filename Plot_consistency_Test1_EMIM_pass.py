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


#Gráficos com apenas EMIM:
data1=pd.read_excel('EMIM.xlsx', sheet_name='emimbf4_10_xiao', header=0, usecols='C,I', engine='openpyxl')
x1=data1['T [K]']
y1=data1['dT(T0T)']
x1=np.array(x1)
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

data4=pd.read_excel('EMIM.xlsx', sheet_name='emimcl_01_partoon', header=0, usecols='C,I', engine='openpyxl')
x4=data4['T [K]']
y4=data4['dT(T0T)']
x4=np.array(x4)
y4=np.array(y4)

data5=pd.read_excel('EMIM.xlsx', sheet_name='emimcl_05_partoon', header=0, usecols='C,I', engine='openpyxl')
x5=data5['T [K]']
y5=data5['dT(T0T)']
x5=np.array(x5)
y5=np.array(y5)

data6=pd.read_excel('EMIM.xlsx', sheet_name='emimcl_1_partoon', header=0, usecols='C,I', engine='openpyxl')
x6=data6['T [K]']
y6=data6['dT(T0T)']
x6=np.array(x6)
y6=np.array(y6)

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

data10=pd.read_excel('EMIM.xlsx', sheet_name='emimetso4_8_zare', header=0, usecols='C,I', engine='openpyxl')
x10=data10['T [K]']
y10=data10['dT(T0T)']
x10=np.array(x10)
y10=np.array(y10)

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

data16=pd.read_excel('EMIM.xlsx', sheet_name='emimno3_55_long', header=0, usecols='C,I', engine='openpyxl')
x16=data16['T [K]']
y16=data16['dT(T0T)']
x16=np.array(x16)
y16=np.array(y16)

data17=pd.read_excel('EMIM.xlsx', sheet_name='emimno3_10_long', header=0, usecols='C,I', engine='openpyxl')
x17=data17['T [K]']
y17=data17['dT(T0T)']
x17=np.array(x17)
y17=np.array(y17)

data18=pd.read_excel('EMIM.xlsx', sheet_name='emimno3_20_long', header=0, usecols='C,I', engine='openpyxl')
x18=data18['T [K]']
y18=data18['dT(T0T)']
x18=np.array(x18)
y18=np.array(y18)

data19=pd.read_excel('EMIM.xlsx', sheet_name='emimno3_30_long', header=0, usecols='C,I', engine='openpyxl')
x19=data19['T [K]']
y19=data19['dT(T0T)']
x19=np.array(x19)
y19=np.array(y19)

data20=pd.read_excel('EMIM.xlsx', sheet_name='emimno3_40_long', header=0, usecols='C,I', engine='openpyxl')
x20=data20['T [K]']
y20=data20['dT(T0T)']
x20=np.array(x20)
y20=np.array(y20)

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

plt.plot(x1,y1,'^', **opt, color='#ffa733') #emimbf4_10_xiao
plt.plot(x2,y2,'^', **opt, color='#ffa733') #emimbf4_10_kim
plt.plot(x3,y3,'^', **opt, color='#ffa733') #emimbf4_10_mardani
plt.plot(x4,y4,'o', **opt, color='#61bd20') #emimcl_01_partoon
plt.plot(x5,y5,'o', **opt, color='#61bd20') #emimcl_05_partoon
plt.plot(x6,y6,'o', **opt, color='#61bd20') #emimcl_1_partoon
plt.plot(x7,y7,'o', **opt, color='#ffa733') #emimcl_10_xiao
plt.plot(x8,y8,'o', **opt, color='#ffa733') #emimcl_10_long 
plt.plot(x9,y9,'o', **opt, color='#ffa733') #emimcl_10_chu
plt.plot(x10,y10,'s', **opt, color='#61bd20')  #emimetso4_8_zare
plt.plot(x11,y11,'s', **opt, color='#ffa733') #emimetso4_10_zare
plt.plot(x12,y12,'p', **opt, color='#ffa733') #emimhso4_10_zare
plt.plot(x13,y13,'d', **opt, color='#ffa733') #emimclo4_10_long
plt.plot(x14,y14,'h', **opt, color='#ffa733')  #emimscn_10_long
plt.plot(x15,y15,'H', **opt, color='#ffa733') #emimac_10_long
plt.plot(x16,y16,'p', **opt, color='#61bd20') #emimno3_55_long
plt.plot(x17,y17,'p', **opt, color='#ffa733') #emimno3_10_long
plt.plot(x18,y18,'p', **opt, color='#991c5e') #emimno3_20_long
plt.plot(x19,y19,'p', **opt, color='#991c5e') #emimno3_30long
plt.plot(x20,y20,'p', **opt, color='#991c5e')  #emimno3_40_long
plt.plot(x21,y21,'>', **opt, color='#ffa733') #emimdhp_10_sulaimon
plt.plot(x22,y22,'<', **opt, color='#ffa733') #emimi_10_li

plt.xlabel('Temperature [K]',fontproperties=font)
plt.ylabel('$\Delta$T/(T$_0$T)',fontproperties=font)
#plt.legend(loc="upper left")

plt.savefig('test1_EMIM_all.png',format='png',bbox_inches='tight',
                dpi=300,transparent=False)
plt.show()