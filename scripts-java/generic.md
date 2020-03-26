

## 泛型

```
# 泛型类
# 语法格式
	【修饰符】 class 类名<泛型形参列表>{}
	【修饰符】 class interface 接口名<泛型形参列表>{}
# 泛型的使用
	class Student<T> {
		private String name;
		private T score;

		public Student(String name, T score) {
			super();
			this.name = name;
			this.score = score;
		}
		// get / set...
	}
	// 对于成绩来说不同的人评判标准不一样
	Student<String> chinese = new Student<String>("张三", "优秀");
	Student<Double> math = new Student<Double>("张三", 89.5);
	Student<Character> english = new Student<Character>("张三", 'A');
	# 继承泛型类,泛型接口时可以执行泛型类型实参
	class ChineseStudent extends Student<String>
	# 实现泛型接口时,可以指定泛型实参数
	class Employee implements Comparable<Employee>
	# 泛型类型或泛型接口上的<泛型形参>可以使用的范围
		- 属性，方法，数据形参，局部变量
		- 不能用于静态成员(在创建对象的过程中使用泛型的形参)
		class RangClass<T> {
			private T t; // 属性数据类型
			// private static T t2; // 不能作用于静态方法上
			public RangClass(T t) { // 方法的数据形参
				super();
				this.t = t;
			}
			// 返回值类型
			public T getT() {
				return t;
			}
			public void setT(T t) {
				this.t = t;
			}
			public void func() {
				T t;// 局部变量的类型
			}
			// public static T getT2() {
			// return t2;
			// }
			// public static void setT2(T t2) {
			// RangClass.t2 = t2;
			// }

		}
	# 泛型类或泛型接口的泛型形参,设定上限
		- <T extends 上限> -- >
		class Student<T extends Number>{}
		- Student stu = new Student<String>() // 报错
		// T的类型实参要求，同时是Number的子类，还要实现Comparable和Serializable的接口,当有多个上限的时候按照最左边第一个处理
		- class ClassName<T extends Number & Comparable & Serializable>
	# 泛型的形参类型的说明：
		- ArrayList<E>: E 表示集合的元素类型
		- Map<K,V>: K代表key类型，V代表的value类型
		- Comparable<T>: T 表示要与当前对象比较的另一个对象的类型
	# 泛型统配符
		- <?>:代表可以是任意类型
		- <? extends 上限>：? 代表是上限或者是上限的子类
		- <? super 下限>：?代表的是下限或者下限的父类
```