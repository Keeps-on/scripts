

## Dockerfile


```

基础使用

[root@docker ~]# mkdir -p /opt/dockerfile/centos6.9_sshd
[root@docker centos6.9_sshd]# vim Dockerfile

# Centos6.9-SSHDv1.0
FROM centos@2199b8eb8390
RUN mv /etc/yum.repos.d/*.repo /tmp && echo -e "[ftp]\nname=ftp\nbaseurl=ftp://172.17.0.1/centos6.9\ngpgcheck=0">/etc/yum.repos.d/ftp.repo && yum makecache fast && yum install openssh-server -y
RUN  /etc/init.d/sshd start && /etc/init.d/sshd stop && echo "123456" | passwd root --stdin
# 拷贝init.sh 在容器跟目录下
COPY init.sh /
# 将master.tar.gz 拷贝到/var/www/html 下并进行自动解压
ADD  master.tar.gz /var/www/html/
ADD  https://mirrors.aliyun.com/centos/7.6.1810/os/x86_64/Packages/centos-bookmarks-7-1.el7.noarch.rpm /tmp
EXPOSE 22
EXPOSE 80
EXPOSE 3306
CMD ["/bin/bash","/init.sh"]

# index.sh文件
	#!/bin/bash
	/etc/init.d/mysqld start
	mysql -e "grant all on *.* to root@'%' identified by '123';grant all on *.* to discuz@'%' identified by '123';create database d
	iscuz charset utf8;"
	/etc/init.d/httpd start
	/usr/sbin/sshd -D

docker image build -t "lee/centos6.9-sshd:v1.0" ./

测试
	rm -rf .ssh  # 如果当前连接的ip地址已经连接过则删除

Dockerfile 常用指令 
	FROM： 基础镜像
		Syntax：
		FROM	centos:6.9
		FROM 	centos@2199b8eb8390

	RUN：  构建镜像过程中运行的命令
		Syntax：
		RUN	 mv /etc/yum.repos.d/*.repo /tmp && echo -e "[ftp]\nname=ftp\nbaseurl=ftp://172.17.0.1/centos6.9\ngpgcheck
	=0">/etc/yum.repos.d/ftp.repo && yum makecache fast && yum install openssh-server -y
		RUN	["mysqld","--initialize-insecure","--user=mysql"  ,"--basedir=/usr/local/mysql","--datadir=/data/mysql/data"] 

	EXPOSE: 向外暴露的端口 
		Syntax:
			EXPOSE  22

	CMD    使用镜像启动容器时运行的命令
		Syntax：
		CMD	["/usr/sbin/sshd","-D"]

	COPY： 

	Syntax：
		  <src>...   <dest>
		  
			从dockerfile所在目录，拷贝目标文件到容器的制定目录下。
			可以支持统配符，如果拷贝的是目录，只拷贝目录下的子文件子目录。
			cp oldguo/* 		
	ADD    	
	Syntax：
		  <src>...   <dest>
		  url        <dest>

		  比COPY命令多的功能是，可以自动解压.tar*的软件包到目标目录下
		  可以指定源文件为URL地址

	VOLUME ["/var/www/html","/data/mysql/data"]

	WORKDIR 

	ENV  设定变量 
	ENV CODEDIR /var/www/html/
	ENV DATADIR /data/mysql/data
	ADD bbs.tar.gz ${CODEDIR}
	VOLUME ["${CODEDIR}","${DATADIR}"]


	ENTRYPOINT

	#CMD ["/bin/bash","/init.sh"]
	ENTRYPOINT ["/bin/bash","/init.sh"]

	说明： 
	ENTRYPOINT 可以方式，在启动容器时，第一进程被手工输入的命令替换掉，防止容器秒起秒关

```