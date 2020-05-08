* 安装Anaconda3:  
  ```powershell
  wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2019.07-Linux-x86_64.sh
  ```
* 安装ssh:
  ```powershell
  yum install -y openssh-clients openssh-server
  ```
* 安装JAVA:
  ```powershell
  yum install -y java-1.8.0-openjdk java-1.8.0-openjdk-devel
  vim /etc/profile
  export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk
  source /etc/profile
  java -version
  ```
* 安装hadoop:
  ```powershell
  mkdir /usr/local/package
  cd /usr/local/package
  wget http://mirror.bit.edu.cn/apache/hadoop/common/hadoop-2.7.7/hadoop-2.7.7.tar.gz
  tar -zxvf hadoop-2.7.7.tar.gz -C /usr/local
  cd /usr/local/
  mv ./hadoop-2.7.7/ ./hadoop
  ```
* ssh免密配置:
  ```powershell
  vim /etc/hosts
  ```
  每台机器IP配置不同,master节点配置自己内网IP和其他节点外网IP，如:  
  127.0.0.1 localhost  
  自身内网IP(ifconfig查询） master  
  slave1外网IP    slave1  
  slave2外网IP    slave2  
  slave3外网IP    slave3  
  ```powershell
  cd  ~/.ssh
  ssh-keygen -t rsa -P ''
  cat id_rsa.pub >> authorized_keys
  ssh-copy-id master  (slave1,2,3)
  ssh-copy-id slave1  (master,slave2,3)
  ssh-copy-id slave2  (master,slave1,3)
  ssh-copy-id slave3  (master,slave1,2)
  ```

* 配置hadoop文件:
  ```powershell
  systemctl stop firewalld
  cd /usr/local/hadoop/etc/hadoop
  ```
  修改 slaves、core-site.xml、hdfs-site.xml、mapred-site.xml、yarn-site.xml,参考配置：[conf/hadoop](https://github.com/efishliu/Jobs-Recommendation-System/tree/master/Hadoop/conf/hadoop)  
  设置环境变量：
  ```powershell
  vim /etc/profile
  source /etc/profile
  ```
  ```powershell
  export HADOOP_HOME=/usr/local/hadoop
  export HADOOP_INSTALL=$HADOOP_HOME
  export HADOOP_MAPRED_HOME=$HADOOP_HOME
  export HADOOP_COMMON_HOME=$HADOOP_HOME
  export HADOOP_HDFS_HOME=$HADOOP_HOME
  export YARN_HOME=$HADOOP_HOME
  export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
  export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
  ```
* 安装spark：
  ```powershell
  cd /usr/local/package
  wget http://mirrors.tuna.tsinghua.edu.cn/apache/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz
  ```
* 安装mysql:
  ```powershell
  wget http://dev.mysql.com/get/mysql57-community-release-el7-8.noarch.rpm
  yum localinstall mysql57-community-release-el7-8.noarch.rpm
  yum install mysql-community-server
  ```
  ```powershell
  grep 'temporary password' /var/log/mysqld.log
  mysql -uroot -p
  ALTER USER 'root'@'localhost' IDENTIFIED BY 'YourPasswd1!';
  ```
* 安装sqoop:
  ```powershell
  wget https://mirrors.tuna.tsinghua.edu.cn/apache/sqoop/1.4.7/sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz
  tar -zxvf sqoop-1.4.7.bin__hadoop-2.6.0.tar.gz
  ```

  
