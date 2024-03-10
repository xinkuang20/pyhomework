#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, mu, sigma):
    return np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))

# 定义参数
mu = 0
sigma = 1

# 生成x轴数据
x = np.linspace(-5, 5, 1000)

# 计算高斯分布
y = gaussian(x, mu, sigma)

# 绘制曲线
plt.plot(x, y, label=f"μ={mu}, σ={sigma}")
plt.xlabel('x')
plt.ylabel('Probability density')
plt.title('Gaussian Distribution')
plt.legend()
plt.grid(True)
plt.show()


# In[2]:


import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, mu, sigma):
    return np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))

# 定义参数
mu = 0       # 均值
sigma = 10    # 方差

# 生成x轴数据
x = np.linspace(-5, 5, 1000)

# 计算高斯分布
y = gaussian(x, mu, sigma)

# 绘制曲线
plt.plot(x, y, label=f"μ={mu}, σ={sigma}")
plt.xlabel('x')
plt.ylabel('Probability density')
plt.title('Gaussian Distribution')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:




