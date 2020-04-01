

## JSTL
```
简介：JSP Standard Tag Library（JSP标准标签库）
作用：JSTL替代JSP中的脚本中的代码。
使用JSTL：
	导包
	  - taglibs-standard-impl-1.2.1.jar
	  - taglibs-standard-spec-1.2.5.jar 	
	  -	<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
	使用
		JSTL常用标签：
			- <c:set var="变量名" value="值" scope="域范围">
	  		- <c:set target="对象名" property="属性名" value="属性值">
	  			用于添加或者修改域中的属性
	  				- value 
	  				  - 作用：要输出的值
	  				  - 参数类型：Object
	  				- var
	  				  - 作用：表示域中存放的属性名
	  				  - 参数类型：String
	  				- scope
	  				  - 作用：指定域对象(page,request,session,application)若不指定则为page域对象
	  				  - 参数类型：String
	  				- target
	  				  - 作用：要修改的域对象的属性名(必须是JavaBean或者Map)
	  				  - 参数类型：Object
	  				- property
	  				  - 作用：指定要修改的对象的属性名
	  				  - 参数类型：String
	  				- <c:set var="key" value="value" scope="request">  // 设置属性
	  				- <c:set property="name" target="${user}" value="孙悟空">  // 修改属性

	  		- <c:out value="值">
	  			将计算一个表达式并将结果输出到当前页面
	  			类似于 jsp : <%=> el： ${}
	  				- value 
	  				  - 作用：要输出的值
	  				  - 参数类型：Object
	  				- default
	  				  - 作用：当value为null的时候显示的值
	  				  - 参数类型：Object
	  				- escaXml
	  				  - 作用：是否对特殊字符转义
	  				  - 参数类型：boolean
	  			######### 代码 #########
  					<%
						int i = 10;
						request.setAttribute("i", i);
					%>
					jsp:<%=i%>

					<h1>JSTL通用标签</h1>
					<c:set var="i" value="100" scope="page"></c:set> <!-- 默认为page对象 -->
					jstl:<c:out value="${pageScope.i}"></c:out>
					jstl:<c:out value="${requestScope.i}"></c:out>
					jstl:<c:out value="${sessionScope.i}"></c:out>

	  		- <c:remove var="变量名" scope="域范围">
	  			用于移除域中的属性
	  				- var
	  				  - 作用：设置要移除的属性的名字
	  				  - 参数类型：String
	  				- scope
	  				  - 作用：设置要移除属性所在的域,若不指定则删除所有域中的对应的属性
	  				  - 参数类型：String
	  				- <c:remove var="key"/>  // 移除所有域中的属性
	  				- <c:remove var="key" scope="request">
	  			######### 代码 #########
	  				<c:remove var="i" scope="page" /> <!-- 如果不指定page默认将所有的作用域移除 -->
					<br> el:${i}

	  		- <c:if test="判断的结果为布尔值" var="变量" scope="域范围"></if>
	  			用于实现if语句的判断功能
	  				- test
	  				  - 作用：设置if的判断条件，用于判断标签体是否执行
	  				  - 参数：boolean
	  				- var
	  				  - 作用：用于指定接收判断结果的变量名
	  				  - 参数类型：boolean
	  				- scope
	  				  - 作用：指定判断结果保存到哪个域
	  				  - 参数类型：String
	  				###### 代码 ######
	  					<c:set target="${requestScope.user }" property="username" value="lisi"></c:set>
						<!-- 将zs修改为lisi -->
						${requestScope.user}
						<!-- User [username=lisi, password=123456]-->
						<c:if test="${not empty requestScope.user }">
							user is null
						</c:if>

	  		- <c:choose>
	  			<c:when test="">
	  			</c:when>
	  			<c:otherwise>
	  			</c:otherwise>
	  		  </c:choose>
	  		  	<c:choose>、</c:when>、<c:otherwise> 三个标签配合使用，功能类似于Java中的if/else
	  		  	- <c:choose>是</c:when>、<c:otherwise>的父标签
	  		  	- <c:when>的属性
	  		  	  - test
	  		  	    - 作用：用于设置判断条件，若正确则执行 when中的代码否则执行boolean
	  		  	    - 参数类型：boolean
	  		  	- <c:otherwise>
	  		  	  - 作用：如果所有的<c:when>都没有执行则执行<c:otherwise>的标签体
	  		  	######### 代码 #########
  		  			<c:set var="age" value="85" scope="session"></c:set>
					<c:choose>
						<c:when test="${sessionScope.age<18 }">
							未成年
						</c:when>
						<c:when test="${sessionScope.age>=18 and sessionScope.age < 30 }">
							青年
						</c:when>
						<c:when test="${sessionScope.age>=30 and sessionScope.age < 60 }">
							中年
						</c:when>
						<c:when test="${sessionScope.age>=60 and sessionScope.age < 80 }">
							中老年
						</c:when>
						<c:otherwise>
							老年
						</c:otherwise>
					</c:choose>
					<br>

	  		- <c:forEach var="变量名" begin="起始下标" end="结束下标" step="步长" item="迭代的集合|数组">
	  		  </c:forEach>
	  			用于对多个对象的集合进行迭代，重复执行标签体，或者重复迭代固定的次数
	  				- 属性
	  				  - var 
	  				  	 - 作用：设置遍历出对象的名称
	  				  	 - 参数类型：String
	  				  - items
	  				     - 作用：指定要遍历的集合对象
	  				     - 参数类型：数组、字符串和各种集合
	  				  - varStatus
	  				  	 - 作用：指定保存迭代状态的对象的名字，该变量引用的是一个LoopTagStatus类型的对象，通过该对象可以获得一些遍历的状态
	  				  	 	- count
	  				  	 	- index
	  				  	 	- first
	  				  	 	- list
	  				  	 	- name
	  				  	 - 参数类型：String
	  				  - begin
	  				    - 作用：指定遍历的开始位置
	  				    - 参数类型：int
	  				  - end
	  				    - 作用：指定遍历结束的位置
	  				    - 参数类型：int
	  				  - step
	  				    - 作用：迭代的步长
	  				    - 参数类型：int
				######### 代码 #########
		  		  	<c:forEach var="i" begin="0" end="100" step="2" varStatus="vs">
						${i }
					</c:forEach>
					
						<%
							//list
							List<User> list = new ArrayList<User>();
							list.add(0, new User("zs", "123456"));
							list.add(1, new User("lisi", "123456"));
							list.add(2, new User("wangwu", "123456"));
							session.setAttribute("list", list);
						%>

						<c:forEach items="${sessionScope.list }" var="user">
							username:${user.username }----password:${user.password }<br>
						</c:forEach>
	  	
```