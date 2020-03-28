

## JDBC-note

### 事务
```java
mysql默认每一个连接是自动提交事务的。
JDBC事务
	1. 设置手动提交事务
		Connection的对象.setAutoCommit(false)
	2. 成功提交
		Connection的对象.commit();
	3. 回滚
		Connection的对象.rollback();

######## 代码 ###########
// 1. 注册驱动
Class.forName("com.mysql.jdbc.Driver");
// 2. 获取连接
Connection conn = DriverManager.getConnection(
		"jdbc:mysql://localhost:3306/jdbc_test", "root", "root123456");
// 3. 设置手动提交
conn.setAutoCommit(false);
// 执行sql
String sql_right = "update student set name = 'New_name2' where id = 2";
String sql_error = "update student set name = 'New_name' id = 2";

PreparedStatement pst = null;

try {
	pst = conn.prepareStatement(sql_right);
	int len = pst.executeUpdate();
	System.out.println("第一条：" + (len > 0 ? "成功" : "失败"));

	pst = conn.prepareStatement(sql_error);
	len = pst.executeUpdate();
	System.out.println("第二条：" + (len > 0 ? "成功" : "失败"));
	// 都成功了，就提交事务
	System.out.println("提交");
	conn.commit();
} catch (SQLException e) {
	System.out.println("回滚");
	// 失败要回滚
	conn.rollback();
}
// 4、关闭
pst.close();
conn.setAutoCommit(true);// 还原为自动提交
conn.close();
```

### 批处理

```java
long start = System.currentTimeMillis();
// 1. 注册驱动
Class.forName("com.mysql.jdbc.Driver");
// 2. 获取连接 rewriteBatchedStatements=true
Connection conn = DriverManager
		.getConnection(
				"jdbc:mysql://localhost:3306/jdbc_test?rewriteBatchedStatements=true",
				"root", "root123456");
// 3. 编写sql
String sql = "insert into user values(null,?,?)";
PreparedStatement pst = conn.prepareStatement(sql);
// 4. 预定义sql
for (int i = 1; i <= 1000; i++) {
	pst.setObject(1, "测试数据" + i);
	pst.setObject(2, "测试密码" + i);
	// 使用批处理
	pst.addBatch();
}

int[] executeBatch = pst.executeBatch(); // 执行语句返回结果,需要就接收,不需要就不接收

// 关闭
pst.close();
conn.close();

long end = System.currentTimeMillis();
System.out.println("耗时" + (end - start));
```

### 获取主键自增

```java
// 1. 注册驱动
Class.forName("com.mysql.jdbc.Driver");
// 2. 连接数据库
Connection conn = DriverManager.getConnection(
		"jdbc:mysql://localhost:3306/jdbc_test", "root", "root123456");

// 3. 定义sql语句
String sql = "insert into user values(null,?,?)";
// 4. 预编译sql语句
PreparedStatement pst = conn.prepareStatement(sql,Statement.RETURN_GENERATED_KEYS);
// 5. 设置sql
pst.setObject(1, "Bob");
pst.setObject(2, "789");
//执行sql
int len = pst.executeUpdate();//返回影响的记录数
if(len>0){
	//从pst中获取到服务器端返回的键值
	ResultSet rs = pst.getGeneratedKeys();
	//因为这里的key值可能多个，因为insert语句可以同时添加多行，所以用ResultSet封装
	//这里因为只添加一条，所以用if判断
	if(rs.next()){
		System.out.println(rs);
		Object key = rs.getObject(1); // rs.getObject() 有几列就能获取到第几列的数据
		System.out.println("自增的key值id =" + key);
	}
}
//4、关闭
pst.close();
conn.close();
```

