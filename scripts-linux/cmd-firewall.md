


## CentOS7 防火墙的配置

查看版本
```
cat /etc/redhat-release


```

查看firewall服务状态
```
systemctl status firewalld

```
查看firewall的状态
```
firewall-cmd --state
// no or running
```
开启、重启、关闭 firewalld.service服务
```
# 开启
service firewalld start
# 重启
service firewalld restart
# 关闭
service firewalld stop

```
查看防火墙规则
```
firewall-cmd --list-all 

```
查询、开放、关闭端口
```
# 查询端口是否开放
firewall-cmd --query-port=8080/tcp
# 开放80端口
firewall-cmd --permanent --add-port=80/tcp
# 移除端口
firewall-cmd --permanent --remove-port=8080/tcp

#重启防火墙(修改配置后要重启防火墙)
firewall-cmd --reload

# 参数解释
1、firwall-cmd：是Linux提供的操作firewall的一个工具；
2、--permanent：表示设置为持久；
3、--add-port：标识添加的端口；

```
开机禁用或者启用firewall
```
systemctl disable/enable firewalld.service

```



