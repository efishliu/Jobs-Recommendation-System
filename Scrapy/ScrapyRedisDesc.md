# 介绍
Scrapy-Redis是一个基于Redis的Scrapy分布式组件。它利用Redis对用于爬取的请求(Requests)进行存储和调度(Schedule)，
并对爬取产生的项目(items)存储以供后续处理使用。
scrapy-redis重写了scrapy一些比较关键的代码，将scrapy变成一个可以在多个主机上同时运行的分布式爬虫。  

# 项目说明：  
[master爬虫项目]()是master节点运行项目，负责整理url逻辑和将需要爬取的url存入Redis  
[slave爬虫项目]()是其余slave节点运行项目，负责从master节点的Redis的url取出，并解析网页，最后将数据存入MySQL数据库中  

# 准备：  
```powershell
    yum install redis
    vim /etc/redis.conf
```
将bind 127.0.0.1 改为 0.0.0.0  
将protected-mode yes 改为 protected-mode no  
将daemonize no 改为 daemonize yes  

安装redis(python),scrapy-redis
```powershell
    pip install redis
    pip install scrapy-redis
```
# 分布式爬取：
启动主节点master的redis数据库
```powershell
    redis-server /etc/redis.conf
```
运行主节点的爬虫程序：  
```powershell
    scrapy crawl spider_index
```
运行其他slave节点的爬虫程序：  
```powershell
    scrapy crawl spider_job51
```
