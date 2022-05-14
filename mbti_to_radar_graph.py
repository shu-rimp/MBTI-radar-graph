#!/usr/bin/env python
# coding: utf-8

# In[15]:


import matplotlib.font_manager as fm
font_path = 'C:/Windows/Fonts/HANBatang.ttf'
fontprop = fm.FontProperties(fname=font_path, size=20)


# In[96]: csv로 불러온 데이터 확인
df = None
df = pd.read_csv('C:/Users/suzi/Downloads/MBTI.csv', encoding = 'euc - kr')
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

# In[121]:


def saveMBTItoFig(name):
    df= None
    df= pd.read_csv('C:/Users/suzi/Downloads/MBTI.csv', encoding = 'euc-kr')
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