
## 数据库的连接池

```
说明：由于每次执行sql语句的过程中都需要连接数据库并且数据库创建新的连接然后随之释放。数据库的连接相当于TCP/IP协议
编程的Socket,每个客户端,每一次连接都有一个独立的Socket,在连接之前有三次握手,断开连接时候四次捂手。该过程是一次资源成本高的一个过程
数据库连接池参数(DataSource)
  - 初始化连接数：即从一开始准备的连接数量,例如：10 个
  - 最大连接数：即数据库服务器最多能承受多少个连接数：100 个
  - 每次增量：如果10个不够了,会增加多少,直到达到100 个
  - 等待时间
    如果达到了100个,用户应该如何操作
      - 让用户无限等待
      - 等待一定时间后,返回异常,告知客户端,连接超时
常见的数据库连接池
  - DBCP: Apache提供,速度相对c3p0较快,不稳定
  - c3p0: 相对稳定
  - Proxool
  - BoneCP
  - Druid: 阿里提供
连接池的使用优点
  - 连接资源的重用
  - 对于用户来说,系统的响应速度快
  - 新的资源分配手段(原来从数据库直接获取现在是从连接池中获取)
  - 避免了数据库服务器的高压力
连接池的使用
  - 引入jar包并且添加到build path中
  - 配置文件中写配置参数
    - url : 数据库资源定位符
    - username : 用户名
    - password : 密码
    - driverClassName : 驱动类名
    - initialSize : 初始化连接数
    - maxActive : 最大连接数
    - maxWait : 等待时间
    - minIdle : 空闲时间最小连接池数量
  - 获取连接对象
  	- DataSource ds = DruidDataSourceFactory.createDataSource(properties);
  	- Connection connection = ds.getConnection();
  - 关闭连接
  	- connection.close(); // 使用后释放
############# 代码 #############
@Test
public void test01() throws Exception {
  Properties properties = new Properties();
  /**
   * Test01.class:得到当前类的Class对象 xx.getClassLoader():获取当前类加载器对象
   * 类加载器对象.getResourceAsStream():加载资源文件,并且把配置文件中的数据封装到Properties对象
   */
  properties.load(Test01.class.getClassLoader().getResourceAsStream(
      "druid.properties"));
  DataSource ds = DruidDataSourceFactory.createDataSource(properties);
  System.out.println(ds);
  // 获取连接对象-从连接池中获取
  for (int i = 1; i <= 30; i++) {
    Connection connection = ds.getConnection();
    System.out.println("第" + i + "个连接" + connection);
    
    connection.close(); // 使用后释放
  }
}
```

