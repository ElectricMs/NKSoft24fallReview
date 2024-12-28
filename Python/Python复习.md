# Python复习

Python复习  202412  2211030

## 语法介绍 

CPython，官方解释器，基于c语言

Python创始人：吉多·范罗苏姆（Guido van Rossum），荷兰人

**解释器和编译器的区别**

解释器逐行读取并执行源代码，编译器会一次性地将整个程序从高级语言转换成机器语言或中间表示形式（如字节码），然后生成一个独立的可执行文件。

**动态类型**

变量不需要事先声明其类型，可以在任何时候给一个变量赋值为任意类型的对象

**强类型**

```python
y = 10 + "20"   # 这会导致 TypeError: unsupported operand type(s) for +: 'int' and 'str'
a = 99 + True   # 不会报错，bool被视为整形
b = 99 + true   # 报错，python大小写敏感
```

**标识符**

- 区分大小写，如: sxt和SXT是不同的
- 第一个字符必须是字母、下划线，其后的字符是：字母、数字、下划线
- 不能使用关键字，如: if, or, while等

**Python中一切皆为对象**

每个对象都有三个基本属性：

- 身份（Identity）：每个对象都有一个独一无二的身份标识，可以通过内置函数`id()`获取。这个身份通常是在创建对象时分配的内存地址。
- 类型（Type）：每个对象都有一个定义其行为和允许操作的类型。你可以使用内置函数`type()`来查询对象的类型。
- 值（Value）：这是对象所包含的数据或信息。

对象一旦被创建，其id与type便无法再修改

### 赋值

```python
a = 99
b = 88
b, a = a, a + b # 先计算a+b的值再分别赋值
print(a) # 187
print(b) # 99
```

```python
# 与c语言不同的赋值方式
a = 10
b = a
a = 20
print(a, b) # 20 10
```

**解包赋值：**

- 将一个可迭代对象（如列表、元组、字符串等）中的元素直接分配给多个变量
- 扩展解包操作符`*`，允许我们将一部分元素分配给单个变量，而剩下的元素作为一个列表或元组分配给另一个变量

```python
# 元组解包
coordinates = (10, 20)
x, y = coordinates
print(x, y)  # 输出: 10 20

# 列表解包
values = [4, 5, 6]
a, b, c = values
print(a, b, c)  # 输出: 4 5 6

char_tuple = ('P', 'y', 't', 'h', 'o', 'n')
first, second, *rest = char_tuple
print(first, second, rest)  # 输出: P y ['t', 'h', 'o', 'n']
```

- ==**单星号 `\*` 的作用**：用于解包可迭代对象（如列表、元组）为位置参数。==
- ==**双星号 `\**` 的作用**：用于解包字典为关键字参数。==

**赋值操作与两种拷贝**

- 赋值 (`=`)：不创建新对象，只创建新引用。
- 浅拷贝 (`copy.copy()` 或 `.copy()` 方法)：创建新对象，但嵌套对象仍共享。
- 深拷贝 (`copy.deepcopy()`)：创建新对象及其所有嵌套对象的新副本。

```python
a = [1, 2, [3, 4]]
b = a  # 这里只是创建了一个新的引用，a 和 b 指向同一个列表
b[0] = 99
print(a)  # 输出: [99, 2, [3, 4]]
```

```python
import copy

a = [1, 2, [3, 4]]
b = copy.copy(a)  # 或者 a.copy() 对于支持该方法的对象
b[0] = 99
print(a)  # 输出: [1, 2, [3, 4]] 因为改变的是顶层元素
b[2][0] = 5
print(a)  # 输出: [1, 2, [5, 4]] 因为改变了嵌套列表中的元素
```

```python
import copy

a = [1, 2, [3, 4]]
b = copy.deepcopy(a)
b[0] = 99
b[2][0] = 5
print(a)  # 输出: [1, 2, [3, 4]] 新对象的修改不影响原对象
print(b)  # 输出: [99, 2, [5, 4]]
```

### String

**基本操作**

- **join(seq)**: 将序列中的元素连接成一个字符串。
- **len(string)**: 返回字符串的长度。
- **count(str, beg=0, end=len(string))**: 计算字符串中某个子串出现的次数。
- **capitalize()**: 将字符串的第一个字符转换为大写，其余字符转换为小写。
- **title()**: 将字符串中的每个单词的首字母转换为大写。
- **upper()**: 将字符串中的所有字符转换为大写。
- **lower()**: 将字符串中的所有字符转换为小写。
- **swapcase()**: 将字符串中的大写字母转换为小写，小写字母转换为大写。

**查找和定位**

- **index(str, beg=0, end=len(string))**: 返回字符串中指定子串的第一个匹配项的索引。
- **rindex(str, beg=0, end=len(string))**: 返回字符串中指定子串的最后一个匹配项的索引。
- **find(str, beg=0, end=len(string))**: 类似于 `index`，但如果没有找到子串则返回 `-1`。
- **rfind(str, beg=0, end=len(string))**: 类似于 `rindex`，但如果没有找到子串则返回 `-1`。

**格式化和对齐**

- **rjust(width[, fillchar])**: 将字符串右对齐，并使用指定字符填充左侧。
- **center(width, fillchar)**: 将字符串居中，并使用指定字符填充两侧。
- **ljust(width, fillchar)**: 将字符串左对齐，并使用指定字符填充右侧。
- **max(str)**: 返回字符串中最大的字符。
- **min(str)**: 返回字符串中最小的字符。
- **replace(old, new [, max])**: 替换字符串中所有的 `old` 子串为 `new` 子串。

**判断**

- **isalnum()**: 检查字符串是否只包含字母数字字符。
- **isalpha()**: 检查字符串是否只包含字母字符。
- **isdigit()**: 检查字符串是否只包含数字字符。
- **islower()**: 检查字符串是否全部为小写字母。
- **isnumeric()**: 检查字符串是否只包含数字字符（包括Unicode数字）。
- **isspace()**: 检查字符串是否只包含空白字符。
- **istitle()**: 检查字符串是否符合标题格式（每个单词首字母大写）。
- **isupper()**: 检查字符串是否全部为大写字母。
- **isdecimal()**: 检查字符串是否只包含十进制数字字符。

**分割和组合**

- **splitlines([keepends])**: 按行分割字符串。
- **split(str="", num=string.count(str))**: 按指定分隔符分割字符串。
- **zfill(width)**: 将字符串用零填充到指定宽度。
- **expandtabs(tabsize=8)**: 将字符串中的制表符扩展为空格。
- **maketrans()**: 创建一个用于翻译的映射表。

**编码和解码**

- **encode(encoding='UTF-8', errors='strict')**: 将字符串编码为字节。
- **bytes.decode(encoding="utf-8", errors="strict")**: 将字节解码为字符串。
- **startswith(substr, beg=0, end=len(string))**: 检查字符串是否以指定子串开头。
- **endswith(suffix, beg=0, end=len(string))**: 检查字符串是否以指定子串结尾。
- **strip([chars])**: 删除字符串两端的指定字符。
- **rstrip()**: 删除字符串右侧的空白字符。
- **lstrip()**: 删除字符串左侧的空白字符。

**其他**

- **translate(table, deletechars='')**: 使用给定的映射表替换或删除字符串中的字符。

### Formatted Output

**1. 使用 `%` 操作符（旧式格式化）**

这是较老的一种方式，使用类似于C语言中的 `printf` 函数的方式。

```python
name = "Alice"
age = 30
formatted_string = "Hello, %s. You are %d years old." % (name, age)
print(formatted_string)  # 输出: Hello, Alice. You are 30 years old.
```

- `%s` 表示字符串。
- `%d` 表示整数。
- `%f` 表示浮点数。`%3.4f`表示宽度至少3位，小数保留4位

**2. 使用 `str.format()` 方法（新式格式化）**

这是一种更灵活且推荐的方式，允许你通过位置或命名参数来指定值的位置。

```python
formatted_string = "Hello, {}. You are {} years old.".format(name, age)
print(formatted_string)

# 也可以通过索引或关键字参数来指定：
formatted_string = "Hello, {1}. You are {0} years old.".format(age, name)
print(formatted_string)

formatted_string = "Hello, {person_name}. You are {person_age} years old.".format(person_name=name, person_age=age)
print(formatted_string)
```

**3. 使用 f-string（格式化字符串字面量）(Python 3.6+)**

这是最现代的方法，它允许你在字符串中直接嵌入表达式，并在运行时求值。

```python
formatted_string = f"Hello, {name}. You are {age} years old."
print(formatted_string)

# 你可以直接在花括号内进行简单的运算或调用函数
formatted_string = f"{name.upper()} is {age * 2} years old in dog years."
print(formatted_string)
```

f-string 不仅简洁，而且性能更好，因为它们是在编译时解析的，而不是像 `str.format()` 那样在运行时解析。

**4. 使用 `string.Template` 类（模板字符串）**

这种方式适用于需要用户输入或者从不可信来源获取内容的情况，因为它不支持复杂的表达式，只支持简单的变量替换，因此更加安全。

```python
from string import Template

t = Template('Hey, $name. You are $age years old.')
formatted_string = t.substitute(name=name, age=age)
print(formatted_string)
```

选择哪种方法取决于你的具体需求和Python版本。对于新项目，建议使用 f-string 或者 `str.format()` 方法，因为它们提供了更好的可读性和灵活性。如果你正在维护一个较老的代码库，可能还需要继续使用 `%` 操作符格式化。



### List

```python
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
print(list[1:3]) # [786, 2.23], 包头不包尾
tinylist = [123, 'john']
print(tinylist * 2) # [123, 'john', 123, 'john']\

del list[2] # 删除列表第三个元素
list.append(obj)  # 末尾添加⼀个元素
list.extend(seq)  # 在末尾⼀次性追加另⼀个序列（可以是列表，元组等）
list.clear() # 移除列表中所有元素
list.remove(obj) # 移除列表中指定的元素
list.insert(index, obj) # 在指定位置（前⾯）插⼊⼀个元素
list.reverse() # 反转列表中的元素顺序
list.sort([func]) # 对列表进⾏排序
list.count(obj) # 统计列表中指定元素的出现次数
list.index(obj) # 返回列表中第⼀个匹配给定值的元素的索引
```

易错题：

```python
nums=[1,2,2,2,3,4,2]
for num in nums:
    print(num)
    if num==2:
        nums.remove(2)
print(nums)

"""
1
2
2
4
2
[1, 3, 4, 2]
"""
```

排序：

```python
list.sort(key=None,reverse=False) # 对原有列表排序
#key 参数是⼀个函数，⽤于⽣成⽤于排序⽐较的键。
#reverse 参数是⼀个布尔值，⽤于指定是否按降序进⾏排序。
list.reverse() # 反转列表中的元素顺序
sorted(iterable, key=None, reverse=False) #sorted和reversed都是内置函数，不会改变list
#iterable 是要排序的可迭代对象，key和reverse 参数与list.sort() ⽅法相似
reversed(seq) # 这是⼀个内置函数，返回⼀个反向的迭代器

# list[start:stop:step], 切片，注意！不改变原来的list，返回新的排序对象
original_list = [1, 2, 3, 4, 5]
reversed_list = original_list[::-1]
print(reversed_list)  # 输出: [5, 4, 3, 2, 1]
```

### Tuple

```python
tuple = (1,) # 单元素元组的表示
```

元组是不可变的

python函数返回有且仅有一个返回值（None，一个，多个是元组）

### Dict

键（key）需要是不可变的数据类型：Number, str, tuple, bool, None, frozenset

```python
# 使⽤花括号创建字典
my_dict = {'key1': 'value1', 'key2': 'value2'}
# 使⽤dict()构造函数创建字典
another_dict = dict(key1='value1', key2='value2')

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print (dict['one']) # Prints value for 'one' key
print (dict[2]) # Prints value for 2 key
print (tinydict) # Prints complete dictionary
print (tinydict.keys()) # Prints all the keys
print (tinydict.values()) # Prints all the values
```

### Set

```python
# 使用大括号创建一个可变集合
my_set = {1, 2, 3}
my_set.add(4)        # 添加元素
my_set.remove(2)     # 移除元素
print(my_set)        # 输出可能是 {1, 3, 4}，因为集合是无序的
```

### 函数参数

**1. 位置参数（Positional Arguments）**

位置参数是最常见的参数形式，它们按照函数定义时的顺序传递给函数。调用函数时，实参必须按照形参的顺序提供。

```python
def greet(name, greeting):
    print(f"{greeting}, {name}!")

greet("Alice", "Hello")  # 正确：Hello, Alice!
```

**2. 默认参数（Default Arguments）**

默认参数是带有默认值的参数。如果调用函数时没有为该参数提供值，则使用默认值。==默认参数总是放在非默认参数之后==。默认参数在函数被定义时就已创建，而非在程序运行时。

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")  # 使用默认值：Hello, Alice!
greet("Bob", "Hi")  # 提供了greeting参数：Hi, Bob!
```

```python
def buggy(arg, result = []):
    result.append(arg)
    print(result)
    
buggy('a') # ['a']
buggy('b') # ['a', 'b']
buggy('c', []) # ['c']
buggy('d') # ['a', 'b', 'd']
```

**3. 可变参数（Varargs 或 *args）**

可变参数允许你传递任意数量的位置参数给函数。在函数定义中，使用单星号 `*` 前缀一个参数名来接收这些参数，通常命名为 `*args`。

```python
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3))  # 输出: 6
print(sum_all(1, 2, 3, 4, 5))  # 输出: 15
```

**4. 关键字参数（Keyword Arguments 或 **kwargs）**

关键字参数允许你传递任意数量的关键字参数给函数。在函数定义中，使用双星号 `**` 前缀一个参数名来接收这些参数，通常命名为 `**kwargs`。

```python
def person(name, age, **kwargs):
    print('name:', name, 'age:', age, 'other:', kwargs)

person('Jack', 23)
person('Alice', 25, city='Beijing', job='Engineer')
"""
name: Jack age: 23 other: {}
name: Alice age: 25 other: {'city': 'Beijing', 'job': 'Engineer'}
"""
```

**5. 命名关键字参数（Named Keyword Arguments）**

命名关键字参数要求调用者明确地指定参数名，并且可以在函数定义中使用 `*` 来标记命名关键字参数的开始。==所有位于 `*` 后面的参数都必须以关键字的形式给出，注意是后面==。

```python
def greet(*, name, greeting):  # 这里的 * 表示之后的所有参数都是命名关键字参数
    print(f"{greeting}, {name}!")

greet(name="Alice", greeting="Hi")  # 正确
# greet("Alice", "Hi")  # 错误，需要使用关键字参数
```

**注意事项**

- 默认参数的值只会在函数定义时被计算一次，因此不应该使用可变对象作为默认参数值，除非你清楚这样做会带来的后果。
- 当同时使用位置参数、可变参数、关键字参数等混合类型的参数时，应该遵循一定的顺序：位置参数 -> 默认参数 -> *args -> 命名关键字参数 -> **kwargs。
  

例如：
```python
def example(pos1, pos2, default="default", *args, named_kwarg, **kwargs):
    pass
```

上述函数签名表明，`pos1` 和 `pos2` 是位置参数，`default` 是有默认值的位置参数，`*args` 接收额外的位置参数，`named_kwarg` 是命名关键字参数，而 `**kwargs` 接收额外的关键字参数。

### 作用域

查找顺序：L - E - G - B

**局部作用域 (Local Scope)**:

- 在一个函数内部定义的变量拥有局部作用域。
- 局部变量只能在其被定义的函数体内访问。
- 当函数执行完毕后，局部作用域就会消失，除非该函数返回了一个闭包。

**嵌套作用域 (Enclosing Scope)**:

- 这是指在另一个函数内部定义的函数，内部函数可以访问外部函数中的变量。
- 嵌套作用域允许内部函数访问其包围函数中定义的变量，只要这些变量不是局部变量。

**全局作用域 (Global Scope)**:

- 在最顶层的代码块（即不在任何函数或类定义之内）中定义的变量拥有全局作用域。
- 全局变量可以在整个模块的任何地方被访问，但是要在函数内部修改全局变量的话，需要使用`global`关键字声明。

**内置作用域 (Built-in Scope)**:

- 这是最外层的作用域，包含了所有内置函数和标准类型的名字。
- 内置作用域是Python本身提供的，包含了如`len`, `str`, `object`等名称。

#### 改变作用域

- global：将局部变量变为全局变量
- nonlocal：可在闭包函数中引用并使用闭包外部函数的变量（非全局）
- global可以用于任何地方，声明变量为全局变量（声明时，不能同时赋值）； 声明后再修改，则修改了全局变量的值。
- nonlocal的作用范围仅限于所在子函数的上一层函数中拥有的局部变量， 必须在上层函数中已经定义过，且非全局变量，否则报错。

### 闭包

嵌套、引用、返回

```python
def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent
    return exponent_of

square = nth_power(2)
cube = nth_power(3)
print(square(2)) # 4
print(cube(2)) # 8
```

```python
def deco():
    age = 10
    def wrapper():
        nonlocal age # 声明 age 为非局部变量
        age += 1
        print(age)
    return wrapper

deco()()  # 输出 11

# 存储返回的 wrapper 函数
increment_age = deco()

# 每次调用 increment_age，age 都会在上一次的基础上 +1
increment_age()  # 输出 11
increment_age()  # 输出 12
increment_age()  # 输出 13
```

任何一层子函数，若直接使用全局变量且不对其改变的话，则共享全局变量的 值；一旦子函数中改变该同名变量，则其降为该子函数所属的局部变量。

```python
def deco():
    age = 10
    def wrapper():
        print(age) # 这样是可以访问的
    return wrapper

deco()()  # 输出 10
```



### 其他

**逻辑运算符：**and, or, not

**成员运算符：**in, not in

**身份运算符：**is, is not

python中没有switch，相似的结构为match

表达式：由变量、运算符、常量和其他语法构造组成的组合，用于计算一个值。换句话说，表达式是为了求值而存在的。

语句：是程序中的指令，用于执行某个动作或命令。它是用来告诉计算机做什么事情的，而不是为了产生一个值。

```python
x + y           # 数学加法表达式
2 * (3 + 4)     # 包含括号的数学表达式
len(my_list)    # 函数调用作为表达式
x > y           # 比较操作符构成的布尔表达式

if x > 0:       # 条件语句
    print("Positive")   # 函数调用语句
for i in range(5):      # 循环语句
    print(i)
def my_function():      # 函数定义语句
    pass
x = 10                 # 变量赋值语句
```



#### 推导式

列表推导式、集合推导式、字典推导式

```python
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]
unique_squares = {x**2 for x in range(-3, 4)}
square_dict = {x: x**2 for x in range(5)}
```

还有生成器表达式

```python
gen_exp = (x**2 for x in range(5))
# 使用生成器
for num in gen_exp:
    print(num)
```



#### 匿名函数与高阶函数

高阶函数：能够接受函数作为参数或者返回函数作为结果的函数

Python 提供了一些内置的高阶函数，它们可以直接使用而无需额外导入：

- **`map(function, iterable, ...)`**: 将函数应用于所有输入列表的元素，并返回一个包含结果的迭代器。
- **`filter(function or None, iterable)`**: 构造一个迭代器，从输入迭代器中提取出使函数返回`True`的元素。
- **`reduce(function, sequence[, initial])`**: 对序列累积地应用二元函数function，从左到右，以便将其减少为单一值。（需从`functools`模块导入）
- **`sorted(iterable, *, key=None, reverse=False)`**: 返回一个新的已排序列表，可以指定排序规则。

```python
# 使用 map() 和 lambda 将列表中的每个元素平方
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # 输出: [1, 4, 9, 16]

# 使用 filter() 和 lambda 筛选出偶数
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 输出: [2, 4]

# 使用 reduce() 和 lambda 计算列表元素的乘积 (需从 functools 导入)
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 输出: 24

# 按照字典项的值进行排序
exam_res = {'Mike': 75, 'Judy': 88, 'Cris': 57}
sorted_items = sorted(exam_res.items(), key=lambda item: item[1], reverse=True)
print(sorted_items)  # 输出: [('Judy', 88), ('Mike', 75), ('Cris', 57)]
```







## Decorator

装饰器通常是一个以另一函数作为参数的函数，并返回一个新的函数。

1. **函数作为对象**：在Python中，函数是一等公民，意味着函数可以被赋值给变量、作为参数传递给其他函数、从函数中返回，甚至可以包含在数据结构中。
2. **内嵌函数**：可以在另一个函数内部定义函数，这种函数称为内嵌函数或局部函数。
3. **闭包（Closure）**：如果一个内嵌函数引用了外部作用域中的变量，并且这个内嵌函数在外部函数返回后仍然有效，那么就形成了闭包。闭包保留对外部作用域变量的访问权限。

```python
import time
def time_counter(fn):
    def wrapper():
        start = time.time()
        fn()
        end = time.time()
        return end - start
    return wrapper

@time_counter
def func():
    # func = time_counter(func)
    print("Hello, World!")

func() 
```















## Generator, Iterator









## OOP









## Exception











## 文件操作













## 模块、包、库