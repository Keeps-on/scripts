

## Docker数据的持久化存储
```
1.创建容器
	mkdir -p /opt/n1
	docker run -d -p 80:80 -v /opt/n1:/usr/share/nginx/html --name="n1" nginx
	此时在宿主机的/opt/n1的目录和容器n1/usr/share/nginx/html为共享目录
	
	补充指令将宿主机的文件拷贝到容器下的指定目录下
	宿主机-cp-n1
	docker container cp test.py n1:/usr/share/nginx/html
	n1-cp-宿主机
	docker container cp n1:/usr/share/nginx/50x.html ./

2. 多个容器同时挂载宿主机的目录
	[root@docker ~]# docker container run -d -p 90:80 --name="nginx-1" -v /opt/n1:/usr/share/nginx/html nginx
		33abfdc801471f0b133fbfd8f0d1575232aba04f611f6556ae59ad54743b2b8f
	[root@docker ~]# docker container run -d -p 91:80 --name="nginx-2" -v /opt/n1:/usr/share/nginx/html nginx
		a6dcfd18f0badb7330928cb575d870fe0b247bad90aadcc50f476b9fe9d0b349

3. 数据卷容器挂载
	宿主机目录
	mkdir -p /opt/Volume/a
	mkdir -p /opt/Volume/b
	touch /opt/Volume/a/a.txt
	touch /opt/Volume/b/b.txt
	创建数据卷容器
	docker run -it  --name "nginx_volumes" -v /opt/Volume/a:/opt/a  -v /opt/Volume/b:/opt/b centos:6.9 /bin/bash
	创建nginx容器
	docker run -d  -p 8085:80 --volumes-from  nginx_volumes --name "n8085"  nginx
	docker run -d  -p 8086:80 --volumes-from  nginx_volumes --name "n8086"  nginx

4. 制作本地局域网yum源
	1. 安装vsftpd软件
	[root@docker ~]# yum install -y vsftpd
	2. 启动ftp 
	[root@docker ~]# systemctl enable vsftpd
	[root@docker ~]# systemctl start vsftpd
	3. 上传系统进行到虚拟机
	略.
	mv CentOS-6.9-x86_64-bin-DVD1.iso /mnt/
	mv CentOS-7-x86_64-DVD-1804.iso /mnt/

	4. 配置yum仓库
	mkdir -p /var/ftp/centos6.9 
	mkdir -p /var/ftp/centos7.5

	mount -o loop /mnt/CentOS-6.9-x86_64-bin-DVD1.iso  /var/ftp/centos6.9/
	mount -o loop /mnt/CentOS-7-x86_64-DVD-1804.iso  /var/ftp/centos7.5/

	设置开机自动挂载
	vim /etc/rc.local
	mount -o loop /mnt/CentOS-6.9-x86_64-bin-DVD1.iso  /var/ftp/centos6.9/
	mount -o loop /mnt/CentOS-7-x86_64-DVD-1804.iso  /var/ftp/centos7.5/
	sh /etc/rc.local

	cat >/etc/yum.repos.d/ftp_6.repo <<EOF 
	[ftp]
	name=ftpbase
	baseurl=ftp://172.17.0.1/centos6.9
	enabled=1
	gpgcheck=0
	EOF


	cat >/etc/yum.repos.d/ftp_7.repo <<EOF 
	[ftp]
	name=ftpbase
	baseurl=ftp://10.0.0.100/centos7.5
	enabled=1
	gpgcheck=0
	EOF

5. 容器制作
	运行容器
	docker run -it --name="c1" centos:6.9
	修改yum源
	[root@4e88e33c1068 /]# cd etc/yum.repos.d/
	移除当前的yum源
		mv * /tmp/

	cat >/etc/yum.repos.d/ftp_6.repo <<EOF 
	[ftp]
	name=ftpbase
	baseurl=ftp://172.17.0.1/centos6.9
	enabled=1
	gpgcheck=0
	EOF

	yum clearn all
	yum makecache

	安装ssh
	yum install openssh-server -y
	启动ssh
	/etc/init.d/sshd start
	给当前用户设置密码
	passwd

	查看ip地址 宿主机连接测试
	[root@docker ~]# ssh root@172.17.0.2
	创建当前状态-快照
	docker commit 4e88e33c1068 lee/centos6.9_ssh:v1
	保持启动后台运行 启动后 sshd 可以正常运行
	docker container run -d --name="sshd" 6eacc92e4d4e /usr/sbin/sshd -D
	Xshell 连接 容器
	docker container run -d  --name=sshd_2222    -p 2222:22  6eacc92e4d4e /usr/sbin/sshd -D
	

```
镜像的制作
```
1. 运行容器
  373  # 创建容器
  374  # 制作镜像的完整步骤
  375  # 1. 创建宿主机数据卷
  376  ls
  377  # 1. 创建宿主机数据卷
  378  # 制作镜像的完整步骤
  379  # 1. 创建宿主机数据卷
  380  mkdir -p /opt/{mysql,html}
  381  # 2. 运行容器
  382  docker run -it --name="lee_centos" -v /opt/mysql/:/var/lib/mysql -v /opt/html/:/var/www/html centos:6.9
	优化yum源并安装软件
	mv /etc/yum.repos.d/*.repo /tmp
	echo -e "[ftp]\nname=ftp\nbaseurl=ftp://172.17.0.1/centos6.9\ngpgcheck=0">/etc/yum.repos.d/ftp.repo
	yum makecache fast && yum install openssh-server htppd mysql mysql-server php php-mysql -y

	软件初始化

	# sshd 初始化
	/etc/init.d/sshd start
	/etc/init.d/sshd stop
	echo "123456" | passwd  root --stdin 

 	# mysqld 初始化
	[root@c3fd597ec194 mysql]# /etc/init.d/mysqld start
	mysql> grant all on *.* to root@'%' identified by '123';
	mysql> grant all on *.* to discuz@'%' identified by '123';
	mysql> create database discuz charset utf8;

	# apache初始化
	[root@c3fd597ec194 mysql]# /etc/init.d/httpd start
	# 制作镜像
	docker commit d99fff709cac lee/centos_lamp:v1
2. 根据镜像启动新的容器并且暴露端口
	docker run -it --name="lee_centos2" -v /opt/vol/mysql:/var/lib/mysql -v /opt/vol/html:/var/www/html -p 8080:80 b851639a6060

	/etc/init.d/mysqld start 
	/etc/init.d/httpd start

	上传代码配置测试环境


	[root@docker html]# cd /opt/html
	[root@docker html]# cat init.sh 
	#!/bin/bash
	/etc/init.d/mysqld start 
	/etc/init.d/httpd start
	/usr/sbin/sshd -D
	[root@docker html]# chmod 777 init.sh 
	运行容器并执行启动脚本
	docker container run -d --name="lee_cnetos_end" -v /opt/vol/mysql:/var/lib/mysql -v /opt/vol/html:/var/www/html  -p 22222:22 -p 8888:80 -p 33060:3306 ac8888ea3e21 /var/www/html/init.sh

	基于centos7制作镜像
	docker run -it --name="75sshd" centos:7.5.1804
	
	mv /etc/yum.repos.d/*.repo /tmp
	echo -e "[ftp]\nname=ftp\nbaseurl=ftp://172.17.0.1/centos7.5\ngpgcheck=0">/etc/yum.repos.d/ftp.repo
	yum makecache fast && yum install openssh-server  -y

	mkdir /var/run/sshd
	echo 'UseDNS no' >> /etc/ssh/sshd_config
	sed -i -e '/pam_loginuid.so/d' /etc/pam.d/sshd
	echo 'root:123456' | chpasswd
	/usr/bin/ssh-keygen -A

	docker  commit lee_c75sshd d2bcdbdfd0f8 
	[root@docker ~]# docker container run -d  --name=sshd_2222    -p 222:22  lee_c75sshd /usr/sbin/sshd -D


```