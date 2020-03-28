
## JDBCUtils

JDBCUtils
```
private static DataSource ds;
private static ThreadLocal<Connection> th;

static{
	try {
		//静态代码块
		Properties pro = new Properties();
		pro.load(TestPools.class.getClassLoader().getResourceAsStream("druid.properties"));
		ds = DruidDataSourceFactory.createDataSource(pro);
		th = new ThreadLocal<Connection>();
	} catch (IOException e) {
		e.printStackTrace();
	} catch (Exception e) {
		e.printStackTrace();
	}
}

//抛出编译时异常
public static Connection getConnection() throws SQLException{
	//方式一：DriverManager.getConnection()
	//方式二：连接池对象.getConnection()
	Connection conn = th.get();//获取当前线程中的共享的连接对象
	if(conn == null){//当前线程没有拿过连接，第一个获取连接
		conn = ds.getConnection();//从连接池中拿一个新的
		th.set(conn);//放到当前线程共享变量中
	}
	return conn;
}

//把编译时异常转为运行时异常
public static void free(Connection conn){
	try {
		if(conn != null){
			conn.close();
		}
	} catch (SQLException e) {
		throw new RuntimeException(e);
	}
}

######## JDBC事务 ########
public static void main(String[] args) throws SQLException {
	String sql1 = "UPDATE t_department SET description = 'xx' WHERE did = 5183";
	String sql2 = "UPDATE t_department SET description = 'yy' where did = 5";//这个sql是故意写错的
	
	Connection conn = JDBCUtils.getConnection();
	conn.setAutoCommit(false);
	
	try {
		JDBCUtils.update(sql1);
		JDBCUtils.update(sql2);
		conn.commit();
	} catch (Exception e) {
		e.printStackTrace();
		conn.rollback();
	}
	
	conn.setAutoCommit(true);
	JDBCUtils.free(conn);
}

```
JDBCUtils的抽取
```

import java.lang.reflect.Field;
import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public abstract class BasicDAOImpl<T> {
	//type代表T的实际类型
	private Class<T> type;
	
	//在创建子类对象时，一定会调用父类的构造，默认调用父类的无参构造
	public BasicDAOImpl(){
		//这个this是你正在new的对象
		//那么这个clazz就是正在new对象的那个子类的类型的Class对象
		Class<? extends BasicDAOImpl> clazz = this.getClass();
		Type t = clazz.getGenericSuperclass();
		ParameterizedType pt = (ParameterizedType) t;//为什要强制，因为为了调用getActualTypeArguments
		Type[] types = pt.getActualTypeArguments();
		type = (Class) types[0];
	}
	
	//通用的增、删、改方法
	public int update(String sql,Object... args)throws SQLException{
		Connection conn = JDBCToolsV3.getConnection();
		PreparedStatement pst = conn.prepareStatement(sql);
		if(args != null && args.length>0){
			for (int i = 0; i < args.length; i++) {
				pst.setObject(i+1, args[i]);
			}
		}
		int len = pst.executeUpdate();
		pst.close();
		///JDBCToolsV3.free(conn);//故意不关，考虑到线程在多个位置可能共享同一个连接对象
		return len;
	}
	
	//通用的查询，一个T对象
	public T getBean(String sql,Object... args)throws SQLException, InstantiationException, IllegalAccessException, NoSuchFieldException, SecurityException{
		Connection conn = JDBCToolsV3.getConnection();
		PreparedStatement pst = conn.prepareStatement(sql);
		if(args != null && args.length>0){
			for (int i = 0; i < args.length; i++) {
				pst.setObject(i+1, args[i]);
			}
		}
		//第一步，创建T的对象
		T t = type.newInstance();
		
		ResultSet rs = pst.executeQuery();
		
		/*
		 * 结果集的元数据对象，(元数据：描述数据的数据，描述结果集中的数据的数据）
		 * 例如：结果集记录的列数
		 *     结果集的字段列表的名称
		 * 相当于SQLyog查询结果的标题行
		 */
		ResultSetMetaData metaData = rs.getMetaData();
		int counts = metaData.getColumnCount();//列数
		
		//这里用if,因为就查询一个对象，就一行
		if(rs.next()){
			//为t对象的属性赋值
			/*
			 * 反射如何为任意对象的任意属性赋值
			 * （1）获取属性对象
			 * Field field = clazz.getDeclaredField("属性名");
			 * （2）设置属性可访问
			 * field.setAccessible(true);
			 * （3）设置属性值
			 * field.set(t,属性值);
			 */
			//有几列，说明有几个属性
			//为counts个属性赋值
			for (int i = 0; i < counts; i++) {
//				Field field = type.getDeclaredField(metaData.getColumnName(i+1));//这个是数据库中的列的字段名
				Field field = type.getDeclaredField(metaData.getColumnLabel(i+1));//要获取Javabean中属性名，在sql语句中，用别名来代表类的属性名
				field.setAccessible(true);
				field.set(t, rs.getObject(i+1));
			}
		}
		
		rs.close();
		pst.close();
		return t;
	}
	
	//通用的查询，多个T对象
	public List<T> getBeanList(String sql,Object... args)throws SQLException, InstantiationException, IllegalAccessException, NoSuchFieldException, SecurityException{
		Connection conn = JDBCToolsV3.getConnection();
		PreparedStatement pst = conn.prepareStatement(sql);
		if(args != null && args.length>0){
			for (int i = 0; i < args.length; i++) {
				pst.setObject(i+1, args[i]);
			}
		}
		
		ArrayList<T> list = new ArrayList<T>();
		ResultSet rs = pst.executeQuery();
		
		/*
		 * 结果集的元数据对象，(元数据：描述数据的数据，描述结果集中的数据的数据）
		 * 例如：结果集记录的列数
		 *     结果集的字段列表的名称
		 * 相当于SQLyog查询结果的标题行
		 */
		ResultSetMetaData metaData = rs.getMetaData();
		int counts = metaData.getColumnCount();//列数
		
		//while循环一次，代表一行
		while(rs.next()){
			//第一步，创建T的对象
			T t = type.newInstance();
			//为t对象的属性赋值
			/*
			 * 反射如何为任意对象的任意属性赋值
			 * （1）获取属性对象
			 * Field field = clazz.getDeclaredField("属性名");
			 * （2）设置属性可访问
			 * field.setAccessible(true);
			 * （3）设置属性值
			 * field.set(t,属性值);
			 */
			//有几列，说明有几个属性
			//为counts个属性赋值
			for (int i = 0; i < counts; i++) {
				Field field = type.getDeclaredField(metaData.getColumnName(i+1));
				field.setAccessible(true);
				field.set(t, rs.getObject(i+1));
			}
			
			list.add(t);
		}
		
		rs.close();
		pst.close();
		return list;
	}
}

```
综合案例
```
######### 接口 #########
public interface DepartmentDAO {
	void addDepartment(Department dept);
	void updateDepartment(Department dept);
	void deleteDepartmentByDid(int did);
	Department getById(int did);
	List<Department> getAll();
}
######### 接口实现类 #########
public class DepartmentDAOImpl extends BasicDAOImpl<Department> implements DepartmentDAO{

	@Override
	public void addDepartment(Department dept) {
		String sql = "INSERT INTO `t_department` VALUES(NULL,?,?)";
		try {
			update(sql, dept.getDname(), dept.getDescription());
		} catch (SQLException e) {
			throw new RuntimeException(e);
		}
	}

	@Override
	public void updateDepartment(Department dept) {
		String sql = "UPDATE t_department SET dname=?,description=? WHERE did = ?";
		try {
			update(sql, dept.getDname(), dept.getDescription(), dept.getDid());
		} catch (Exception e){
			throw new RuntimeException(e);
		}
	}

	@Override
	public void deleteDepartmentByDid(int did) {
		String sql = "DELETE FROM t_department WHERE did = ?";
		try {
			update(sql, did);
		} catch (Exception e){
			throw new RuntimeException(e);
		}
	}

	@Override
	public Department getById(int did) {
		String sql = "SELECT did,dname,description FROM t_department WHERE did = ?";
		Department t = null;
		try {
			t = getBean(sql, did);
		} catch (Exception e){
			throw new RuntimeException(e);
		}
		return t;
	}

	@Override
	public List<Department> getAll() {
		String sql = "SELECT did,dname,description FROM t_department";
		List<Department> list = null;
		try{
			list = getBeanList(sql);
		} catch (Exception e){
			throw new RuntimeException(e);
		}
		return list;
	}

}
```
dbutils.QueryRunner;
```

 commons-dbutils 是 Apache 组织提供的一个开源 JDBC工具类库，它是对JDBC的简单封装
 并且使用dbutils能极大简化jdbc编码的工作量，同时也不会影响程序的性能。
  
 使用方式
  - 加入jar并且添加build path中
  - 修改BasicDAOImpl类
 QueryRunner该类封装了SQL的执行，是线程安全的。
  - 可以实现增、删、改、查、批处理、
  - 考虑了事务处理需要共用Connection。
  - 该类最主要的就是简单化了SQL查询，它与ResultSetHandler组合在一起使用可以完成大部分的数据库操作，能够大大减少编码量。

ResultSetHandler接口在查询时要用：
	该接口用于处理 java.sql.ResultSet，将数据按要求转换为另一种形式。
	该接口有如下实现类可以使用：
- BeanHandler：将结果集中的第一行数据封装到一个对应的JavaBean实例中。
- BeanListHandler：将结果集中的每一行数据都封装到一个对应的JavaBean实例中，存放到List里。
- ScalarHandler：查询单个值对象
- MapHandler：将结果集中的第一行数据封装到一个Map里，key是列名，value就是对应的值。
- MapListHandler：将结果集中的每一行数据都封装到一个Map里，然后再存放到List
- ColumnListHandler：将结果集中某一列的数据存放到List中。
- KeyedHandler(name)：将结果集中的每一行数据都封装到一个Map里，再把这些map再存到一个map里，其key为指定的key。
- ArrayHandler：把结果集中的第一行数据转成对象数组。
- ArrayListHandler：把结果集中的每一行数据都转成一个数组，再存放到List中。
########## JDBCUtils ##########
private static DataSource ds;
private static ThreadLocal<Connection> th;

static{
	try {
		//静态代码块
		Properties pro = new Properties();
		pro.load(TestPools.class.getClassLoader().getResourceAsStream("druid.properties"));
		ds = DruidDataSourceFactory.createDataSource(pro);
		th = new ThreadLocal<Connection>();
	} catch (IOException e) {
		e.printStackTrace();
	} catch (Exception e) {
		e.printStackTrace();
	}
}

//抛出编译时异常
public static Connection getConnection() throws SQLException{
	//方式一：DriverManager.getConnection()
	//方式二：连接池对象.getConnection()
	Connection conn = th.get();//获取当前线程中的共享的连接对象
	if(conn == null){//当前线程没有拿过连接，第一个获取连接
		conn = ds.getConnection();//从连接池中拿一个新的
		th.set(conn);//放到当前线程共享变量中
	}
	return conn;
}

//把编译时异常转为运行时异常
public static void free(Connection conn){
	try {
		if(conn != null){
			conn.close();
		}
	} catch (SQLException e) {
		throw new RuntimeException(e);
	}
}
########## JDBCUtils抽取 ##########
package com.atguigu.test07;

import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;
import java.sql.SQLException;
import java.util.List;
import java.util.Map;

import org.apache.commons.dbutils.QueryRunner;
import org.apache.commons.dbutils.handlers.BeanHandler;
import org.apache.commons.dbutils.handlers.BeanListHandler;
import org.apache.commons.dbutils.handlers.MapHandler;
import org.apache.commons.dbutils.handlers.MapListHandler;
import org.apache.commons.dbutils.handlers.ScalarHandler;

public abstract class BasicDAOImpl<T> {
	//type代表T的实际类型
	private Class<T> type;
	private QueryRunner qr = new QueryRunner();
	
	//在创建子类对象时，一定会调用父类的构造，默认调用父类的无参构造
	public BasicDAOImpl(){
		//这个this是你正在new的对象
		//那么这个clazz就是正在new对象的那个子类的类型的Class对象
		Class<? extends BasicDAOImpl2> clazz = this.getClass();
		Type t = clazz.getGenericSuperclass();
		ParameterizedType pt = (ParameterizedType) t;//为什要强制，因为为了调用getActualTypeArguments
		Type[] types = pt.getActualTypeArguments();
		type = (Class) types[0];
	}
	
	public int update(String sql,Object... args)throws SQLException{
		return qr.update(JDBCUtils.getConnection(), sql, args);
	}
	
	public T getBean(String sql,Object... args)throws SQLException{
		return qr.query(JDBCUtils.getConnection(), sql, new BeanHandler<>(type), args);
	}
	
	public List<T> getBeanList(String sql,Object... args)throws SQLException{
		return qr.query(JDBCUtils.getConnection(), sql, new BeanListHandler<>(type), args);
	}
	
	public Object getObject(String sql,Object... args)throws SQLException{
		return qr.query(JDBCUtils.getConnection(), sql, new ScalarHandler(), args);
	}
	
	public Map getMap(String sql,Object... args)throws SQLException{
		return qr.query(JDBCUtils.getConnection(), sql, new MapHandler(), args);
	}
	
	public List<Map<String,Object>> getMapList(String sql,Object... args)throws SQLException{
		return qr.query(JDBCUtils.getConnection(), sql, new MapListHandler(), args);
	}
}

########## JDBCUtils使用 ##########
public interface EmployeeDAO {
	void addEmployee(Employee emp);
	void updateEmployee(Employee emp);
	void deleteEmployeeByEid(int eid);
	Employee getByEid(int eid);
	List<Employee> getAll();
	long getEmployeeCount();
	
	//key：部门编号
	//value：部门的平均工资
	Map<Integer,Double> getAvgPerDepartment();
}

public class EmployeeDAOImpl extends BasicDAOImpl<Employee> implements EmployeeDAO{

	@Override
	public void addEmployee(Employee emp) {
		String sql = "INSERT INTO t_employee VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?)";
		//eid,ename,tel,gender,salary,commission_pct,birthday,hiredate,job_id,email,`mid`,address,native_place,did
		try{
			update(sql, emp.getEname(),
					emp.getTel(),
					emp.getGender(),
					emp.getSalary(),
					emp.getCommission_pct(),
					emp.getBirthday(),
					emp.getHiredate(),
					emp.getJobId(),
					emp.getEmail(),
					emp.getMid(),
					emp.getAddress(),
					emp.getNativePlace(),
					emp.getDid());
		}catch(Exception  e){
			throw new RuntimeException(e);
		}
	}

	@Override
	public void updateEmployee(Employee emp) {
		String sql = "UPDATE t_employee SET ename = ?,tel=?,gender=?,salary=?,commission_pct=?,birthday=?,hiredate=?,job_id=?,email=?,`mid`=?,address=?,native_place=?,did=? WHERE eid=?";
		try{
			update(sql, emp.getEname(),
					emp.getTel(),
					emp.getGender(),
					emp.getSalary(),
					emp.getCommission_pct(),
					emp.getBirthday(),
					emp.getHiredate(),
					emp.getJobId(),
					emp.getEmail(),
					emp.getMid(),
					emp.getAddress(),
					emp.getNativePlace(),
					emp.getDid(),
					emp.getEid());
		}catch(Exception  e){
			throw new RuntimeException(e);
		}
	}

	@Override
	public void deleteEmployeeByEid(int eid) {
		String sql = "DELETE FROM t_employee WHERE eid=?";
		try{
			update(sql, eid);
		}catch(Exception  e){
			throw new RuntimeException(e);
		}
	}

	@Override
	public Employee getByEid(int eid) {
		String sql = "SELECT eid,ename,tel,gender,salary,commission_pct,birthday,hiredate,job_id as jobId,email,`mid`,address,native_place as nativePlace,did FROM t_employee WHERE eid=?";
		Employee emp = null;
		try{
			emp = getBean(sql, eid);
		}catch(Exception  e){
			throw new RuntimeException(e);
		}
		return emp;
	}

	@Override
	public List<Employee> getAll() {
		String sql = "SELECT eid,ename,tel,gender,salary,commission_pct,birthday,hiredate,job_id,email,`mid`,address,native_place,did FROM t_employee";
		List<Employee> list = null;
		try{
			list = getBeanList(sql);
		}catch(Exception  e){
			throw new RuntimeException(e);
		}
		return list;
	}

	@Override
	public long getEmployeeCount() {
		String sql = "SELECT COUNT(*) FROM t_employee";
		long count = 0;
		try{
			count = (long) getObject(sql);
		}catch(Exception  e){
			throw new RuntimeException(e);
		}
		return count;
	}

	@Override
	public Map<Integer, Double> getAvgPerDepartment() {
		String sql = "SELECT did,AVG(salary) FROM t_employee GROUP BY did";
		Map<Integer, Double> map =new HashMap<Integer,Double>();
		try{
			List<Map<String, Object>> mapList = getMapList(sql);
			for (Map<String, Object> m : mapList) {
				/*
				 * m中存的是这个
				 * did=1
				AVG(salary)=22306.509285714284
				
				map.put(1, 22306.509285714284);
				 */
				Integer did = (Integer) m.get("did");
				Double avgSalary = (Double) m.get("AVG(salary)");
				map.put(did, avgSalary);
			}
		}catch(Exception  e){
			throw new RuntimeException(e);
		}
		return map;
	}

}



```