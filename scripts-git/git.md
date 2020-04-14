

## git学习整理


### git创建项目的过程
1、创建远程仓库
2、克隆到本地项目
```
git clone 
```
3、创建虚拟环境
```
python3 -m venv .venv
```
4、升级pip
```
pip install -U pip
```
5、备份安装包
```
pip freeze > requirements.txt
```
6、创建项目并配置项目
```
django-admin startproject projects ./
```
7、创建分支并推送分支
```
# 创建develop分支
git checkout -b develop
# 创建user分支
git checkout -b feat-user
# 切换分支
git checkout -
# 将分支推到远程版本库
git push -u origin develop
git checkout -
git push -u origin feat-user
```
8、删除本地分支
```
git branch -d [branch-name]
# 注意 删除前确定是否已经合并到分支
```
9、删除远程分支
```
git push origin --delete [branchname]
``
`
---
### git 版本回退
#### 本地到暂存区(add)
1、将本地文件添加到暂存区
> git add
```
git add .
```
2、将暂存区的文件进行撤回
> git rm --cached filename

## 暂存区到本地库（commit）
1、将暂存区添加到本地库
> git commit -m "提交信息"
```

```
2、查看版本信息
1. git log
> git log
> git log --pretty=oneline
> git log --oneline
> git reflog
```
# 第一种方式 git log --pretty=oneline
[root@iz2zehz627bdguedekm47az wordsapce]# git log --pretty=oneline

db62b7472239e2bd1ee5276daeda6cbf3f78e378 第二次提交
06be98d799d02c294b1e70e83ec9644b94573ab7 This is a demo
# 第二种方式
[root@iz2zehz627bdguedekm47az wordsapce]# git log --oneline

db62b74 第二次提交
06be98d This is a demo
[root@iz2zehz627bdguedekm47az wordsapce]# git reflog
# 第三种方式
db62b74 HEAD@{0}: commit: 第二次提交
06be98d HEAD@{1}: commit (initial): This is a demo
```
#### 版本回退
1、基于索引值操作
```
git reset --hard 【索引值】
```
2、使用^符号，只能后退
```
git reset --hard HEAD^
```
**注意：**一个 `^` 表示后退一步，`n` 个表示后退n步
3、使用~符号，只能后退
```
git reset --hard HEAD~n
```
**注意:**表示后退n步

---

删除远程的文件夹
```
参考:https://blog.csdn.net/cui130/article/details/84033966
git rm -r --cached test //--cached不会把本地的test删除
git commit -m 'delete test dir'
git push -u origin master


```
