#!/usr/bin/env python
# coding: utf-8

# In[2]:


import jieba
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
def read_file(file_path):
    """
    读取文件，一行一句为单位，返回包含每一行文本的列表
    """
    lines = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                lines.append(line.strip())  
    except FileNotFoundError:
        print("文件未找到！")
    return lines

def load_stopwords(stopwords_file):
    """
    加载停用词列表
    """
    stopwords = set()
    try:
        with open(stopwords_file, 'r', encoding='utf-8') as file:
            for line in file:
                stopwords.add(line.strip())
    except FileNotFoundError:
        print("停用词文件未找到！")
    return stopwords

def tokenize_and_count(lines, stopwords):
    """
    使用jieba对文档进行分词，并统计词频，同时过滤停用词
    """
    # 分词并将结果存储在列表中
    tokens = []
    for line in lines:
        words = jieba.cut(line)  # 使用jieba进行分词
        for word in words:
            if word not in stopwords:  # 过滤停用词
                tokens.append(word)
    
    # 统计词频
    word_counts = Counter(tokens)
    
    return word_counts

def generate_wordcloud(word_counts, title):
    """
    生成词云图
    """
    # 生成词云图
    wordcloud = WordCloud(font_path='simhei.ttf', width=800, height=400, background_color='white').generate_from_frequencies(word_counts)

    # 显示词云图
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(title)
    plt.axis('off') 
    plt.show()

# 读取文件内容
file_path = "D:\\python homework\\week2.txt"
lines = read_file(file_path)

# 加载停用词列表
stopwords_file = "D:\\python homework\\stopword.txt"
stopwords = load_stopwords(stopwords_file)

# 对文档进行分词并统计词频
word_counts = tokenize_and_count(lines, stopwords)

# 生成高频词的词云图
generate_wordcloud(word_counts, "高频词词云图")


# In[4]:


import jieba
import jieba.posseg as pseg
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
def read_file(file_path):
    """
    读取文件，一行一句为单位，返回包含每一行文本的列表
    """
    lines = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                lines.append(line.strip())  
    except FileNotFoundError:
        print("文件未找到！")
    return lines

def load_stopwords(stopwords_file):
    """
    加载停用词列表
    """
    stopwords = set()
    try:
        with open(stopwords_file, 'r', encoding='utf-8') as file:
            for line in file:
                stopwords.add(line.strip())
    except FileNotFoundError:
        print("停用词文件未找到！")
    return stopwords

def tokenize_and_count(lines, stopwords):
    """
    使用jieba对文档进行分词，并统计词频，同时过滤停用词
    """
    # 分词并将结果存储在列表中
    tokens = []
    for line in lines:
        words = pseg.cut(line)  # 使用jieba进行分词和词性标注
        for word, flag in words:
            if flag.startswith('v') and word not in stopwords:  # 选择动词
                tokens.append(word)
    
    # 统计词频
    word_counts = Counter(tokens)
    
    return word_counts

def generate_wordcloud(word_counts, title):
    """
    生成词云图
    """
    # 生成词云图
    wordcloud = WordCloud(font_path='simhei.ttf', width=800, height=400, background_color='white').generate_from_frequencies(word_counts)

    # 显示词云图
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(title)
    plt.axis('off')  # 不显示坐标轴
    plt.show()

# 读取文件内容
file_path = "D:\\python homework\\week2.txt"
lines = read_file(file_path)

# 加载停用词列表
stopwords_file = "D:\\python homework\\stopword.txt"
stopwords = load_stopwords(stopwords_file)

# 对文档进行分词并统计动词频率
verb_word_counts = tokenize_and_count(lines, stopwords)

# 生成动词高频词的词云图
generate_wordcloud(verb_word_counts, "动词高频词词云图")


# In[5]:


import jieba
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def read_file(file_path):
    """
    读取文件，一行一句为单位，返回包含每一行文本的列表
    """
    lines = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                lines.append(line.strip()) 
    except FileNotFoundError:
        print("文件未找到！")
    return lines

def tokenize_and_count(lines):
    """
    使用jieba对文档进行分词，并统计bigram词频
    """
    # 分词并将结果存储在列表中
    tokens = []
    for line in lines:
        words = jieba.lcut(line)  # 使用jieba进行分词
        for i in range(len(words)-1):
            tokens.append((words[i], words[i+1]))
    
    # 统计bigram词频
    bigram_counts = Counter(tokens)
    
    # 对词频进行排序
    sorted_bigram_counts = sorted(bigram_counts.items(), key=lambda x: x[1], reverse=True)
    
    # 输出前20个高频bigram
    print("前20个高频bigram：")
    for bigram, count in sorted_bigram_counts[:20]:
        print(f"{bigram}: {count}")
    
    return sorted_bigram_counts

def generate_wordcloud(word_counts, title):
    """
    生成词云图
    """
    # 提取高频的bigram和对应的频率
    bigrams = [item[0] for item in word_counts]
    frequencies = [item[1] for item in word_counts]
    
    # 将bigrams转换为字符串
    bigram_strings = [' '.join(bigram) for bigram in bigrams]
    
    # 将bigrams和frequencies组合成字典
    bigram_freq_dict = dict(zip(bigram_strings, frequencies))
    
    # 生成词云图
    wordcloud = WordCloud(font_path='simhei.ttf', width=800, height=400, background_color='white').generate_from_frequencies(bigram_freq_dict)

    # 显示词云图
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(title)
    plt.axis('off')  # 不显示坐标轴
    plt.show()


# 读取文件内容
file_path = "D:\\python homework\\week2.txt"
lines = read_file(file_path)

# 对文档进行分词并统计bigram词频
sorted_bigram_counts = tokenize_and_count(lines)

# 生成高频bigram的词云图
generate_wordcloud(sorted_bigram_counts, "高频Bigram词云图")


# In[ ]:




