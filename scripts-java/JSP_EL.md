

## JSP/El
```
简介：Java Server Pages(java服务端页面)
	Servlet = java + html
	Jsp只能运行服务器(Web容器)中
	Jsp本质是Servlet
运行原理
	第一次访问jsp文件时候,会经历以下步骤
		- 服务器将.jsp文件翻译为.java文件
		- 将.java文件编译为.class文件
		- 运行
	如文件未改变时候 以后在访问 不会翻译或编译
基本语法
	指令：
	  - 语法：<%@ %>
	脚本片段
	  - 语法：<%%>
	  - 作用：书写java代码(_javaService()中)
	表达式
	  - 语法：<%= %>
	  - 作用：输出数据到页面
	声明
	  - 语法：<%! %>
	  - 作用：java代码(类中)
	注释
	  - html：<!---->
	  - java：// /**/
	  - jsp：<%--  --%>
指令
	语法：<%@ 指令名   属性=属性值    属性2=属性值2%>
	常用指令：
	  - page指令：
	    - language：支持语言，默认java，只有java。
	  	- contentType：与response.setContentType()作用一致。
	  	- pageEncoding：jsp页面编码。
	  	- import：导包
	  	- errorPage：错误页面（当前页面报错时，显示的页面）
	  	- isErrorPage：设置当前页面是否为错误页面
	  - include指令
	    - 作用：将目标页面包含到当前页面中。
	    - 特点：静态包含，被包含的文件不会被翻译和编译。
Jsp动作标签：
	语法：<jsp: 标签名  属性=属性值></jsp:>
	常用的动作标签
		转发：
			- 带参数
				<jsp:forward page="NewFile.jsp">
					<jsp:param value="18" name="age"/>
			 	</jsp:forward>
	  		- 不带参数
	  			注意开始标签与结束标签之间不能有任何内容。
	  	动态包含	
	  		- 语法：<jsp:include page="被包含文件的路径"></jsp:include>
	  		- 特点：被包含文件会先被翻译和编译
Jsp九大隐含对象
	定义：可以在jsp中直接使用的对象。(不需要我们new的对象，服务器实例化的九大隐含对象，并存放在_jspService()方法中)
	对象详情
		1. application
			* 类型：ServletContext
		 	* 作用：域对象
		 	* Servlet中的获取方式：this.getServletContext()
		2. session
		 	* 类型：HttpSession
		 	* 作用：域对象
		 	* Servlet中的获取方式：request.getSession();
		3. request
			* 类型：HttpServletRequest
			* 作用：域对象（4个）
			* Servlet中的获取方式：直接使用
		4. pageContext
			* 类型：PageContext
			* 作用
				* 域对象
				* jsp老大（可以通过老大直接获取其他八个隐含对象） 
			* Servlet中的获取方式：无
		5. response
			* 类型：HttpServletResponse
			* 作用：域Servlet中的response对象一致
			* Servlet中的获取方式：直接使用
		6. page
			* 类型：Object
			* 作用：page = this,当前类的对象。
		7. out
			* 类型：JspWriter
			* 作用：与Servlet中的PrintWriter的作用类似。(都继承了java.io.Writer)
		8. config
			* 类型：ServletConfig
			* 作用：与Servlet中的ServletConfig的作用一致
			* Servlet中的获取方式:this.getServletConfig()
		9. exception
			* 类型：Throwable
			* 作用：接受处理异常信息

Jsp四大域对象
	域：区域，在web应用的不同资源中，相互传递数据。
		生活区域（快递）
			昌平区域
			北京同城
			全国快递
			全球快递
		程序区域
	域对象共有的方法
		getAttribute()
		setAttribute()
		removeAttribute()
  	详情
  		application
  			范围： 当前项目中有效
  		session
  			范围： 当前会话中有效（与浏览器，只有浏览器不关闭|不换，就一直有效）
  		request
  			范围： 当前请求中有效
  		pageContext 
  			范围： 当前页面中有效
  	能用小域，就不用大域。
######## 代码 ########
	<%
		application.setAttribute("name", "zs");
		session.setAttribute("name2", "zs2");
		request.setAttribute("name3", "zs3");
		pageContext.setAttribute("name4", "zs4");
	%>
	
	application:<%=application.getAttribute("name") %><br>
	session:<%=session.getAttribute("name2") %><br>
	request:<%=request.getAttribute("name3") %><br>
	pageContext:<%=pageContext.getAttribute("name4") %><br>

	<jsp:forward page="jsp_objectdemo2.jsp"></jsp:forward>
	<!-- 页面跳转 -->
	<a href="jsp_objectdemo2.jsp">demo2</a>
```
## El
```
EL简介：Expression Language（表达式语言）
	- JSP内置的表达式语言,用以访问页面的上下文以及不同作用域中的对象，取得对象属性的值，或执行简单的运算或判断操作。
EL作用：
	- EL表达式用于代替JSP表达式(<%= %>)在页面中做输出操作。
	- EL表达式仅仅用来读取数据，而不能对数据进行修改。
EL特点：
	- EL在得到某个数据时，会自动进行数据类型的转换。
	- 使用EL表达式输出数据时，如果有则输出数据，如果为null则什么也不输出。
El表达式与Jsp表达式的区别：
	- 如果数据为null,jsp显示null,El什么都不显示。
	- El显示的数据，必须存放在域对象或上下文对象中。
	- El可以自带数据类型转换的功能
El中的域对象：
	    名称 				jsp				    el 
	application域		 application		applicationScope
	session域			 session			sessionScope
	request域			 request			requsetScope
	page域				 pageContext		pageScope
El使用			 
	语法：${表达式}		
	eg:${requestScope.i} 	${stu.name}
	默认从小域到大域进行查找 pageContext < request < session < application
	### 代码 ###
	- jsp
		<%
			int i = 10;
		%>
		jsp:<%=i %>
	- el表达式
		pageContext.setAttribute("i", i);
 		request.setAttribute("i", i);
		session.setAttribute("i", i);
		application.setAttribute("i", i);
		el:${i}
	- el获取对象的属性值
		<%@page import="java.util.ArrayList"%>
		<%@page import="java.util.List"%>
		<%@page import="com.jsp.bean.Student"%>

		<%
			Student stu = new Student("zhangsan", 18);
			request.setAttribute("stu", stu);
		%>

		el:${stu.name }
		jsp:<%=((Student) request.getAttribute("stu"))%>

El的11个隐含对象：
	- pageContext：与jsp中的pageContext作用一致。
	- applicationScope
	- sessionScope
	- requestScope
	- pageScope
	- param:相当于request.getParameter() == ${param.username}
	- paramValues:相当于request.getParameterValues()
	- header:获取报文头信息
	- headerValues：
	- initParam：获取初始化参数
	- cookie：获取cookie信息
El的运算符：
	java:算术运算符	逻辑运算符		比较运算符	 位运算符	三元运算符
	El判断空值的运算符
	 	empty判断支持三种空
	 		- null
	 		- ""
	 		- List<String> list = new ArrayList<String>();(集合无数据) 
				<%
					String s = "";
					String s2 = null;
					List<String> list = new ArrayList<String>();

					request.setAttribute("s", s);
					request.setAttribute("s2", s2);
					request.setAttribute("list", list);
				%>
				${empty s} ${empty s2} ${empty list} ${not empty s}
				<br> ${!empty s2}
				<br> ${empty list}
				<br>
	 	判断非空
	 		- !empty
	 		- not empty 	
```