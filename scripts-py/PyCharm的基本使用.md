

[TOC]



# [PyCharm的基本使用](<https://www.jetbrains.com/help/pycharm/meet-pycharm.html>)

## 1 PyCharm安装

### 1.1 更改hosts文件

目的：将`0.0.0.0 account.jetbrains.com`添加到hosts文件中。这一步很重要。

hosts文件所在的位置`C:\Windows\System32\drivers\etc`  系统 文件中

+ 如果hosts文件为空

  ```
  # Copyright (c) 1993-1999 Microsoft Corp.
  
  #
  
  # This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
  
  #
  
  # This file contains the mappings of IP addresses to host names. Each
  
  # entry should be kept on an individual line. The IP address should
  
  # be placed in the first column followed by the corresponding host name.
  
  # The IP address and the host name should be separated by at least one
  
  # space.
  
  #
  
  # Additionally, comments (such as these) may be inserted on individual
  
  # lines or following the machine name denoted by a '#' symbol.
  
  #
  
  # For example:
  
  #
  
  # 102.54.94.97 rhino.acme.com # source server
  
  # 38.25.63.10 x.acme.com # x client host
  
  127.0.0.1 localhost
  0.0.0.0 account.jetbrains.com
  ```

+ 如果hosts文件不为空则将`0.0.0.0 account.jetbrains.com`加入底部

### 1.2 下载破解安装包

+ 下载安装包放入安装路径中 点击PyCharm >打开文件位置(右键) 

+ 找到两个文件分别是在最后尾部添加``

### 1.3 生成注册码

http://idea.lanyus.com/

## 2 配置PyCharm

### 2.1 配置字体

设置[^settings]> Editor > Font> `Consolas`

### 2.2 设置背景颜色

设置[^settings]> Editor > Color Scheme>  General `Darcula` 

### 2.3  鼠标滚轮控制字体的大小

设置[^settings]> Ctrl + Alt + S > Editor > General > `Mouse > Chang foot size(Zoom) with Ctrl+Mouse Wheel`

### 2.4  设置编码文件和SSH Terminal 

1. 文件编码配置

设置[^settings]> Editor > Code Style > File Encodings > **Global Encoding** `UTF-8` / **Project Encodings** `UTF-8`

2. 设置终端

设置[^settings]> Tools > SSH Terminal > Default encoding `UTF-8`

### 2.5 设置默认浏览器

设置[^settings] > Tools > Web Browsers **启动**快捷键 `Alt + F2`

配置Pycharm找不多Chrome的方法

设置[^settings] > Tools > Web Browsers 

path : 设置为Chrome的安装路径

Default Browser一栏勾选Custom Path

### 2.6 设置文件头部模板

File -> Settings -> Editor -> File and Code Templates ->Python Script

```
# -*- coding: utf-8 -*-
# @Time    : ${DATE} ${TIME}
# @Author  : Lee
# @Email  : 1299793997@qq.com
# @File  : ${NAME}.py
```

模板变量

```
$ {PROJECT_NAME} - 当前项目的名称。
$ {NAME} - 在文件创建过程中在“新建文件”对话框中指定的新文件的名称。
$ {USER} - 当前用户的登录名。
$ {DATE} - 当前的系统日期。
$ {TIME} - 当前系统时间。
$ {YEAR} - 今年。
$ {MONTH} - 当月。
$ {DAY} - 当月的当天。
$ {HOUR} - 目前的小时。
$ {MINUTE} - 当前分钟。
$ {PRODUCT_NAME} - 将在其中创建文件的IDE的名称。
$ {MONTH_NAME_SHORT} - 月份名称的前3个字母。 示例：1月，2月等
$ {MONTH_NAME_FULL} - 一个月的全名。 示例：1月，2月等
```

### 2.7 [设置自定义代码片段](<https://www.jetbrains.com/help/pycharm/2017.1/edit-template-variables-dialog.html>)

> <http://www.cnblogs.com/andy9468/p/8988501.html>

#### 2.7.1 Python Example

##### 分割线  `line`

```python
print('$VAR$'.center(30, '-')) 
$END$
```

#### 2.7.2 Python Persinal

##### 返回真 `rt` / `rf`

```python
return True / return False
```

##### 创建函数 `de`

```html
def $Function$($VAR$):
    $pass$
```

##### 快速添加字符串 `Ctrl + Alt + T`

```html
name 当没有添加字符串的时候
配置 toString
'$SELECTION$'  # 注意$SELECTION$的使用方法，然后注意的时候使用单引号`$SELECTION$`
1. 选中单词
2. ctrl + Alt + T 选中 toString
```

##### 定义一个基础的数组 `l`

```html
ll = [1, 2, 3, 'a', 'b', 'c']
```

##### 定义一个基础的字典 `ob`

```python
$res$ = {'name': 'Kevin', 'age': 18, 'sex': '男'$Var$}  $END$
```

### 2.8 Pycharm 恢复默认设置

C:\Users\Lee\.PyCharm2018.1 删除 `.PyCharm2018.1`

### 2.9 配置Django live template

#### 2.9.1 Django settins

##### 配置数据库

##### 配置模板路径

##### 配置redis

##### 配置orm测试模式

#### 2.9.2 Django models

##### 常用字段的配置



#### 2.9.3 Django views

##### 基本导入



##### 视图函数



#### 2.9.4 Django urls

##### 反向解析

##### 模板url

## 3 配置WebStorm定义片段

### 3.1 常用的[CDN](<https://www.bootcdn.cn/>)

#### 3.1.1 [Jquery](https://www.bootcdn.cn/jquery/)

```html
<script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js"></script>
```

#### 3.1.2 [Bootstrap3](https://v3.bootcss.com/getting-started/) 

```html
<!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- 可选的 Bootstrap 主题文件（一般不用引入） -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

<!-- 最新的 Bootstrap 核心 JavaScript 文件 -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
```

#### 3.1.3 [DataTables](https://datatables.net/manual/installation#Installing-Javascript-/-CSS)

```html
<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.19/css/jquery.dataTables.css">

<script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.js"></script>
```

#### 3.1.4 [LayUI](https://layui.hcwl520.com.cn/) 

```html
//layui.hcwl520.com.cn/layui/css/layui.css?v=201811010202
//layui.hcwl520.com.cn/layui/layui.js?v=201811010202
-----
<link rel="stylesheet" type="text/css" href="//layui.hcwl520.com.cn/layui/css/layui.css?v=201801090202" />
<script src="//layui.hcwl520.com.cn/layui/layui.js?v=201801090202"></script>
```

#### 3.1.5 [Sweetalert2](<https://sweetalert2.github.io/>)

```html
<script src="https://cdn.bootcss.com/limonte-sweetalert2/7.33.1/sweetalert2.all.min.js"></script>

<link href="https://cdn.bootcss.com/limonte-sweetalert2/7.33.1/sweetalert2.min.css" rel="stylesheet">
```

#### 3.1.6 [Echarts](<https://echarts.baidu.com/>)

```html
<script src="https://cdn.bootcss.com/echarts/4.2.1-rc1/echarts-en.common.min.js"></script>
```

#### 3.1.7 [FormValidation](<https://formvalidation.io/>)

```html
<link href="https://cdn.bootcss.com/jquery.bootstrapvalidator/0.5.3/css/bootstrapValidator.min.css" rel="stylesheet">

<script src="https://cdn.bootcss.com/jquery.bootstrapvalidator/0.5.3/js/bootstrapValidator.min.js"></script>
```

#### 3.1.8 [jquery Validation](<https://jqueryvalidation.org/>)

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-validate/1.19.0/jquery.validate.min.js"></script>
```

#### 3.1.9 [Highcharts](<https://www.highcharts.com.cn/>)

```html
// Highcharts
<script src="https://cdn.highcharts.com.cn/highcharts/highcharts.js"></script>

// Highstock
<script src="https://cdn.highcharts.com.cn/highstock/highstock.js"></script>

// Highmaps
<script src="https://cdn.highcharts.com.cn/highmaps/highmaps.js"></script>

// Highcharts Gantt
<script src="https://cdn.highcharts.com.cn/gantt/highcharts-gantt.js"></script>
```

### 3.2 HTML配置

#### 3.2.1 HMTL Import

##### 导入 jQuery `jq`

##### 导入 Bootstrap `bs3`

##### 导入 Datatables `dt`

##### 导入 SweetAlert2 `sw`

##### 导入 LayUI `lu`

##### 导入 Echarts `ec`

##### 导入 FormValidation `fv`

##### 导入 Jquery Validation `jv`

### 3.3 jQuery配置

#### 3.3.1 基本的配置

去掉代码下划线

settings -> Editor -> Colors & Fonts -> General ->Errors and Warnings
添加常用的代码提示
Language & Frameworks > JavaScript > Librares 下载常用的库

##### Jquery settings

###### 导入预加载 `do`

```html
<script>
    $(document).ready(function () {
        $END$
    });
</script>
```

###### 配置常用的事件 `e`

```html
$('#$ID$').on('$"click"$', function($ARG$){
   $END$ 
});
```

设置默认值，且需要注意的是默认值必须使用双引号进行包裹`“click”`

###### 配置绑定事件 `o`

```html
$('#$id$').on('$"click"$', $Function$);
```

###### 配置获取值操作 `val`

```html
var $Key$ = $('#$ID$').val();

```

###### 配置当前操作的值 `tv`

```html
$(this).val();
```

配置jq对象id `,`/ class 选择器`.`

```html
$('#$VAR$') / $('.$VAR$')
```

配置打印输出 `cl`

```html
console.log($VAR$) 
```



#### 3.3.2 配置Ajax

##### Jquery Ajax

###### 发送GET请求 `ag`

```html
$.ajax({
    url: '$URL$',
    type: 'POST',
    data: $DATA$,
    success: function(res){
        console.log(res)
    },
});$END$
```

###### 发送POST请求 `ap`

```html
$.ajax({
    url: '$URL$',
    type: 'GET',
    data: $DATA$,
    success: function(res){
        console.log(res)
    },
});$END$
```





一直更新。。。。









本文参考链接：

官网：https://www.jetbrains.com/help/idea/meet-intellij-idea.html

博客：https://www.cnblogs.com/luoahong/p/7529972.html

快捷键：https://resources.jetbrains.com/storage/products/intellij-idea/docs/IntelliJIDEA_ReferenceCard.pdf



[^settings]: Ctrl+Alt+S





设置<sup>Ctrl + Alt + S</sup>  >   
下表<sub>SUB</sub>