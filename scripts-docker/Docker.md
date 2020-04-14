

## Docker
```
简介：


安装：

yum源准备

	curl  http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo -o /etc/yum.repos.d/docker-ce.repo
	wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
	curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo

安装依赖包

	yum install -y yum-utils device-mapper-persistent-data lvm2
	yum list docker-ce.x86_64 --showduplicates | sort -r
	yum install -y docker-ce

安装docker-ce

	yum install -y --setopt=obsoletes=0 \
	docker-ce-17.03.2.ce-1.el7.centos.x86_64 \
	docker-ce-selinux-17.03.2.ce-1.el7.centos.noarch


启动Docker服务

	systemctl daemon-reload
	systemctl restart docker
	docker version
	docker  info


配置镜像加速

	阿里云Docker-hub
	https://cr.console.aliyun.com/cn-hangzhou/mirrors

	mkdir -p /etc/docker
	tee /etc/docker/daemon.json <<-'EOF'
	{
	  "registry-mirrors": ["https://uoggbpok.mirror.aliyuncs.com"]
	}
	EOF

	systemctl daemon-reload
	systemctl restart docker
	  	  
	或者:
	vim   /etc/docker/daemon.json

		{
			 "registry-mirrors": ["https://68rmyzg7.mirror.aliyuncs.com"]
		}	


```
docker镜像的相关操作
```
docker拉取镜像
	docker search centos
	docker pull centos:6.9
	docker pull centos:7.5.1804
	docker pull nginx

查看系统中的镜像
	docker image ls
	docker image ls --no-trunc 
	docker image ls -a 查看当前正在
	标识镜像唯一性的方法:
		1. REPOSITORY:TAG
			centos:7.5.1804 
		2. IMAGE ID (sha256:64位的号码,默认只截取12位)
			82f3b5f3c58   
	查看镜像的id
		docker image ls -q
	查看镜像的详细信息
		docker image inspect ubuntu:latest
		docker image inspect 82f3b5f3c58f
	镜像的删除 
		docker image rm -f 3556258649b2
		docker image rm -f `docker image ls -q`

镜像的导入和导出

	导入
		docker image save 4e5021d210f6 > /tmp/ubuntu.tar
	导出
		docker image load -i /tmp/ubuntu.tar

镜像的修改标签和名称
	docker image tag 4e5021d210f6 ubu:v1


```
docker容器的相关操作
```
创建容器
	交互运行

		[root@docker ~]# docker container run -it  cf49811e3cdb
		[root@0310842ec60d /]#  # 直接进入到创建的容器中,退出容器则该容器变为Exited

		[root@docker ~]# docker container ls
		CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                             
		0310842ec60d        cf49811e3cdb        "/bin/bash"         2 minutes ago       Up 2 minutes   

		[root@docker ~]# docker container ls -a  # - a 参数查看当前包含未运行的容器
		CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                              
		0310842ec60d        cf49811e3cdb        "/bin/bash"         3 minutes ago       Exited (0) 18 seconds ago                       
		自定义名字创建镜像
		 	docker container run -it  --name="centos-1" cf49811e3cdb
		测试启动(退出后会自动删除)
			docker container run -it --name="centos-2"  --rm cf49811e3cdb
		启动
			docker container start ee6f5fdc87a8 # 相当于 Ctrl + p,q
			docker container start -i ee6f5fdc87a8 # 启动并登陆到容器中
		关闭
			docker container stop ee6f5fdc87a8
		连接
			docker container attach ee6f5fdc87a8 # 注意该种方式为同步的
			docker container exec -it  ee6f5fdc87a8 /bin/bash # 退出的时候不影响当前的状态



	守护运行
		docker run -d --name="nginx-1" ed21b7a8aee9
		端口映射 -p
		docker run -d -p 8080:80 --name="nginx-2" nginx
			[root@docker ~]# docker container ls
			CONTAINER ID        IMAGE       PORTS               NAMES
			743ac7c783e5        nginx   0.0.0.0:8080->80/tcp    nginx-2

	容器的后台及前台运行:
		1. ctrl + P, Q   
			attach 调用到前台
		2. 死循环 
		3. 让程序前台一直允许(夯在前台) 相当于 tail -f 

查看容器 
	docker container ls
	docker container ls -a
	docker container ls -a -q
		CONTAINER ID : 容器的唯一号码(自动生成的)
		NAMES		 : 容器的名字(可以自动,也可以手工指定)
		STATUS	     : 容器的运行状态  ( Exited , Up)
	查看容器的信息
		docker container inspect centos-1

删除容器
	docker container rm 8ceea7ebae88
	docker container rm -f 8ceea7ebae88
	docker container rm `docker container ls -a -q`

```
docker 容器的网络访问
```
指定映射(docker 会自动添加一条iptables规则来实现端口映射)
    -p hostPort:containerPort
    -p ip:hostPort:containerPort 
    -p ip::containerPort(随机端口:32768-60999)
    -p hostPort:containerPort/udp
    -p 81:80 –p 443:443
随机映射
	[root@docker ~]# docker run -d --name="n1" centos
	f4aa385578c11d28d83c0026e06dc87645bbefb6423289e42ad607fa82923277
	[root@docker ~]# docker run -d --name="n2" centos
	d3a163be16e250bcb085d39702a452e748a46a4fe000de762c81670d73d60c81
	连接到容器中
		yum install iproute* 
		ping 容器ip地址
将端口与容器进行端口的映射
	docker run -d -p 8080:80 --name="n1" nginx
	浏览器访问：http://192.168.8.104:8080/
	随机分配端口
	[root@docker ~]# docker container run -d -p 80 --name="n3" nginx
	[root@docker ~]# docker container ls -a
	CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                   NAMES
	473eadb14d3f        nginx               "nginx -g 'daemon of…"   3 seconds ago       Up 2 seconds        0.0.0.0:32768->80/tcp   n3

```
容器的其他管理
```
查看当前容器的进程
	docker  container top  ba9143bcaf74 
查看容器的日志
	[root@oldboy docker]# docker logs n1
	动态读取日志外部访问nginx
	[root@oldboy docker]# docker logs -t n1
	[root@oldboy docker]# docker logs -tf n1
	[root@oldboy docker]# docker logs -tf  --tail 10 n1
```