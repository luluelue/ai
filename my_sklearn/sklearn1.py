from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.preprocessing import MinMaxScaler, StandardScaler

import jieba


def dictven():
    # 这个DictVectorizer默认会将字典转化为sparse矩阵，节约内存，（即使用三元组来表示稀疏矩阵）
    # dict = DictVectorizer()
    dict = DictVectorizer(sparse=False)
    data = dict.fit_transform(
        [{"city": "北京", "temperature": 35}, {"city": "上海", "temperature": 23}, {"city": "杭州", "temperature": 12}])
    # 打印出抽取的特征值
    print(dict.get_feature_names())

    print(data)
    pass


# 将中文分词为空格隔开的句子
def cut_chinese():
    str1 = "另外值得一提的是Memcache的内存hash表所特有的Expires数据过期淘汰机制，正好和Session的过期机制不谋而合，降低了 过期Session数据删除的代码复杂度，对比“基于数据库的存储方案”，仅这块逻辑就给数据表产生巨大的查询压力。"
    str2 = "Memcache由于是一款基于Libevent多路异步I/O技术的内存共享系统，简单的Key + Value数据存储模式使得代码逻辑小巧高效，因此在并发处理能力上占据了绝对优势，目前本人所经历的项目达到2000/秒 平均查询，并且服务器CPU消耗依然不到10%。"
    str3 = "这个方案的优点无需额外的服务器资源；缺点是由于受http协议头信心长度的限制，仅能够存储小部分的用户信息，同时Cookie化的 Session内容需要进行安全加解密（如：采用DES、RSA等进行明文加解密；再由MD5、SHA-1等算法进行防伪认证），另外它也会占用一定的带 宽资源，因为浏览器会在请求当前域名下任何资源时将本地Cookie附加在http头中传递到服务器。"
    strs1 = " ".join(list(jieba.cut(str1)))
    strs2 = " ".join(list(jieba.cut(str2)))
    strs3 = " ".join(list(jieba.cut(str3)))
    return strs1, strs2, strs3


def counter():
    cv = CountVectorizer()
    data = cv.fit_transform(["from sklearn.feature_extraction.text import from CountVectorizer",
                             "from sklearn.feature_extraction import aa DictVectorizer aa",
                             "Process finished with exit code 0"])

    print(data)
    print(cv.get_feature_names())
    print(data.toarray())


# 将中文进行特征抽取
def counter_chinese():
    cv = CountVectorizer()
    data = cv.fit_transform(cut_chinese())
    print(cv.get_feature_names())
    print(data.toarray())


# Tfidf方式进行特征抽取 tf*idf 得到权重（与es中的tfidf 相同，tf指的是词频，idf指的是 log(总文档数/该词出现的文档数） ）
def tfidfvec():
    tf = TfidfVectorizer()
    data = tf.fit_transform(cut_chinese())
    print(tf.get_feature_names())
    print(data.toarray())


# 归一化处理
def mm():
    mm = MinMaxScaler()
    data = mm.fit_transform([[90, 2, 10, 40], [85, 15, 16, 43], [91, 58, 27, 35]])
    print(data)

# 标准化处理（数据的预处理最常用） 公式：x-mean/a    a 为标准差，mean为均值
def stand():
    std = StandardScaler()
    data = std.fit_transform([[8, 4, 6, 3], [6, 9, 5, 7], [5, 1, 8, 6]])
    print(data)


if __name__ == "__main__":
    # dictven()
    # counter()
    # counter_chinese()
    # tfidfvec()
    # mm()
    stand()
