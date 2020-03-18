
## JDBC

概念：
```
JDBC 规范定义接口，具体的实现由各大数据库厂商来实现。
JDBC 是 Java 访问数据库的标准规范，真正怎么操作数据库还需要具体的实现类，也就是数据库驱动。每个
数据库厂商根据自家数据库的通信格式编写好自己数据库的驱动。所以我们只需要会调用 JDBC 接口中的方法即
可，数据库驱动由数据库厂商提供。
```
常用JDBC开发包
```
java.sql
	所有与 JDBC 访问数据库相关的接口和类
javax.sql
	数据库扩展包，提供数据库额外的功能。如：连接池
数据库的驱动
	由各大数据库厂商提供，需要额外去下载，是对 JDBC 接口实现的类
```
JDBC的核心API
```
DriverManager 类
说明： 
  1) 管理和注册数据库驱动
  2) 得到数据库连接对象
方法：
	// 通过连接字符串,用户名,密码来得到数据的连接对象
	Connection getConnection (String url, String user, String password)
	参数说明：
		用户名：登录用户名
		密码：登录的密码
		资源定位符(URL)：协议名:子协议://服务器名或 IP 地址:端口号/数据库名?参数=参数值
						jdbc:mysql://localhost:3306/db?characterEncoding=utf8

Connection 接口
说明：
  一个连接对象，可用于创建 Statement 和 PreparedStatement 对象
方法：
  // 创建一条 SQL 语句对象
  Statement createStatement() 

Statement 接口
说明：
  一个 SQL 语句对象，用于将 SQL 语句发送给数据库服务器。(静态 SQL 语句)
方法：
  int executeUpdate(String sql)
  	发送DML语句
  	操作：insert 、update、 delete、
  	返回值：返回对数据库影响的行数

  ResultSet executeQuery(String sql)
  	发送DQL语句
  	执行操作：select
  	返回值：查询的结果集

PreparedStatemen 接口
	一个 SQL 语句对象，是 Statement 的子接口
ResultSet 接口
	用于封装数据库查询的结果集，返回给客户端 Java 程序

```
JDBC实现步骤
```
############ 步骤 ############
1. 注册驱动
2. 创建连接对象
3. 创建Statement语句对象
4. 执行SQL语句：executeUpdate(sql) -- insert update delete
5. 返回影响的行数
6. 释放资源
	释放资源的对象：ResultSet 结果集，Statement 语句，Connection 连接
	释放原则：先开的后关，后开的先关。ResultSet > Statement > Connection
############ 代码 ############
package com.jdbc.demo;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;
public class TEST01 {
	public static void main(String[] args) throws  Exception {
		// 注册驱动
		Class.forName("com.mysql.jdbc.Driver");
		// 连接数据库
		String url = "jdbc:mysql://localhost:3306/jdbc_test??characterEncoding=utf8";
		Connection connection = DriverManager.getConnection(url, "root", "root123456");
		// 编写sql,创建Statement对象
		String sql = "create table student (id int PRIMARY key auto_increment, " +
						"name varchar(20) not null, gender boolean, birthday date)";
		Statement statement = connection.createStatement();
		// 返回结果
		int result = statement.executeUpdate(sql);  // 此处为静态sql 使用executeUpdate方法
		System.out.println(result); // 返回0 受影响的行数为0
		// 关闭资源
		statement.close();
		connection.close();
	}
}
// ---------------------插入数据--------------------------
package com.jdbc.demo;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class TEST02 {
	public static void main(String[] args) {
		Connection connection = null;
		Statement statement = null;
		try {
			// 注册驱动
			Class.forName("com.mysql.jdbc.Driver");
			// 连接数据库
			String url = "jdbc:mysql://localhost:3306/jdbc_test??characterEncoding=utf8";
			connection = DriverManager.getConnection(url, "root", "root123456");
			statement = connection.createStatement();
			int count = 0;
			count += statement.executeUpdate("insert into student values(null, '小赵', 1, '1993-03-24')");
			count += statement.executeUpdate("insert into student values(null, '小李', 0, '1993-03-24')");
			count += statement.executeUpdate("insert into student values(null, '小钱', 1, '1993-03-24')");
			count += statement.executeUpdate("insert into student values(null, '小孙', 0, '1993-03-24')");
			System.out.println("插入了"+ count + "条记录"); // 返回0 受影响的行数为0
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		// 关闭资源
		try {
			connection.close();
			statement.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
```
ResultSet
```
作用：封装数据库查询的结果集，对结果集进行遍历，取出每一条记录
方法：
	boolean next() 
	  游标向下移动一行
	  返回boolean类型，如果还有下一条记录，返回true,否则返回false
	数据类型 getXxx()
	  通过字段名，参数类型是String类型。返回不同的数据
	  通过列号，参数是整数，从 1 开始。返回不同的类型
	  boolean ---> getBoolean(String columnLabel)
	  byte  --->  getByte(String columnLabel)
	  short --->  getShort(String columnLabel)
	  long  --->  getLong(String columnLabel)
	  float --->  getFloat(String columnLabel)
	  double ---> getDouble(String columnLabel)
	  String ---> getString(String columnLabel) 以Java编程语言String的形式获取此ResultSet对象当前行中指定的列
############ 代码 ############
package com.jdbc.demo;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Date;

public class Test03 {
	public static void main(String[] args) {
		
		Connection connection = null;
		Statement statement = null;
		ResultSet resultSet = null;
		try {
			// 注册驱动
			Class.forName("com.mysql.jdbc.Driver");
			// 连接数据库
			String url = "jdbc:mysql://localhost:3306/jdbc_test??characterEncoding=utf8";
			connection = DriverManager.getConnection(url, "root", "root123456");
			statement = connection.createStatement();
			String sql = "select * from student";
			resultSet = statement.executeQuery(sql);
			while (resultSet.next()) {
				System.out.println(resultSet);
				int id = resultSet.getInt("id");
				String name = resultSet.getString("name");
				boolean gender = resultSet.getBoolean("gender");
				Date birthday = resultSet.getDate("birthday");
				System.out.println("编号：" + id + ", 姓名：" + name + ", 性别：" + gender + ", 生日：" +	birthday);
			}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		// 关闭资源
		try {
			resultSet.close();
			statement.close();
			connection.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}

```
数据库工具类jdbcUtil
```
package com.jdbc.utils;

import java.sql.*;

public class jdbcUtils {
	// 可以把几个字符串定义成常量：用户名，密码，URL，驱动类
	private static final String USER = "root";
	private static final String PWD = "root";
	private static final String URL = "jdbc:mysql://localhost:3306/jdbc_test??characterEncoding=utf8";
	private static final String DRIVER = "com.mysql.jdbc.Driver";

	/**
	 * 注册驱动
	 */
	static {
		try {
			Class.forName(DRIVER);
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		}
	}

	/**
	 * 得到数据库的连接
	 */
	public static Connection getConnection() throws SQLException {
		return DriverManager.getConnection(URL, USER, PWD);
	}

	/**
	 * 关闭所有打开的资源
	 */
	public static void close(Connection conn, Statement stmt) {
		if (stmt != null) {
			try {
				stmt.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		if (conn != null) {
			try {
				conn.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
	}

	/**
	 * 关闭所有打开的资源
	 */
	public static void close(Connection conn, Statement stmt, ResultSet rs) {
		if (rs != null) {
			try {
				rs.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		close(conn, stmt);
	}
}
############# JDBCUtils #######################
package com.jdbc.demo;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

import com.jdbc.utils.jdbcUtils;

public class Test04 {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		System.out.println("请输入用户名：");
		String name = scanner.nextLine();
		System.out.println("请输入密码：");
		String password = scanner.nextLine();
		login(name, password);
	}

	/**
	 * 登录方法
	 */
	public static void login(String name, String password) {
		Connection connection = null;
		Statement statement = null;
		ResultSet rs = null;

		try {
			connection = jdbcUtils.getConnection();
			statement = connection.createStatement();
			String sql = "select * from user where name='" + name
					+ "' and password='" + password + "'";
			System.out.println(sql);
			rs = statement.executeQuery(sql);
			if (rs.next()) {
				System.out.println("登录成功，欢迎您：" + name);
			} else {
				System.out.println("登录失败");
			}

		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} finally {
			// 释放资源
			jdbcUtils.close(connection, statement, rs);
		}

	}
}
```
PreparedStatement
```
作用：PreparedStatement 是 Statement 接口的子接口，继承于父接口中所有的方法。它是一个预编译的 SQL 语句
方法：
	PreparedStatement prepareStatement(String sql)
		指定预编译的 SQL 语句，SQL 语句中使用占位符 ?
		创建一个语句对象
	int executeUpdate() 
		执行 DML，增删改的操作，返回影响的行数
	ResultSet executeQuery()
		执行 DQL，查询的操作，返回结果集
优点：
	prepareStatement()会先将 SQL 语句发送给数据库预编译。PreparedStatement 会引用着预编译后的结果。可以多次传入不同的参数给 PreparedStatement 对象并执行。减少 SQL 编译次数，提高效率。
	安全性更高，没有 SQL 注入的隐患。
使用方法
	1. 编写 SQL 语句，未知内容使用?占位："SELECT * FROM user WHERE name=? AND password=?";
	2. 获得 PreparedStatement 对象
	3. 设置实际参数：setXxx(占位符的位置, 真实的值)
	4. 执行参数化 SQL 语句
	5. 关闭资源
常用的设置方法
	void setDouble(int parameterIndex, double x)  将指定参数设置为给定 Java double 值。
	void setFloat(int parameterIndex, float x)    将指定参数设置为给定 Java REAL 值。
	void setInt(int parameterIndex, int x)        将指定参数设置为给定 Java int 值。
	void setLong(int parameterIndex, long x)      将指定参数设置为给定 Java long 值。
	void setObject(int parameterIndex, Object x)  使用给定对象设置指定参数的值。
	void setString(int parameterIndex, String x)  将指定参数设置为给定 Java String 值
############ 代码 ############
package com.jdbc.demo;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Scanner;

import com.jdbc.utils.*;

public class Test05 {
	public static void main(String[] args) throws SQLException {

		Scanner sc = new Scanner(System.in);
		System.out.println("请输入用户名：");
		String name = sc.nextLine();
		System.out.println("请输入密码：");
		String password = sc.nextLine();
		login(name, password);
	}

	private static void login(String name, String password) throws SQLException {
		Connection connection = jdbcUtils.getConnection();
		// 写成登录 SQL 语句，没有单引号
		String sql = "select * from user where name=? and password=?";
		// 得到语句对象
		PreparedStatement ps = connection.prepareStatement(sql);
		// 设置参数
		ps.setString(1, name);
		ps.setString(2, password);
		ResultSet resultSet = ps.executeQuery();
		if (resultSet.next()) {
			System.out.println("登录成功：" + name);
		} else {
			System.out.println("登录失败");
		}
		// 释放资源,子接口直接给父接口
		jdbcUtils.close(connection, ps, resultSet);
	}
}

```