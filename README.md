## 概述  
Jobs-Recommendation-System使用Scrapy爬虫框架对招聘网站进行爬取，并使用ETL工具将数据存储到分布式文件系统；利用大数据，机器学习等技术对求职者和职位信息进行画像建模，并通过推荐算法对求职者做出职位的智能推荐。  

## 系统设计框架  
* **前期设计框架**：  
  * 使用3台云服务器进行大数据平台的搭建，其中master节点作为主节点，其他2台服务器作为slave节点，平台主要安装和使用Hadoop,Spark,Hbase,Hive等工具。
  * 在master节点上通过python开源框架Scrapy将前程无忧网(jobs.51job.com)的职位数据爬取到master节点的MySQL数据库中进行存储，之后通过sqoop工具将数据抽取转换到Hbase数据库中。
  * 通过spark计算框架对hbase中的职位数据进行分析批处理，并将结果存储到Hbase数据库中。
  * 对用户的接口使用的是python开源框架Django的web网页，当用户需要推荐时，通过web端发起请求，之后响应程序使用推荐算法做出推荐并返回给用户。
  基本设计框架图如下：
<div align=center>
  <img src="https://github.com/efishliu/Jobs-Recommendation-System/blob/master/image/%E7%BB%98%E5%9B%BE1.jpg?raw=true" width = 60% height = 60% />
</div>   

* **后期设计框架**： ~~(未构建完成)~~  
  * 使用4台云服务器，在存储端使用MySQL,HDFS,HBase3种存储方式，计算框架采用Spark

## 系统主要功能模块的实现  
* **大数据平台的设计与搭建**  
  * [Hadoop平台搭建说明](https://github.com/efishliu/Jobs-Recommendation-System/blob/master/Hadoop/Hadoop%20Installtion%20Description.md)

* **基于Scrapy的爬虫实现**  
    * **基于单机的爬虫实现：** 在master节点上将数据爬取到MySQL数据库中并通过sqoop工具导入大数据平台。其中单机爬虫实现的源代码项目：[jobs](https://github.com/efishliu/Jobs-Recommendation-System/tree/master/Scrapy/jobs)，MySQL数据库建表SQL：[all_posts_data.sql](https://github.com/efishliu/Jobs-Recommendation-System/blob/master/Scrapy/all_posts_data.sql)。  
    需要安装*anconda3,scrapy,mysql,mysql-server,pymysql*模块。  
    参考文档：[Scrapy Document](https://scrapy.org/doc/)，[《精通python爬虫框架Scrapy》](https://github.com/efishliu/Jobs-Recommendation-System/tree/master/scrapybook)  
    * **基于分布式的爬虫实现：** 
      * 在master节点上整理爬取逻辑和去重工作，将需要爬取网页的url存入Redis共享队列中。 [master爬虫程序](https://github.com/efishliu/Jobs-Recommendation-System/tree/master/Scrapy/master/master)  
      * 3台slave节点从master节点的Redis共享队列中获取需要爬取的网页，并行地爬取和解析相应的网页，并将数据存储在各自的MySQL数据库中。[slave爬虫程序](https://github.com/efishliu/Jobs-Recommendation-System/tree/master/Scrapy/slave)  
      * sqoop工具并行抽取3台slave节点的数据到HDFS文件系统中。**(注意解决sqoop数据倾斜问题）**  
    分布式爬虫项目说明：[ScrapyRedisDesc.md](https://github.com/efishliu/Jobs-Recommendation-System/blob/master/Scrapy/ScrapyRedisDesc.md)  
    参考文档：[Scrapy分布式爬虫](https://edu.csdn.net/notebook/python/week10/9.html)

* **用户画像与职位信息标签化处理**  
    * 用户画像说明： [UserPortraitDescription](https://github.com/efishliu/Jobs-Recommendation-System/blob/master/User%20Portrait/UserPortraitDescription.md)  
    * 使用TF-IDF,word2vec提取关键词和向量化:  
    python实现(本地)：[TF_IDF](https://github.com/efishliu/Jobs-Recommendation-System/tree/master/User%20Portrait/TF-IDF)，[word2vec.py](https://github.com/efishliu/Jobs-Recommendation-System/tree/master/User%20Portrait/Text%20vectorization)  
    spark ML实现：[spark_tf_idf.py]()，[spark_word2vec.py]()
    * 使用spark对学历，城市，工作经验，行业等进行薪资统计:[spark_mapreduce]()
    * 使用Hbase进行数据存储：HBase表结构设计：[HBase]()
* **基于Django开源框架的web页面与推荐算法**  
    * 使用MySQL构建HBase的索引：MySQL表结构：[index_hbase.sql]()
    * 基于内容的推荐:TopN的过滤与排名:[jobs_fliter_rank]()
    * Django框架的实现与部署：[Website Deploy](https://github.com/efishliu/Jobs-Recommendation-System/tree/master/Website/Website%20Deploy)
    * web页面设计：[Website Design](https://github.com/efishliu/Jobs-Recommendation-System/tree/master/Website/Website%20Design)
 
