#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

# set data
df = pd.DataFrame({
    'group': ['A','B','C','D'],
    'var1': [38,1.5,30,4],
    'var2': [29,10,9,34],
    'var3': [8,39,23,24],
    'var4': [7,31,33,14],
    'var5': [28,15,32,14]
})

# number of variable
categories = list(df)[1:]
N = len(categories)

# We are going to plot the first line of the data frame.
# But we need to repeat the first value to close the circular graph:
values = df.loc[0].drop('group').values.flatten().tolist()
#loc[0]으로 데이터 불러온 후 drop()을 사용해서 'group'제외
values += values[:1]    #원형 그래프를 닫아주기 위해 첫번째 값을 마지막에도 붙여줌
values

# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles [:1]
#원형그래프에 각도를 지정해 각을만들어줌

# Initialise the spider plot
ax = plt.subplot(111, polar = True)

# Draw one axe per variable + add labels labels yet #xticks = 밖에있는 데이터
plt.xticks(angles[:-1], categories, color = 'grey', size = 8)

# Draw ylabels
ax.set_rlabel_position(0)     #label이 출력되는 각도를 지정해줌
plt.yticks([10,20,30], ['10','20','30'], color = 'grey', size = 7)
plt.ylim(0,40)   #yticks = 안에있는 데이터, ylim = y축 범위제한

# Plot data (angles값에 values값을 넣음)
ax.plot(angles, values, linewidth = 1, linestyle = 'solid')

# Fill area (plot data로 그린 그래프를 채워줌)
ax.fill(angles, values, 'b', alpha = 0.1)

plt.show()


# In[2]:


list(df)
len(categories)
df.loc[0]
values[:1]
range(N)


# In[15]:


import matplotlib.font_manager as fm
font_path = 'C:\Windows\Fonts\HANBatang.ttf'
fontprop = fm.FontProperties(fname=font_path, size=20)


# In[99]:


# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

# number of variable
categories = list(df)
N = len(categories)

# We are going to plot the first line of the data frame.
# But we need to repeat the first value to close the circular graph:
values = df.loc['박수지'].values.flatten().tolist()
#loc[0]으로 데이터 불러온 후 drop()을 사용해서 'group'제외
values += values[:1]    #원형 그래프를 닫아주기 위해 첫번째 값을 마지막에도 붙여줌
values

# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles [:1]
#원형그래프에 각도를 지정해 각을만들어줌

# Initialise the spider plot
ax = plt.subplot(111, polar = True)

# Draw one axe per variable + add labels labels yet #xticks = 밖에있는 데이터
plt.xticks(angles[:-1], categories, color = 'grey', size = 8)

# Draw ylabels
ax.set_rlabel_position(0)     #label이 출력되는 각도를 지정해줌
plt.yticks([20,40,60,80], ['20','40','60','80'], color = 'grey', size = 7)
plt.ylim(0,100)   #yticks = 안에있는 데이터, ylim = y축 범위제한

# Plot data (angles값에 values값을 넣음)
ax.plot(angles, values, linewidth = 1, linestyle = 'solid', color = 'chartreuse')

# Fill area (plot data로 그린 그래프를 채워줌)
ax.fill(angles, values, 'olivedrab', alpha = 0.1)

plt.show()


# In[96]:


df = None
df = pd.read_csv('c:/python_data/MBTI.csv', encoding = 'euc - kr')
df = df[['NAME','E','N','T','J','I','S','F','P']]
df.set_index('NAME', inplace = True)
mbtiList = df.columns


# In[87]:


list(df)


# In[29]:


df.loc['박수지']


# In[26]:


len(categories)


# In[ ]:


mbtiList = ['E','N','T','J','I','S','F','P']
N = len(mbtiList)


# In[112]:


import matplotlib.pyplot as plt
import pandas as pd
from math import pi
import matplotlib.font_manager as fm
font_path = 'C:\Windows\Fonts\HANBatang.ttf'
fontprop = fm.FontProperties(fname = font_path, size = 10)

df= None
df= pd.read_csv('c:/python_data/MBTI.csv', encoding = 'euc-kr')
df= df[['NAME','E','N','T','J','I','S','F','P']]
df.set_index('NAME', inplace = True)
mbtiList = df.columns
N = len(mbtiList)

for name in df.index.values.tolist():
    values = df.loc[name].values.flatten().tolist()
    values += values[:1]
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
    
    fig = plt.gcf()
    plt.figure
    ax = plt.subplot(111, polar = True)
    plt.xticks(angles[:-1], mbtiList, color = 'grey', size =10)
    
    plt.ylim(0,100)
    
    ax.plot(angles, values, color = 'chartreuse', linewidth=1, linestyle='solid')
    ax.fill(angles, values, 'olivedrab', alpha = 0.1)
    plt.title(name, position=(0.25,1.0),fontproperties=fontprop)
    plt.show()
    plt.draw()
    figname = name + '.png'
    fig.savefig(figname, dpi = 1000)


# In[121]:


def saveMBTItoFig(name):
    df= None
    df= pd.read_csv('c:/python_data/MBTI.csv', encoding = 'euc-kr')
    df= df[['NAME','E','N','T','J','I','S','F','P']]
    df.set_index('NAME', inplace = True)
    mbtiList = df.columns
    N = len(mbtiList)
    values = df.loc[name].values.flatten().tolist()
    values += values[:1]
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    fig = plt.gcf()
    plt.figure
    ax = plt.subplot(111, polar = True)
    plt.xticks(angles[:-1], mbtiList, color = 'grey', size =10)

    plt.ylim(0,100)

    ax.plot(angles, values, color = 'chartreuse', linewidth=1, linestyle='solid')
    ax.fill(angles, values, 'olivedrab', alpha = 0.1)
    plt.title(name, position=(0.25,1.0),fontproperties=fontprop)
    plt.show()
    plt.draw()
    figname = name + '.png'
    fig.savefig(figname, dpi = 1000)


try:
    a = input('이름을 입력하세요.')
    saveMBTItoFig(a)
except:
    print('이름을 찾을 수 없습니다!')
    
    
    


# In[122]:


import numpy as np
arr = [1,2,3]
a = np.array([1,2,3])

print(arr)
print(a)
print(type(a))

arr = [(1,2,3),(4,5,6)]
a = np.array(arr, dtype=float)
print(a)


# In[123]:


a = np.zeros((3,4))   #0으로 채워진 3*4 배열생성
print(a)


# In[124]:


a = np.ones((3,4))    #1로 채워진 3*4 배열생성
print(a)


# In[127]:


a = np.full((3,4),5)
print(a)


# In[131]:


print(np.eye(4))
print(np.empty((4,2)))
print(np.empty((4,3)))


# In[137]:


a = np.linspace(0,1,5)
print(a)
plt.plot(a, 'v')
plt.show()


# In[138]:


mean = 0
std = 1
a = np.random.normal(mean,std,(2,3))
print(a)


# In[4]:


data = np.random.normal(0,1,100000)
plt.hist(data, bins=100)
plt.show()


# In[7]:


from selenium import webdriver
path = 'c://python_data//chromedriver.exe'
browser = webdriver.Chrome('c:/python_data/chromedriver.exe')
url = 'http://www.naver.com'
browser.get(url)


# In[ ]:




