# -*- coding: utf-8 -*-  # 指定源码文件使用 UTF-8 编码，确保中文注释不乱码
"""
Python函数与类知识大全  # 文件标题：一本可直接运行的 Python 函数与类教程脚本

使用方法：  # 说明如何使用本文件
1. 直接运行本文件：python Python函数与类知识大全.py  # 会按章节输出示例结果
2. 阅读每一章函数内部代码与注释  # 每一章都是一个独立知识点
3. 修改每个示例中的变量、参数和类  # 通过动手修改加深理解
4. 面试题在文件末尾的 INTERVIEW_QUESTIONS 列表中  # 可用于复习与自测

说明：  # 关于本教程的说明
- 本文件围绕“函数、参数、lambda、装饰器、类、魔术方法、描述符、元类、反射”等主题展开。  # 内容范围
- 示例追求清晰和可运行，而不是写成工程项目。  # 学习定位
- 运行输出较多，建议在终端或 IDE 中运行。  # 运行建议
"""


# ============================== 00. 公共工具函数 ==============================  # 分隔线：公共工具区


def print_title(title):  # 定义一个打印章节标题的函数
    print("\n" + "=" * 80)  # 打印上边界线，方便阅读输出
    print(title)  # 打印当前章节标题
    print("=" * 80)  # 打印下边界线，方便阅读输出


def safe_run(func):  # 定义一个安全运行章节函数的工具
    try:  # 尝试执行章节函数
        func()  # 调用传入的章节函数
    except Exception as error:  # 捕获示例中的异常，防止整个教程中断
        print(f"[章节运行异常] {func.__name__}: {error!r}")  # 打印异常信息，便于排查


# ============================== 01. 函数基础 ==============================  # 分隔线：第 1 章


def chapter_01_function_basic():  # 定义第 1 章演示函数
    print_title("01. 函数基础：def、调用、返回值")  # 打印章节标题

    def greet(name):  # 使用 def 定义函数，并声明一个形参 name
        message = f"你好，{name}"  # 在函数内部创建局部变量
        return message  # 使用 return 把结果返回给调用者

    result = greet("Python")  # 调用函数并把返回值保存到变量 result
    print(result)  # 输出函数返回值


# ============================== 02. 无返回值与 None ==============================  # 分隔线：第 2 章


def chapter_02_none_return():  # 定义第 2 章演示函数
    print_title("02. 无返回值函数：默认返回 None")  # 打印章节标题

    def log(message):  # 定义一个只负责打印的函数
        print(f"[日志] {message}")  # 打印日志内容
        # 没有显式 return 时，Python 会自动返回 None  # 解释默认返回值

    value = log("函数执行完成")  # 调用函数并接收返回值
    print(value)  # 输出 None，说明函数没有显式返回结果


# ============================== 03. 多返回值 ==============================  # 分隔线：第 3 章


def chapter_03_multi_return():  # 定义第 3 章演示函数
    print_title("03. 多返回值：本质是返回元组")  # 打印章节标题

    def analyze_score(score):  # 定义一个根据分数返回多个结果的函数
        passed = score >= 60  # 判断是否及格
        level = "优秀" if score >= 90 else "合格" if passed else "不合格"  # 根据分数生成等级
        return passed, level  # 返回两个值，本质上返回的是一个元组

    ok, text = analyze_score(88)  # 使用序列解包接收多个返回值
    print(ok, text)  # 输出解包后的结果


# ============================== 04. 文档字符串与类型注解 ==============================  # 分隔线：第 4 章


def chapter_04_docstring_type_hint():  # 定义第 4 章演示函数
    print_title("04. 文档字符串与类型注解")  # 打印章节标题

    def add(a: int, b: int) -> int:  # 使用类型注解说明参数和返回值类型
        """返回两个整数之和。"""  # 使用文档字符串说明函数作用
        return a + b  # 返回两个参数的加法结果

    print(add(3, 5))  # 调用函数并输出结果
    print(add.__doc__)  # 查看函数的文档字符串
    print(add.__annotations__)  # 查看函数的类型注解字典


# ============================== 05. 位置参数与关键字参数 ==============================  # 分隔线：第 5 章


def chapter_05_positional_keyword_args():  # 定义第 5 章演示函数
    print_title("05. 位置参数与关键字参数")  # 打印章节标题

    def introduce(name, age, city):  # 定义三个普通形参
        return f"{name}今年{age}岁，来自{city}"  # 返回格式化介绍文本

    print(introduce("小李", 20, "南京"))  # 使用位置参数调用，顺序必须正确
    print(introduce(city="杭州", age=22, name="小王"))  # 使用关键字参数调用，顺序可以改变
    print(introduce("小张", city="成都", age=21))  # 位置参数可以和关键字参数混用


# ============================== 06. 默认参数与可变默认值陷阱 ==============================  # 分隔线：第 6 章


def chapter_06_default_args():  # 定义第 6 章演示函数
    print_title("06. 默认参数与可变默认值陷阱")  # 打印章节标题

    def power(x, exponent=2):  # 定义默认参数 exponent，默认计算平方
        return x ** exponent  # 返回 x 的 exponent 次方

    print(power(5))  # 不传 exponent 时使用默认值 2
    print(power(5, 3))  # 传入 exponent 时覆盖默认值

    def append_bad(item, box=[]):  # 错误示例：可变默认值会在多次调用之间共享
        box.append(item)  # 向共享列表中追加元素
        return box  # 返回共享列表

    def append_good(item, box=None):  # 正确示例：默认值使用 None
        if box is None:  # 判断调用者是否传入列表
            box = []  # 每次未传入时创建一个新的列表
        box.append(item)  # 向当前列表追加元素
        return box  # 返回当前列表

    print(append_bad("A"))  # 第一次调用得到 ['A']
    print(append_bad("B"))  # 第二次调用会意外得到 ['A', 'B']
    print(append_good("A"))  # 正确写法第一次调用得到 ['A']
    print(append_good("B"))  # 正确写法第二次调用得到 ['B']


# ============================== 07. *args 收集位置参数 ==============================  # 分隔线：第 7 章


def chapter_07_args():  # 定义第 7 章演示函数
    print_title("07. *args：接收任意数量的位置参数")  # 打印章节标题

    def total(*numbers):  # 使用 *numbers 收集所有额外位置参数
        print(type(numbers))  # 输出 tuple，说明 *args 本质上收集为元组
        return sum(numbers)  # 对所有数字求和并返回

    print(total(1, 2, 3))  # 传入三个位置参数
    print(total(10, 20, 30, 40))  # 传入四个位置参数


# ============================== 08. **kwargs 收集关键字参数 ==============================  # 分隔线：第 8 章


def chapter_08_kwargs():  # 定义第 8 章演示函数
    print_title("08. **kwargs：接收任意数量的关键字参数")  # 打印章节标题

    def show_profile(**info):  # 使用 **info 收集所有额外关键字参数
        print(type(info))  # 输出 dict，说明 **kwargs 本质上收集为字典
        for key, value in info.items():  # 遍历字典中的键值对
            print(f"{key} -> {value}")  # 输出每一个关键字参数

    show_profile(name="小李", age=20, city="上海")  # 使用多个关键字参数调用


# ============================== 09. 参数顺序大全 ==============================  # 分隔线：第 9 章


def chapter_09_parameter_order():  # 定义第 9 章演示函数
    print_title("09. 参数顺序：普通参数、默认参数、*args、关键字-only、**kwargs")  # 打印章节标题

    def demo(a, b=10, *args, c=100, d=200, **kwargs):  # 展示 Python 函数参数的常见完整顺序
        print(f"a={a}")  # 输出普通参数
        print(f"b={b}")  # 输出默认参数
        print(f"args={args}")  # 输出额外位置参数
        print(f"c={c}, d={d}")  # 输出关键字-only 参数
        print(f"kwargs={kwargs}")  # 输出额外关键字参数

    demo(1, 2, 3, 4, c=5, x=6, y=7)  # 调用函数并覆盖多个参数


# ============================== 10. 仅限位置参数 / ==============================  # 分隔线：第 10 章


def chapter_10_positional_only():  # 定义第 10 章演示函数
    print_title("10. 仅限位置参数：斜杠 /")  # 打印章节标题

    def divide(a, b, /):  # 斜杠左侧参数只能按位置传入
        return a / b  # 返回除法结果

    print(divide(10, 2))  # 正确：按位置传入
    # divide(a=10, b=2)  # 错误：a 和 b 是仅限位置参数，不能用关键字传入


# ============================== 11. 仅限关键字参数 * ==============================  # 分隔线：第 11 章


def chapter_11_keyword_only():  # 定义第 11 章演示函数
    print_title("11. 仅限关键字参数：星号 *")  # 打印章节标题

    def connect(host, *, port, timeout=3):  # 星号右侧参数必须使用关键字传入
        return f"连接 {host}:{port}，超时={timeout}s"  # 返回模拟连接信息

    print(connect("localhost", port=8080))  # 正确：port 使用关键字传入
    # connect("localhost", 8080)  # 错误：port 是 keyword-only 参数


# ============================== 12. 参数解包调用 ==============================  # 分隔线：第 12 章


def chapter_12_unpack_call():  # 定义第 12 章演示函数
    print_title("12. 参数解包调用：*列表/元组 与 **字典")  # 打印章节标题

    def build_url(protocol, domain, path):  # 定义一个拼接 URL 的函数
        return f"{protocol}://{domain}/{path}"  # 返回拼接后的 URL

    parts = ("https", "example.com", "index.html")  # 准备用于 * 解包的位置参数
    options = {"protocol": "https", "domain": "python.org", "path": "downloads"}  # 准备用于 ** 解包的关键字参数
    print(build_url(*parts))  # 使用 * 把元组展开为位置参数
    print(build_url(**options))  # 使用 ** 把字典展开为关键字参数


# ============================== 13. 作用域 LEGB ==============================  # 分隔线：第 13 章


def chapter_13_scope_legb():  # 定义第 13 章演示函数
    print_title("13. 作用域：LEGB 规则")  # 打印章节标题
    name = "外层函数变量"  # Enclosing 作用域变量

    def inner():  # 定义内部函数
        name = "内部局部变量"  # Local 作用域变量
        print(name)  # 优先访问 Local 作用域

    inner()  # 调用内部函数
    print(name)  # 外层变量不受内部局部变量影响


# ============================== 14. global 与 nonlocal ==============================  # 分隔线：第 14 章


GLOBAL_COUNT = 0  # 定义一个模块级全局变量，用于 global 示例


def chapter_14_global_nonlocal():  # 定义第 14 章演示函数
    print_title("14. global 与 nonlocal")  # 打印章节标题

    def use_global():  # 定义修改全局变量的函数
        global GLOBAL_COUNT  # 声明使用模块级全局变量
        GLOBAL_COUNT += 1  # 修改全局变量

    def make_counter():  # 定义一个闭包计数器工厂函数
        count = 0  # 定义外层函数变量

        def counter():  # 定义内部计数函数
            nonlocal count  # 声明修改外层函数中的 count
            count += 1  # 修改外层函数变量
            return count  # 返回当前计数值

        return counter  # 返回内部函数，形成闭包

    use_global()  # 调用函数修改全局变量
    c = make_counter()  # 创建一个闭包计数器
    print(GLOBAL_COUNT)  # 输出全局变量
    print(c(), c(), c())  # 连续调用闭包计数器


# ============================== 15. 闭包 ==============================  # 分隔线：第 15 章


def chapter_15_closure():  # 定义第 15 章演示函数
    print_title("15. 闭包：函数记住外层变量")  # 打印章节标题

    def make_multiplier(factor):  # 定义一个创建乘法器的函数
        def multiply(number):  # 定义内部函数
            return number * factor  # 内部函数使用外层变量 factor

        return multiply  # 返回内部函数对象

    double = make_multiplier(2)  # 创建一个乘 2 的函数
    triple = make_multiplier(3)  # 创建一个乘 3 的函数
    print(double(10))  # 输出 20
    print(triple(10))  # 输出 30
    print(double.__closure__)  # 查看闭包中保存的变量单元


# ============================== 16. lambda 基础 ==============================  # 分隔线：第 16 章


def chapter_16_lambda_basic():  # 定义第 16 章演示函数
    print_title("16. lambda 基础：匿名函数")  # 打印章节标题

    square = lambda x: x * x  # 定义一个匿名函数并赋值给变量
    add = lambda a, b: a + b  # 定义一个接收两个参数的匿名函数
    print(square(6))  # 调用 lambda 计算平方
    print(add(3, 4))  # 调用 lambda 计算加法


# ============================== 17. lambda 与 sorted/map/filter ==============================  # 分隔线：第 17 章


def chapter_17_lambda_common_usage():  # 定义第 17 章演示函数
    print_title("17. lambda 高级用法：sorted、map、filter")  # 打印章节标题
    students = [{"name": "A", "score": 88}, {"name": "B", "score": 95}, {"name": "C", "score": 76}]  # 准备学生列表
    print(sorted(students, key=lambda item: item["score"], reverse=True))  # 按 score 从高到低排序
    print(list(map(lambda x: x * 10, [1, 2, 3])))  # 使用 map 批量处理数据
    print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])))  # 使用 filter 筛选偶数


# ============================== 18. lambda 与闭包延迟绑定 ==============================  # 分隔线：第 18 章


def chapter_18_lambda_late_binding():  # 定义第 18 章演示函数
    print_title("18. lambda 闭包陷阱：延迟绑定与默认参数修复")  # 打印章节标题
    bad_funcs = [lambda: i for i in range(3)]  # 错误示例：lambda 记住的是变量 i，不是当时的值
    good_funcs = [lambda i=i: i for i in range(3)]  # 正确示例：用默认参数保存当前 i 的值
    print([func() for func in bad_funcs])  # 输出 [2, 2, 2]
    print([func() for func in good_funcs])  # 输出 [0, 1, 2]


# ============================== 19. 递归函数 ==============================  # 分隔线：第 19 章


def chapter_19_recursion():  # 定义第 19 章演示函数
    print_title("19. 递归函数：函数调用自己")  # 打印章节标题

    def factorial(n):  # 定义阶乘函数
        if n <= 1:  # 递归终止条件
            return 1  # 返回最小问题的答案
        return n * factorial(n - 1)  # 把问题拆成 n 与 factorial(n-1)

    print(factorial(5))  # 输出 120


# ============================== 20. 高阶函数 ==============================  # 分隔线：第 20 章


def chapter_20_higher_order_function():  # 定义第 20 章演示函数
    print_title("20. 高阶函数：函数作为参数与返回值")  # 打印章节标题

    def apply_twice(func, value):  # 定义一个接收函数作为参数的函数
        return func(func(value))  # 对同一个值连续应用两次函数

    def plus_one(x):  # 定义一个普通函数
        return x + 1  # 返回加 1 的结果

    print(apply_twice(plus_one, 10))  # 输出 12
    print(apply_twice(lambda x: x * 2, 5))  # 输出 20


# ============================== 21. 装饰器基础 ==============================  # 分隔线：第 21 章


def chapter_21_decorator_basic():  # 定义第 21 章演示函数
    print_title("21. 装饰器基础：不修改原函数代码增强功能")  # 打印章节标题

    def log_decorator(func):  # 定义一个装饰器函数
        def wrapper(*args, **kwargs):  # 定义包装函数，接收任意参数
            print(f"准备调用：{func.__name__}")  # 调用前增加日志
            result = func(*args, **kwargs)  # 调用原始函数
            print(f"调用结束：{func.__name__}")  # 调用后增加日志
            return result  # 返回原始函数结果

        return wrapper  # 返回包装函数

    @log_decorator  # 使用装饰器语法修饰函数
    def say(text):  # 定义被装饰函数
        print(text)  # 输出文本内容

    say("你好，装饰器")  # 调用被装饰后的函数


# ============================== 22. functools.wraps ==============================  # 分隔线：第 22 章


def chapter_22_wraps():  # 定义第 22 章演示函数
    print_title("22. functools.wraps：保留原函数元信息")  # 打印章节标题
    from functools import wraps  # 导入 wraps 工具

    def log_decorator(func):  # 定义装饰器
        @wraps(func)  # 使用 wraps 保留 func 的 __name__ 和 __doc__
        def wrapper(*args, **kwargs):  # 定义包装函数
            return func(*args, **kwargs)  # 调用原函数并返回结果

        return wrapper  # 返回包装函数

    @log_decorator  # 使用装饰器
    def hello():  # 定义被装饰函数
        """这是 hello 函数的说明。"""  # 原函数文档字符串
        return "hello"  # 返回字符串

    print(hello.__name__)  # 输出 hello，而不是 wrapper
    print(hello.__doc__)  # 输出原函数文档字符串


# ============================== 23. 带参数的装饰器 ==============================  # 分隔线：第 23 章


def chapter_23_decorator_with_args():  # 定义第 23 章演示函数
    print_title("23. 带参数的装饰器")  # 打印章节标题
    from functools import wraps  # 导入 wraps 工具

    def repeat(times):  # 定义外层函数，用来接收装饰器参数
        def decorator(func):  # 定义真正的装饰器
            @wraps(func)  # 保留原函数元信息
            def wrapper(*args, **kwargs):  # 定义包装函数
                result = None  # 保存最后一次调用结果
                for _ in range(times):  # 根据参数 times 重复执行
                    result = func(*args, **kwargs)  # 调用原函数
                return result  # 返回最后一次结果

            return wrapper  # 返回包装函数

        return decorator  # 返回真正的装饰器

    @repeat(3)  # 使用带参数的装饰器
    def echo(text):  # 定义被装饰函数
        print(text)  # 输出文本

    echo("重复输出")  # 调用函数，会输出三次


# ============================== 24. 类装饰器 ==============================  # 分隔线：第 24 章


def chapter_24_class_decorator():  # 定义第 24 章演示函数
    print_title("24. 类装饰器：用对象实现装饰器")  # 打印章节标题

    class CountCalls:  # 定义一个可调用类，用作装饰器
        def __init__(self, func):  # 初始化时接收被装饰函数
            self.func = func  # 保存原函数
            self.count = 0  # 保存调用次数

        def __call__(self, *args, **kwargs):  # 让装饰器对象可以像函数一样被调用
            self.count += 1  # 每次调用时计数加一
            print(f"第 {self.count} 次调用")  # 输出调用次数
            return self.func(*args, **kwargs)  # 调用原函数并返回结果

    @CountCalls  # 使用类装饰器
    def work():  # 定义被装饰函数
        print("工作中")  # 输出模拟工作信息

    work()  # 第一次调用
    work()  # 第二次调用


# ============================== 25. 缓存装饰器 ==============================  # 分隔线：第 25 章


def chapter_25_cache_decorator():  # 定义第 25 章演示函数
    print_title("25. 缓存装饰器：functools.lru_cache")  # 打印章节标题
    from functools import lru_cache  # 导入内置缓存装饰器

    @lru_cache(maxsize=None)  # 为函数添加无限大小缓存
    def fib(n):  # 定义斐波那契函数
        if n < 2:  # 递归终止条件
            return n  # 返回 0 或 1
        return fib(n - 1) + fib(n - 2)  # 使用递归计算

    print(fib(20))  # 输出第 20 个斐波那契数
    print(fib.cache_info())  # 输出缓存命中情况


# ============================== 26. 生成器函数 yield ==============================  # 分隔线：第 26 章


def chapter_26_generator_basic():  # 定义第 26 章演示函数
    print_title("26. 生成器函数：yield")  # 打印章节标题

    def countdown(n):  # 定义生成器函数
        while n > 0:  # 当 n 大于 0 时继续生成
            yield n  # 产出当前 n，并暂停函数
            n -= 1  # 下次恢复执行时 n 减一

    for value in countdown(3):  # 遍历生成器对象
        print(value)  # 输出每次 yield 的值


# ============================== 27. yield from ==============================  # 分隔线：第 27 章


def chapter_27_yield_from():  # 定义第 27 章演示函数
    print_title("27. yield from：委托生成器")  # 打印章节标题

    def chain():  # 定义一个组合生成器
        yield from [1, 2, 3]  # 直接产出列表中的每个元素
        yield from "AB"  # 直接产出字符串中的每个字符

    print(list(chain()))  # 把生成器结果转换为列表输出


# ============================== 28. 迭代器协议 ==============================  # 分隔线：第 28 章


def chapter_28_iterator_protocol():  # 定义第 28 章演示函数
    print_title("28. 迭代器协议：__iter__ 与 __next__")  # 打印章节标题

    class CountUp:  # 定义一个可迭代计数器类
        def __init__(self, end):  # 初始化终止值
            self.current = 0  # 保存当前值
            self.end = end  # 保存终止值

        def __iter__(self):  # 返回迭代器对象本身
            return self  # self 同时也是迭代器

        def __next__(self):  # 返回下一个元素
            if self.current >= self.end:  # 判断是否迭代结束
                raise StopIteration  # 抛出 StopIteration 表示结束
            self.current += 1  # 当前值加一
            return self.current  # 返回当前值

    print(list(CountUp(5)))  # 把自定义迭代器转换为列表


# ============================== 29. 列表推导式与生成器表达式 ==============================  # 分隔线：第 29 章


def chapter_29_comprehension():  # 定义第 29 章演示函数
    print_title("29. 推导式：列表、字典、集合、生成器表达式")  # 打印章节标题
    nums = [1, 2, 3, 4, 5]  # 准备数字列表
    squares = [x * x for x in nums]  # 列表推导式生成平方列表
    even_map = {x: x * x for x in nums if x % 2 == 0}  # 字典推导式生成偶数平方映射
    unique = {x % 3 for x in nums}  # 集合推导式生成去重结果
    gen = (x * 10 for x in nums)  # 生成器表达式按需产生结果
    print(squares)  # 输出列表推导式结果
    print(even_map)  # 输出字典推导式结果
    print(unique)  # 输出集合推导式结果
    print(list(gen))  # 消费生成器表达式并输出结果


# ============================== 30. 类与对象基础 ==============================  # 分隔线：第 30 章


def chapter_30_class_basic():  # 定义第 30 章演示函数
    print_title("30. 类与对象基础")  # 打印章节标题

    class Student:  # 定义一个学生类
        school = "Python学院"  # 定义类属性，所有实例共享

        def __init__(self, name, score):  # 定义初始化方法
            self.name = name  # 定义实例属性 name
            self.score = score  # 定义实例属性 score

        def show(self):  # 定义实例方法
            return f"{self.name}：{self.score}分"  # 返回学生信息

    stu = Student("小李", 88)  # 创建 Student 实例
    print(stu.show())  # 调用实例方法
    print(Student.school)  # 通过类访问类属性


# ============================== 31. 实例属性与类属性 ==============================  # 分隔线：第 31 章


def chapter_31_instance_class_attr():  # 定义第 31 章演示函数
    print_title("31. 实例属性与类属性")  # 打印章节标题

    class Counter:  # 定义一个计数器类
        total = 0  # 类属性：记录创建过多少个实例

        def __init__(self):  # 初始化方法
            Counter.total += 1  # 每创建一个实例，类属性加一
            self.value = 0  # 实例属性：每个对象独立拥有

    a = Counter()  # 创建第一个对象
    b = Counter()  # 创建第二个对象
    a.value = 10  # 修改 a 的实例属性
    print(a.value, b.value)  # 输出实例属性，互不影响
    print(Counter.total)  # 输出类属性，所有实例共享


# ============================== 32. 实例方法、类方法、静态方法 ==============================  # 分隔线：第 32 章


def chapter_32_method_types():  # 定义第 32 章演示函数
    print_title("32. 实例方法、类方法、静态方法")  # 打印章节标题

    class Person:  # 定义 Person 类
        species = "Human"  # 定义类属性

        def __init__(self, name):  # 初始化实例
            self.name = name  # 保存实例名称

        def instance_method(self):  # 实例方法默认接收 self
            return self.name  # 可以访问实例属性

        @classmethod  # 声明类方法
        def class_method(cls):  # 类方法默认接收 cls
            return cls.species  # 可以访问类属性

        @staticmethod  # 声明静态方法
        def static_method(x, y):  # 静态方法不自动接收 self 或 cls
            return x + y  # 只做普通工具计算

    p = Person("小王")  # 创建实例
    print(p.instance_method())  # 调用实例方法
    print(Person.class_method())  # 调用类方法
    print(Person.static_method(1, 2))  # 调用静态方法


# ============================== 33. 封装与命名约定 ==============================  # 分隔线：第 33 章


def chapter_33_encapsulation():  # 定义第 33 章演示函数
    print_title("33. 封装：公开、保护、私有命名约定")  # 打印章节标题

    class BankAccount:  # 定义银行账户类
        def __init__(self, owner, balance):  # 初始化账户
            self.owner = owner  # 公开属性，外部可以直接访问
            self._status = "normal"  # 单下划线表示受保护约定
            self.__balance = balance  # 双下划线触发名称改写，避免外部误访问

        def get_balance(self):  # 提供公开方法访问私有余额
            return self.__balance  # 返回私有属性

    account = BankAccount("小李", 1000)  # 创建账户对象
    print(account.owner)  # 访问公开属性
    print(account.get_balance())  # 通过方法访问私有属性
    print(account._BankAccount__balance)  # 仍可通过改写后的名字访问，不是真正绝对私有


# ============================== 34. 继承 ==============================  # 分隔线：第 34 章


def chapter_34_inheritance():  # 定义第 34 章演示函数
    print_title("34. 继承：复用父类能力")  # 打印章节标题

    class Animal:  # 定义父类
        def speak(self):  # 定义父类方法
            return "动物发声"  # 返回默认声音

    class Dog(Animal):  # Dog 继承 Animal
        def wag_tail(self):  # 定义子类特有方法
            return "摇尾巴"  # 返回动作文本

    dog = Dog()  # 创建子类实例
    print(dog.speak())  # 子类对象可以调用父类方法
    print(dog.wag_tail())  # 子类对象也可以调用自己的方法


# ============================== 35. 方法重写与 super ==============================  # 分隔线：第 35 章


def chapter_35_override_super():  # 定义第 35 章演示函数
    print_title("35. 方法重写与 super")  # 打印章节标题

    class Animal:  # 定义父类
        def speak(self):  # 定义父类方法
            return "动物发声"  # 返回默认声音

    class Cat(Animal):  # 定义子类
        def speak(self):  # 子类重写父类方法
            parent = super().speak()  # 使用 super 调用父类方法
            return parent + "，猫叫：喵"  # 在父类结果基础上扩展

    cat = Cat()  # 创建子类实例
    print(cat.speak())  # 调用重写后的方法


# ============================== 36. 多继承与 MRO ==============================  # 分隔线：第 36 章


def chapter_36_mro():  # 定义第 36 章演示函数
    print_title("36. 多继承与 MRO 方法解析顺序")  # 打印章节标题

    class A:  # 定义父类 A
        def who(self):  # 定义方法
            return "A"  # 返回类名

    class B(A):  # B 继承 A
        def who(self):  # B 重写方法
            return "B"  # 返回类名

    class C(A):  # C 继承 A
        def who(self):  # C 重写方法
            return "C"  # 返回类名

    class D(B, C):  # D 同时继承 B 和 C
        pass  # 不重写 who，按照 MRO 查找

    d = D()  # 创建 D 实例
    print(d.who())  # 输出 B，因为 MRO 中 B 在 C 前
    print([cls.__name__ for cls in D.__mro__])  # 查看 D 的方法解析顺序


# ============================== 37. 多态与鸭子类型 ==============================  # 分隔线：第 37 章


def chapter_37_polymorphism():  # 定义第 37 章演示函数
    print_title("37. 多态与鸭子类型")  # 打印章节标题

    class Dog:  # 定义 Dog 类
        def speak(self):  # 定义同名方法
            return "汪汪"  # 返回狗叫

    class Cat:  # 定义 Cat 类
        def speak(self):  # 定义同名方法
            return "喵喵"  # 返回猫叫

    def make_sound(animal):  # 定义一个接收任意对象的函数
        print(animal.speak())  # 只关心对象有没有 speak 方法

    make_sound(Dog())  # 传入 Dog 对象
    make_sound(Cat())  # 传入 Cat 对象


# ============================== 38. property 属性 ==============================  # 分隔线：第 38 章


def chapter_38_property():  # 定义第 38 章演示函数
    print_title("38. property：把方法变成属性访问")  # 打印章节标题

    class Temperature:  # 定义温度类
        def __init__(self, celsius):  # 初始化摄氏度
            self._celsius = celsius  # 保存内部摄氏度

        @property  # 把方法声明为只读属性
        def celsius(self):  # 定义 getter
            return self._celsius  # 返回摄氏度

        @celsius.setter  # 定义 setter
        def celsius(self, value):  # 接收新摄氏度
            if value < -273.15:  # 检查绝对零度
                raise ValueError("温度不能低于绝对零度")  # 抛出异常
            self._celsius = value  # 保存合法温度

        @property  # 定义派生属性
        def fahrenheit(self):  # 获取华氏度
            return self._celsius * 9 / 5 + 32  # 摄氏度转华氏度

    temp = Temperature(25)  # 创建温度对象
    print(temp.celsius)  # 像访问属性一样访问 getter
    temp.celsius = 30  # 像设置属性一样调用 setter
    print(temp.fahrenheit)  # 访问派生属性


# ============================== 39. __slots__ ==============================  # 分隔线：第 39 章


def chapter_39_slots():  # 定义第 39 章演示函数
    print_title("39. __slots__：限制实例属性并节省内存")  # 打印章节标题

    class Point:  # 定义点类
        __slots__ = ("x", "y")  # 限制实例只能拥有 x 和 y 两个属性

        def __init__(self, x, y):  # 初始化点坐标
            self.x = x  # 设置 x 坐标
            self.y = y  # 设置 y 坐标

    p = Point(1, 2)  # 创建点对象
    print(p.x, p.y)  # 输出坐标
    # p.z = 3  # 错误：__slots__ 中没有 z，不能动态添加


# ============================== 40. 描述符 Descriptor 基础 ==============================  # 分隔线：第 40 章


def chapter_40_descriptor_basic():  # 定义第 40 章演示函数
    print_title("40. 描述符 Descriptor：控制属性访问")  # 打印章节标题

    class PositiveNumber:  # 定义一个数据描述符
        def __set_name__(self, owner, name):  # 类创建时自动调用，记录属性名
            self.private_name = "_" + name  # 创建内部保存用的属性名

        def __get__(self, instance, owner):  # 读取属性时自动调用
            if instance is None:  # 当通过类访问描述符时
                return self  # 返回描述符对象本身
            return getattr(instance, self.private_name, 0)  # 返回实例中保存的值

        def __set__(self, instance, value):  # 设置属性时自动调用
            if value <= 0:  # 检查值是否为正数
                raise ValueError("必须是正数")  # 非正数则报错
            setattr(instance, self.private_name, value)  # 把合法值保存到实例中

    class Product:  # 定义商品类
        price = PositiveNumber()  # 使用描述符管理 price 属性

        def __init__(self, price):  # 初始化商品价格
            self.price = price  # 触发描述符 __set__

    product = Product(99)  # 创建商品对象
    print(product.price)  # 触发描述符 __get__


# ============================== 41. 上下文管理器 with ==============================  # 分隔线：第 41 章


def chapter_41_context_manager_class():  # 定义第 41 章演示函数
    print_title("41. 上下文管理器：__enter__ 与 __exit__")  # 打印章节标题

    class ManagedResource:  # 定义一个上下文管理器类
        def __enter__(self):  # 进入 with 代码块时调用
            print("打开资源")  # 模拟打开资源
            return self  # 返回资源对象给 as 后面的变量

        def __exit__(self, exc_type, exc, traceback):  # 离开 with 代码块时调用
            print("关闭资源")  # 模拟关闭资源
            return False  # 返回 False 表示不吞掉异常

        def use(self):  # 定义资源使用方法
            print("使用资源")  # 模拟使用资源

    with ManagedResource() as resource:  # 使用 with 自动管理资源
        resource.use()  # 在上下文中使用资源


# ============================== 42. contextlib.contextmanager ==============================  # 分隔线：第 42 章


def chapter_42_contextlib():  # 定义第 42 章演示函数
    print_title("42. contextlib.contextmanager：用生成器写上下文管理器")  # 打印章节标题
    from contextlib import contextmanager  # 导入上下文管理器装饰器

    @contextmanager  # 把生成器函数转换为上下文管理器
    def open_resource():  # 定义生成器上下文管理器
        print("进入：准备资源")  # yield 之前相当于 __enter__
        try:  # 使用 try 保证退出逻辑执行
            yield "资源对象"  # yield 的值会赋给 as 后面的变量
        finally:  # finally 中写清理逻辑
            print("退出：清理资源")  # yield 之后相当于 __exit__

    with open_resource() as res:  # 使用自定义上下文管理器
        print(res)  # 输出资源对象


# ============================== 43. 反射机制 ==============================  # 分隔线：第 43 章


def chapter_43_reflection():  # 定义第 43 章演示函数
    print_title("43. 反射机制：getattr、setattr、hasattr、delattr")  # 打印章节标题

    class User:  # 定义用户类
        def __init__(self, name):  # 初始化用户名
            self.name = name  # 保存用户名

        def hello(self):  # 定义实例方法
            return f"你好，{self.name}"  # 返回问候语

    user = User("小李")  # 创建用户对象
    print(hasattr(user, "name"))  # 判断对象是否有 name 属性
    print(getattr(user, "name"))  # 动态获取 name 属性
    setattr(user, "age", 20)  # 动态设置 age 属性
    print(user.age)  # 输出动态添加的属性
    method = getattr(user, "hello")  # 动态获取方法对象
    print(method())  # 调用动态获取到的方法
    delattr(user, "age")  # 动态删除属性
    print(hasattr(user, "age"))  # 再次判断 age 是否存在


# ============================== 44. introspection 自省 ==============================  # 分隔线：第 44 章


def chapter_44_introspection():  # 定义第 44 章演示函数
    print_title("44. 自省：type、isinstance、issubclass、dir、vars")  # 打印章节标题

    class Animal:  # 定义父类
        pass  # 空类占位

    class Dog(Animal):  # 定义子类
        def __init__(self, name):  # 初始化名称
            self.name = name  # 保存实例属性

    dog = Dog("旺财")  # 创建对象
    print(type(dog))  # 查看对象类型
    print(isinstance(dog, Dog))  # 判断对象是否是 Dog 实例
    print(isinstance(dog, Animal))  # 判断对象是否是 Animal 实例
    print(issubclass(Dog, Animal))  # 判断 Dog 是否是 Animal 的子类
    print("name" in dir(dog))  # 使用 dir 查看对象属性和方法名
    print(vars(dog))  # 使用 vars 查看实例属性字典


# ============================== 45. 动态创建类 type ==============================  # 分隔线：第 45 章


def chapter_45_type_create_class():  # 定义第 45 章演示函数
    print_title("45. 动态创建类：type(name, bases, namespace)")  # 打印章节标题

    def say(self):  # 定义将放入类中的实例方法
        return f"我是{self.name}"  # 返回对象名称

    Person = type("Person", (object,), {"species": "Human", "say": say})  # 使用 type 动态创建类
    p = Person()  # 创建动态类的实例
    p.name = "动态对象"  # 动态添加实例属性
    print(Person.species)  # 访问动态类属性
    print(p.say())  # 调用动态加入的方法


# ============================== 46. 元类 Metaclass ==============================  # 分隔线：第 46 章


def chapter_46_metaclass_basic():  # 定义第 46 章演示函数
    print_title("46. 元类 Metaclass：控制类的创建过程")  # 打印章节标题

    class UpperAttrMeta(type):  # 定义元类，元类本身继承 type
        def __new__(mcls, name, bases, namespace):  # 在类对象创建前调用
            new_namespace = {}  # 准备新的命名空间字典
            for key, value in namespace.items():  # 遍历原始类命名空间
                if not key.startswith("__"):  # 跳过双下划线特殊属性
                    key = key.upper()  # 把普通属性名改为大写
                new_namespace[key] = value  # 保存到新的命名空间
            return super().__new__(mcls, name, bases, new_namespace)  # 创建类对象

    class Demo(metaclass=UpperAttrMeta):  # 使用自定义元类创建类
        language = "Python"  # 这个属性会被元类改成 LANGUAGE

    print(hasattr(Demo, "language"))  # 输出 False
    print(Demo.LANGUAGE)  # 输出 Python


# ============================== 47. 抽象基类 ABC ==============================  # 分隔线：第 47 章


def chapter_47_abc():  # 定义第 47 章演示函数
    print_title("47. 抽象基类 ABC：规定子类必须实现的方法")  # 打印章节标题
    from abc import ABC, abstractmethod  # 导入抽象基类工具

    class Shape(ABC):  # 定义抽象基类
        @abstractmethod  # 声明抽象方法
        def area(self):  # 子类必须实现面积方法
            pass  # 抽象方法不写具体逻辑

    class Rectangle(Shape):  # 定义子类并继承抽象基类
        def __init__(self, width, height):  # 初始化宽高
            self.width = width  # 保存宽度
            self.height = height  # 保存高度

        def area(self):  # 实现抽象方法
            return self.width * self.height  # 返回矩形面积

    rect = Rectangle(3, 4)  # 创建子类对象
    print(rect.area())  # 输出面积


# ============================== 48. dataclass ==============================  # 分隔线：第 48 章


def chapter_48_dataclass():  # 定义第 48 章演示函数
    print_title("48. dataclass：减少样板代码")  # 打印章节标题
    from dataclasses import dataclass, field  # 导入 dataclass 与 field

    @dataclass(order=True)  # 自动生成 __init__、__repr__、比较方法等
    class Student:  # 定义数据类
        score: int  # 定义排序优先字段
        name: str = field(compare=False)  # name 不参与排序比较

    a = Student(90, "A")  # 创建第一个学生
    b = Student(85, "B")  # 创建第二个学生
    print(a)  # 自动生成友好的 repr
    print(a > b)  # 使用自动生成的比较方法


# ============================== 49. namedtuple 与 Enum ==============================  # 分隔线：第 49 章


def chapter_49_namedtuple_enum():  # 定义第 49 章演示函数
    print_title("49. namedtuple 与 Enum")  # 打印章节标题
    from collections import namedtuple  # 导入 namedtuple
    from enum import Enum  # 导入枚举基类

    Point = namedtuple("Point", ["x", "y"])  # 创建带字段名的元组类型

    class Status(Enum):  # 定义枚举类
        PENDING = "pending"  # 等待状态
        DONE = "done"  # 完成状态

    p = Point(1, 2)  # 创建命名元组对象
    print(p.x, p.y)  # 通过字段名访问元组元素
    print(Status.DONE.name, Status.DONE.value)  # 输出枚举名和枚举值


# ============================== 50. 异常处理与自定义异常 ==============================  # 分隔线：第 50 章


def chapter_50_exception():  # 定义第 50 章演示函数
    print_title("50. 异常处理与自定义异常")  # 打印章节标题

    class BusinessError(Exception):  # 定义业务异常类
        pass  # 不额外扩展，仅用于区分异常类型

    def withdraw(balance, amount):  # 定义取款函数
        if amount > balance:  # 判断余额是否足够
            raise BusinessError("余额不足")  # 主动抛出自定义异常
        return balance - amount  # 返回取款后的余额

    try:  # 尝试执行可能出错的代码
        print(withdraw(100, 200))  # 余额不足，会抛出异常
    except BusinessError as error:  # 捕获指定业务异常
        print(f"捕获业务异常：{error}")  # 输出异常信息
    finally:  # 无论是否异常都会执行
        print("交易结束")  # 输出结束信息


# ============================== 51. 常见魔术方法总览类 ==============================  # 分隔线：第 51 章


def chapter_51_magic_methods():  # 定义第 51 章演示函数
    print_title("51. 常见魔术方法：30+ 个示例")  # 打印章节标题
    import copy  # 导入 copy 模块，用于复制魔术方法演示

    class MagicBox:  # 定义一个包含多种魔术方法的演示类
        def __new__(cls, *args, **kwargs):  # __new__ 控制对象创建
            instance = super().__new__(cls)  # 调用父类 __new__ 真正创建对象
            return instance  # 返回新对象

        def __init__(self, items):  # __init__ 控制对象初始化
            self.items = list(items)  # 保存元素列表

        def __repr__(self):  # __repr__ 面向开发者的字符串表示
            return f"MagicBox({self.items!r})"  # 返回可调试字符串

        def __str__(self):  # __str__ 面向用户的字符串表示
            return f"盒子里有 {len(self.items)} 个元素"  # 返回用户友好字符串

        def __len__(self):  # __len__ 支持 len(obj)
            return len(self.items)  # 返回元素数量

        def __bool__(self):  # __bool__ 支持 bool(obj)
            return bool(self.items)  # 空列表为 False，非空为 True

        def __contains__(self, item):  # __contains__ 支持 item in obj
            return item in self.items  # 判断元素是否存在

        def __getitem__(self, index):  # __getitem__ 支持 obj[index]
            return self.items[index]  # 返回指定索引元素

        def __setitem__(self, index, value):  # __setitem__ 支持 obj[index]=value
            self.items[index] = value  # 修改指定索引元素

        def __delitem__(self, index):  # __delitem__ 支持 del obj[index]
            del self.items[index]  # 删除指定索引元素

        def __iter__(self):  # __iter__ 支持 for 循环
            return iter(self.items)  # 返回内部列表的迭代器

        def __call__(self, item):  # __call__ 支持 obj(...)
            self.items.append(item)  # 调用对象时添加元素
            return self  # 返回自身，支持链式调用

        def __eq__(self, other):  # __eq__ 支持 ==
            return isinstance(other, MagicBox) and self.items == other.items  # 判断两个盒子内容是否相等

        def __lt__(self, other):  # __lt__ 支持 <
            return len(self) < len(other)  # 按长度比较大小

        def __hash__(self):  # __hash__ 支持 hash(obj)
            return hash(tuple(self.items))  # 把可变列表转成元组再计算哈希

        def __add__(self, other):  # __add__ 支持 obj + other
            return MagicBox(self.items + other.items)  # 返回新的盒子对象

        def __iadd__(self, other):  # __iadd__ 支持 obj += other
            self.items += other.items  # 原地追加另一个盒子的元素
            return self  # 返回自身

        def __bytes__(self):  # __bytes__ 支持 bytes(obj)
            return str(self.items).encode("utf-8")  # 把列表字符串编码为字节

        def __format__(self, spec):  # __format__ 支持 format(obj, spec)
            return format(str(self), spec)  # 使用字符串格式化逻辑

        def __int__(self):  # __int__ 支持 int(obj)
            return len(self.items)  # 用元素数量表示整数值

        def __float__(self):  # __float__ 支持 float(obj)
            return float(len(self.items))  # 用元素数量表示浮点值

        def __index__(self):  # __index__ 支持切片等需要整数索引的场景
            return len(self.items)  # 返回整数索引值

        def __round__(self, n=None):  # __round__ 支持 round(obj)
            return round(float(len(self.items)), n or 0)  # 对长度做 round

        def __copy__(self):  # __copy__ 支持 copy.copy(obj)
            return MagicBox(self.items.copy())  # 创建浅复制对象

        def __deepcopy__(self, memo):  # __deepcopy__ 支持 copy.deepcopy(obj)
            return MagicBox(copy.deepcopy(self.items, memo))  # 创建深复制对象

        def __getattr__(self, name):  # __getattr__ 在普通查找失败时调用
            return f"不存在的属性：{name}"  # 返回默认提示

        def __setattr__(self, name, value):  # __setattr__ 拦截所有属性设置
            object.__setattr__(self, name, value)  # 委托给 object 避免无限递归

        def __delattr__(self, name):  # __delattr__ 拦截属性删除
            object.__delattr__(self, name)  # 委托给 object 删除属性

        def __dir__(self):  # __dir__ 控制 dir(obj) 的结果
            return sorted(set(super().__dir__()) | {"custom_name"})  # 增加一个自定义名称

        def __enter__(self):  # __enter__ 支持 with obj as x
            print("进入 MagicBox 上下文")  # 输出进入信息
            return self  # 返回上下文对象

        def __exit__(self, exc_type, exc, tb):  # __exit__ 支持 with 退出逻辑
            print("退出 MagicBox 上下文")  # 输出退出信息
            return False  # 不吞掉异常

    box = MagicBox([1, 2, 3])  # 创建 MagicBox 对象
    print(repr(box))  # 调用 __repr__
    print(str(box))  # 调用 __str__
    print(len(box), bool(box))  # 调用 __len__ 与 __bool__
    print(2 in box)  # 调用 __contains__
    print(box[0])  # 调用 __getitem__
    box[1] = 99  # 调用 __setitem__
    print(list(box))  # 调用 __iter__
    box(100)  # 调用 __call__
    print(box + MagicBox([200]))  # 调用 __add__
    print(int(box), float(box))  # 调用 __int__ 与 __float__
    print(bytes(box))  # 调用 __bytes__
    print(box.not_exist)  # 调用 __getattr__
    with box as b:  # 调用 __enter__ 与 __exit__
        print(b)  # 在上下文中输出对象


# ============================== 52. 属性访问底层机制 ==============================  # 分隔线：第 52 章


def chapter_52_attribute_access():  # 定义第 52 章演示函数
    print_title("52. 属性访问底层机制：__getattribute__ 与 __getattr__")  # 打印章节标题

    class TraceAttr:  # 定义属性追踪类
        def __init__(self):  # 初始化对象
            self.name = "Python"  # 设置普通属性

        def __getattribute__(self, name):  # 拦截所有属性读取
            print(f"读取属性：{name}")  # 输出读取痕迹
            return object.__getattribute__(self, name)  # 必须委托 object，避免无限递归

        def __getattr__(self, name):  # 只有属性不存在时才调用
            return f"默认值：{name}"  # 返回默认值

    obj = TraceAttr()  # 创建对象
    print(obj.name)  # 读取存在属性，触发 __getattribute__
    print(obj.missing)  # 读取不存在属性，先触发 __getattribute__，失败后触发 __getattr__


# ============================== 53. 对象生命周期 ==============================  # 分隔线：第 53 章


def chapter_53_object_lifecycle():  # 定义第 53 章演示函数
    print_title("53. 对象生命周期：__new__、__init__、__del__")  # 打印章节标题

    class Life:  # 定义生命周期演示类
        def __new__(cls, name):  # 创建对象前调用
            print("__new__：创建对象")  # 输出创建阶段
            return super().__new__(cls)  # 返回实例对象

        def __init__(self, name):  # 对象创建后初始化
            print("__init__：初始化对象")  # 输出初始化阶段
            self.name = name  # 保存名称

        def __del__(self):  # 对象被垃圾回收时可能调用
            print("__del__：对象将被销毁")  # 输出销毁阶段

    obj = Life("demo")  # 创建对象
    print(obj.name)  # 使用对象属性
    del obj  # 删除引用，可能触发 __del__


# ============================== 54. 类钩子：__init_subclass__ ==============================  # 分隔线：第 54 章


def chapter_54_init_subclass():  # 定义第 54 章演示函数
    print_title("54. 类钩子：__init_subclass__")  # 打印章节标题

    class PluginBase:  # 定义插件基类
        plugins = []  # 保存所有子类插件

        def __init_subclass__(cls, **kwargs):  # 每当有子类继承时自动调用
            super().__init_subclass__(**kwargs)  # 调用父类实现
            PluginBase.plugins.append(cls)  # 自动注册子类

    class CsvPlugin(PluginBase):  # 定义一个插件子类
        pass  # 不需要手动注册

    class JsonPlugin(PluginBase):  # 定义另一个插件子类
        pass  # 不需要手动注册

    print([plugin.__name__ for plugin in PluginBase.plugins])  # 输出已注册插件


# ============================== 55. 泛型语法钩子：__class_getitem__ ==============================  # 分隔线：第 55 章


def chapter_55_class_getitem():  # 定义第 55 章演示函数
    print_title("55. 类下标钩子：__class_getitem__")  # 打印章节标题

    class Box:  # 定义普通类
        def __class_getitem__(cls, item):  # 当写 Box[int] 时调用
            return f"{cls.__name__}[{item.__name__}]"  # 返回自定义结果

    print(Box[int])  # 触发 __class_getitem__


# ============================== 56. 函数对象属性 ==============================  # 分隔线：第 56 章


def chapter_56_function_object():  # 定义第 56 章演示函数
    print_title("56. 函数也是对象：属性、赋值、传递")  # 打印章节标题

    def hello(name):  # 定义普通函数
        return f"Hello {name}"  # 返回问候语

    hello.version = "1.0"  # 给函数对象动态添加属性
    alias = hello  # 把函数对象赋值给另一个变量
    funcs = [hello, str.upper, lambda x: x[::-1]]  # 把函数对象放入列表
    print(alias("Python"))  # 通过别名调用函数
    print(hello.version)  # 读取函数对象属性
    print([func("abc") for func in funcs])  # 批量调用函数列表中的函数


# ============================== 57. 偏函数 partial ==============================  # 分隔线：第 57 章


def chapter_57_partial():  # 定义第 57 章演示函数
    print_title("57. 偏函数 partial：固定部分参数")  # 打印章节标题
    from functools import partial  # 导入 partial

    def power(base, exponent):  # 定义幂运算函数
        return base ** exponent  # 返回 base 的 exponent 次方

    square = partial(power, exponent=2)  # 固定 exponent=2，得到平方函数
    cube = partial(power, exponent=3)  # 固定 exponent=3，得到立方函数
    print(square(5))  # 输出 25
    print(cube(5))  # 输出 125


# ============================== 58. singledispatch 泛型函数 ==============================  # 分隔线：第 58 章


def chapter_58_singledispatch():  # 定义第 58 章演示函数
    print_title("58. singledispatch：根据第一个参数类型分发")  # 打印章节标题
    from functools import singledispatch  # 导入单分派装饰器

    @singledispatch  # 创建泛型函数
    def show(value):  # 默认处理逻辑
        return f"默认处理：{value}"  # 返回默认文本

    @show.register  # 注册 int 类型处理逻辑
    def _(value: int):  # 当第一个参数是 int 时调用
        return f"整数处理：{value * 2}"  # 返回整数处理结果

    @show.register  # 注册 list 类型处理逻辑
    def _(value: list):  # 当第一个参数是 list 时调用
        return f"列表处理：长度={len(value)}"  # 返回列表处理结果

    print(show("abc"))  # 使用默认处理
    print(show(10))  # 使用 int 处理
    print(show([1, 2, 3]))  # 使用 list 处理


# ============================== 59. 参数校验装饰器实战 ==============================  # 分隔线：第 59 章


def chapter_59_validate_decorator():  # 定义第 59 章演示函数
    print_title("59. 参数校验装饰器实战")  # 打印章节标题
    from functools import wraps  # 导入 wraps

    def require_positive(func):  # 定义要求参数为正数的装饰器
        @wraps(func)  # 保留原函数元信息
        def wrapper(*args, **kwargs):  # 包装函数接收任意参数
            values = list(args) + list(kwargs.values())  # 合并位置参数和关键字参数值
            if any(isinstance(v, (int, float)) and v <= 0 for v in values):  # 检查数字参数是否为正
                raise ValueError("数字参数必须为正数")  # 不满足条件则报错
            return func(*args, **kwargs)  # 参数合法则调用原函数

        return wrapper  # 返回包装函数

    @require_positive  # 应用参数校验装饰器
    def area(width, height):  # 定义面积函数
        return width * height  # 返回面积

    print(area(3, height=4))  # 输出合法面积
    # print(area(3, height=-4))  # 错误示例：负数会触发异常


# ============================== 60. 小型综合案例：插件式命令系统 ==============================  # 分隔线：第 60 章


def chapter_60_mini_project():  # 定义第 60 章演示函数
    print_title("60. 综合案例：函数、类、装饰器、反射组成插件式命令系统")  # 打印章节标题

    class CommandRegistry:  # 定义命令注册器类
        def __init__(self):  # 初始化注册器
            self.commands = {}  # 保存命令名到函数的映射

        def register(self, name):  # 定义带参数装饰器，用于注册命令
            def decorator(func):  # 定义真正的装饰器
                self.commands[name] = func  # 把命令名和函数保存到字典
                return func  # 返回原函数，避免破坏函数本身

            return decorator  # 返回装饰器

        def run(self, name, *args, **kwargs):  # 根据命令名运行命令
            if name not in self.commands:  # 判断命令是否存在
                raise KeyError(f"命令不存在：{name}")  # 不存在则报错
            return self.commands[name](*args, **kwargs)  # 调用已注册命令

    registry = CommandRegistry()  # 创建命令注册器

    @registry.register("add")  # 注册 add 命令
    def add(a, b):  # 定义加法命令
        return a + b  # 返回加法结果

    @registry.register("upper")  # 注册 upper 命令
    def upper(text):  # 定义大写转换命令
        return text.upper()  # 返回大写文本

    print(registry.run("add", 1, 2))  # 运行 add 命令
    print(registry.run("upper", "python"))  # 运行 upper 命令
    print(registry.commands.keys())  # 查看所有已注册命令


# ============================== 61. 常见魔术方法速查表 ==============================  # 分隔线：第 61 章


MAGIC_METHOD_CHEATSHEET = {  # 定义魔术方法速查字典
    "__new__": "创建对象时调用，先于 __init__",  # 解释 __new__
    "__init__": "初始化对象时调用",  # 解释 __init__
    "__del__": "对象销毁前可能调用",  # 解释 __del__
    "__repr__": "开发者友好的字符串表示",  # 解释 __repr__
    "__str__": "用户友好的字符串表示",  # 解释 __str__
    "__bytes__": "bytes(obj) 时调用",  # 解释 __bytes__
    "__format__": "format(obj) 时调用",  # 解释 __format__
    "__len__": "len(obj) 时调用",  # 解释 __len__
    "__bool__": "bool(obj) 时调用",  # 解释 __bool__
    "__hash__": "hash(obj) 时调用",  # 解释 __hash__
    "__eq__": "obj == other 时调用",  # 解释 __eq__
    "__ne__": "obj != other 时调用",  # 解释 __ne__
    "__lt__": "obj < other 时调用",  # 解释 __lt__
    "__le__": "obj <= other 时调用",  # 解释 __le__
    "__gt__": "obj > other 时调用",  # 解释 __gt__
    "__ge__": "obj >= other 时调用",  # 解释 __ge__
    "__add__": "obj + other 时调用",  # 解释 __add__
    "__sub__": "obj - other 时调用",  # 解释 __sub__
    "__mul__": "obj * other 时调用",  # 解释 __mul__
    "__truediv__": "obj / other 时调用",  # 解释 __truediv__
    "__floordiv__": "obj // other 时调用",  # 解释 __floordiv__
    "__mod__": "obj % other 时调用",  # 解释 __mod__
    "__pow__": "obj ** other 时调用",  # 解释 __pow__
    "__iadd__": "obj += other 时调用",  # 解释 __iadd__
    "__getitem__": "obj[key] 读取时调用",  # 解释 __getitem__
    "__setitem__": "obj[key]=value 时调用",  # 解释 __setitem__
    "__delitem__": "del obj[key] 时调用",  # 解释 __delitem__
    "__contains__": "item in obj 时调用",  # 解释 __contains__
    "__iter__": "iter(obj) 或 for 循环时调用",  # 解释 __iter__
    "__next__": "next(iterator) 时调用",  # 解释 __next__
    "__call__": "obj(...) 时调用",  # 解释 __call__
    "__enter__": "进入 with 代码块时调用",  # 解释 __enter__
    "__exit__": "退出 with 代码块时调用",  # 解释 __exit__
    "__getattr__": "属性不存在时调用",  # 解释 __getattr__
    "__getattribute__": "所有属性读取时调用",  # 解释 __getattribute__
    "__setattr__": "设置属性时调用",  # 解释 __setattr__
    "__delattr__": "删除属性时调用",  # 解释 __delattr__
    "__dir__": "dir(obj) 时调用",  # 解释 __dir__
    "__copy__": "copy.copy(obj) 时调用",  # 解释 __copy__
    "__deepcopy__": "copy.deepcopy(obj) 时调用",  # 解释 __deepcopy__
    "__set_name__": "描述符绑定到类属性名时调用",  # 解释 __set_name__
    "__init_subclass__": "创建子类时调用",  # 解释 __init_subclass__
    "__class_getitem__": "类使用下标语法时调用，如 Box[int]",  # 解释 __class_getitem__
}  # 魔术方法速查字典结束


def chapter_61_magic_cheatsheet():  # 定义第 61 章演示函数
    print_title("61. 常见魔术方法速查表")  # 打印章节标题
    for name, meaning in list(MAGIC_METHOD_CHEATSHEET.items())[:12]:  # 只打印前 12 个，避免输出过长
        print(f"{name}: {meaning}")  # 输出魔术方法说明
    print(f"共收录 {len(MAGIC_METHOD_CHEATSHEET)} 个常见魔术方法")  # 输出收录数量


# ============================== 62. 学习路线建议 ==============================  # 分隔线：第 62 章


def chapter_62_learning_route():  # 定义第 62 章演示函数
    print_title("62. 学习路线：如何系统掌握函数与类")  # 打印章节标题
    route = [  # 定义学习路线列表
        "1. 先掌握函数定义、参数、返回值、作用域",  # 路线第一步
        "2. 再掌握 lambda、闭包、高阶函数、装饰器",  # 路线第二步
        "3. 接着学习类、对象、继承、多态、property",  # 路线第三步
        "4. 然后学习魔术方法、迭代器、上下文管理器",  # 路线第四步
        "5. 最后学习描述符、反射、元类等高级对象模型",  # 路线第五步
        "6. 每学完一章，自己改参数、改类名、改输出，再运行验证",  # 路线第六步
    ]  # 学习路线列表结束
    for item in route:  # 遍历学习路线
        print(item)  # 输出每一步建议


# ============================== 63. 面试题题库：100+ ==============================  # 分隔线：第 63 章


INTERVIEW_QUESTIONS = [  # 定义 Python 函数与类常见面试题列表
    "001. Python 中函数为什么也是对象？请举例说明。",  # 面试题 001
    "002. def 定义函数和 lambda 定义函数有什么区别？",  # 面试题 002
    "003. 函数没有 return 时返回什么？",  # 面试题 003
    "004. return 一个逗号分隔的多个值时，底层返回的是什么类型？",  # 面试题 004
    "005. 位置参数和关键字参数有什么区别？",  # 面试题 005
    "006. 默认参数在什么时候被创建？为什么可变默认参数危险？",  # 面试题 006
    "007. 如何安全地使用列表作为函数默认参数？",  # 面试题 007
    "008. *args 的本质是什么？",  # 面试题 008
    "009. **kwargs 的本质是什么？",  # 面试题 009
    "010. Python 函数参数的完整顺序是什么？",  # 面试题 010
    "011. 仅限位置参数 / 有什么作用？",  # 面试题 011
    "012. 仅限关键字参数 * 有什么作用？",  # 面试题 012
    "013. 调用函数时 * 和 ** 分别表示什么？",  # 面试题 013
    "014. LEGB 作用域规则分别代表什么？",  # 面试题 014
    "015. global 和 nonlocal 的区别是什么？",  # 面试题 015
    "016. 什么是闭包？闭包有什么使用场景？",  # 面试题 016
    "017. lambda 在循环中为什么可能出现延迟绑定问题？",  # 面试题 017
    "018. 如何修复 lambda 延迟绑定问题？",  # 面试题 018
    "019. 什么是高阶函数？",  # 面试题 019
    "020. map、filter、sorted 中 lambda 的典型用法是什么？",  # 面试题 020
    "021. 装饰器的本质是什么？",  # 面试题 021
    "022. 为什么装饰器内部通常要写 *args 和 **kwargs？",  # 面试题 022
    "023. functools.wraps 的作用是什么？",  # 面试题 023
    "024. 如何写一个带参数的装饰器？",  # 面试题 024
    "025. 类装饰器为什么要实现 __call__？",  # 面试题 025
    "026. lru_cache 的使用场景是什么？",  # 面试题 026
    "027. 递归函数必须具备什么条件？",  # 面试题 027
    "028. 生成器函数和普通函数有什么区别？",  # 面试题 028
    "029. yield 和 return 有什么区别？",  # 面试题 029
    "030. yield from 的作用是什么？",  # 面试题 030
    "031. 什么是迭代器协议？",  # 面试题 031
    "032. __iter__ 和 __next__ 分别负责什么？",  # 面试题 032
    "033. 可迭代对象和迭代器有什么区别？",  # 面试题 033
    "034. 列表推导式和生成器表达式有什么区别？",  # 面试题 034
    "035. 类和对象的区别是什么？",  # 面试题 035
    "036. 实例属性和类属性有什么区别？",  # 面试题 036
    "037. self 代表什么？",  # 面试题 037
    "038. cls 代表什么？",  # 面试题 038
    "039. 实例方法、类方法和静态方法的区别是什么？",  # 面试题 039
    "040. @classmethod 常用于哪些场景？",  # 面试题 040
    "041. @staticmethod 常用于哪些场景？",  # 面试题 041
    "042. 单下划线属性和双下划线属性有什么区别？",  # 面试题 042
    "043. Python 中是否存在真正的私有属性？",  # 面试题 043
    "044. 什么是继承？",  # 面试题 044
    "045. 方法重写是什么？",  # 面试题 045
    "046. super() 的作用是什么？",  # 面试题 046
    "047. 多继承中 MRO 是什么？",  # 面试题 047
    "048. Python 使用什么算法计算 MRO？",  # 面试题 048
    "049. 什么是多态？",  # 面试题 049
    "050. 什么是鸭子类型？",  # 面试题 050
    "051. property 的作用是什么？",  # 面试题 051
    "052. property 的 getter、setter、deleter 怎么写？",  # 面试题 052
    "053. __slots__ 的作用是什么？",  # 面试题 053
    "054. 使用 __slots__ 有什么限制？",  # 面试题 054
    "055. 描述符是什么？",  # 面试题 055
    "056. 数据描述符和非数据描述符有什么区别？",  # 面试题 056
    "057. __get__、__set__、__delete__ 分别什么时候调用？",  # 面试题 057
    "058. __set_name__ 的作用是什么？",  # 面试题 058
    "059. with 语句的底层协议是什么？",  # 面试题 059
    "060. __enter__ 和 __exit__ 分别负责什么？",  # 面试题 060
    "061. contextlib.contextmanager 的原理是什么？",  # 面试题 061
    "062. 反射机制有哪些常用函数？",  # 面试题 062
    "063. getattr 和 __getattr__ 有什么区别？",  # 面试题 063
    "064. setattr 和 __setattr__ 有什么区别？",  # 面试题 064
    "065. hasattr 的底层大概如何工作？",  # 面试题 065
    "066. type(obj) 和 obj.__class__ 有什么关系？",  # 面试题 066
    "067. isinstance 和 type 判断类型有什么区别？",  # 面试题 067
    "068. issubclass 的作用是什么？",  # 面试题 068
    "069. dir 和 vars 有什么区别？",  # 面试题 069
    "070. 如何使用 type 动态创建类？",  # 面试题 070
    "071. 元类是什么？",  # 面试题 071
    "072. 类也是对象这句话如何理解？",  # 面试题 072
    "073. metaclass 在类创建流程中如何工作？",  # 面试题 073
    "074. __new__ 和 __init__ 的区别是什么？",  # 面试题 074
    "075. __del__ 为什么不适合承担关键资源释放逻辑？",  # 面试题 075
    "076. __repr__ 和 __str__ 有什么区别？",  # 面试题 076
    "077. __len__ 和 __bool__ 如何影响对象真假判断？",  # 面试题 077
    "078. __eq__ 和 __hash__ 为什么经常一起考虑？",  # 面试题 078
    "079. 可哈希对象需要满足什么条件？",  # 面试题 079
    "080. __getitem__ 除了索引访问还能支持什么？",  # 面试题 080
    "081. __contains__ 如何影响 in 运算符？",  # 面试题 081
    "082. __call__ 可以用来实现什么设计？",  # 面试题 082
    "083. __getattribute__ 为什么容易造成无限递归？",  # 面试题 083
    "084. 如何在 __getattribute__ 中安全访问属性？",  # 面试题 084
    "085. __init_subclass__ 适合什么场景？",  # 面试题 085
    "086. __class_getitem__ 和泛型语法有什么关系？",  # 面试题 086
    "087. dataclass 自动生成哪些方法？",  # 面试题 087
    "088. dataclass 中 field(compare=False) 有什么作用？",  # 面试题 088
    "089. namedtuple 和普通 tuple 相比有什么优势？",  # 面试题 089
    "090. Enum 的 name 和 value 分别是什么？",  # 面试题 090
    "091. 自定义异常为什么通常继承 Exception？",  # 面试题 091
    "092. try/except/else/finally 的执行顺序是什么？",  # 面试题 092
    "093. raise 的作用是什么？",  # 面试题 093
    "094. partial 的作用是什么？",  # 面试题 094
    "095. singledispatch 的分发依据是什么？",  # 面试题 095
    "096. Python 中函数注解会强制类型检查吗？",  # 面试题 096
    "097. __annotations__ 保存了什么？",  # 面试题 097
    "098. 文档字符串 __doc__ 有什么作用？",  # 面试题 098
    "099. 函数内部修改列表参数会影响外部对象吗？为什么？",  # 面试题 099
    "100. 不可变对象作为参数传递时是否会复制对象？",  # 面试题 100
    "101. Python 参数传递是值传递还是引用传递？",  # 面试题 101
    "102. 浅拷贝和深拷贝的区别是什么？",  # 面试题 102
    "103. copy.copy 会触发哪个魔术方法？",  # 面试题 103
    "104. copy.deepcopy 会触发哪个魔术方法？",  # 面试题 104
    "105. 如何设计一个可迭代的自定义类？",  # 面试题 105
    "106. 如何设计一个支持下标访问的自定义类？",  # 面试题 106
    "107. 如何设计一个支持 with 的资源类？",  # 面试题 107
    "108. 如何设计一个可以像函数一样调用的对象？",  # 面试题 108
    "109. 如何实现一个简易插件注册系统？",  # 面试题 109
    "110. 学习元类前必须先理解哪些概念？",  # 面试题 110
]  # 面试题列表结束


def chapter_63_interview_questions():  # 定义第 63 章演示函数
    print_title("63. 面试题题库：100+ 常见问题")  # 打印章节标题
    print(f"本题库共 {len(INTERVIEW_QUESTIONS)} 道题。")  # 输出题目数量
    for question in INTERVIEW_QUESTIONS[:10]:  # 只打印前 10 题，避免运行输出过长
        print(question)  # 输出题目文本
    print("其余题目请在 INTERVIEW_QUESTIONS 列表中查看。")  # 提示查看完整题库


# ============================== 64. 主入口 ==============================  # 分隔线：主入口区


CHAPTERS = [  # 定义章节函数列表
    chapter_01_function_basic,  # 第 1 章
    chapter_02_none_return,  # 第 2 章
    chapter_03_multi_return,  # 第 3 章
    chapter_04_docstring_type_hint,  # 第 4 章
    chapter_05_positional_keyword_args,  # 第 5 章
    chapter_06_default_args,  # 第 6 章
    chapter_07_args,  # 第 7 章
    chapter_08_kwargs,  # 第 8 章
    chapter_09_parameter_order,  # 第 9 章
    chapter_10_positional_only,  # 第 10 章
    chapter_11_keyword_only,  # 第 11 章
    chapter_12_unpack_call,  # 第 12 章
    chapter_13_scope_legb,  # 第 13 章
    chapter_14_global_nonlocal,  # 第 14 章
    chapter_15_closure,  # 第 15 章
    chapter_16_lambda_basic,  # 第 16 章
    chapter_17_lambda_common_usage,  # 第 17 章
    chapter_18_lambda_late_binding,  # 第 18 章
    chapter_19_recursion,  # 第 19 章
    chapter_20_higher_order_function,  # 第 20 章
    chapter_21_decorator_basic,  # 第 21 章
    chapter_22_wraps,  # 第 22 章
    chapter_23_decorator_with_args,  # 第 23 章
    chapter_24_class_decorator,  # 第 24 章
    chapter_25_cache_decorator,  # 第 25 章
    chapter_26_generator_basic,  # 第 26 章
    chapter_27_yield_from,  # 第 27 章
    chapter_28_iterator_protocol,  # 第 28 章
    chapter_29_comprehension,  # 第 29 章
    chapter_30_class_basic,  # 第 30 章
    chapter_31_instance_class_attr,  # 第 31 章
    chapter_32_method_types,  # 第 32 章
    chapter_33_encapsulation,  # 第 33 章
    chapter_34_inheritance,  # 第 34 章
    chapter_35_override_super,  # 第 35 章
    chapter_36_mro,  # 第 36 章
    chapter_37_polymorphism,  # 第 37 章
    chapter_38_property,  # 第 38 章
    chapter_39_slots,  # 第 39 章
    chapter_40_descriptor_basic,  # 第 40 章
    chapter_41_context_manager_class,  # 第 41 章
    chapter_42_contextlib,  # 第 42 章
    chapter_43_reflection,  # 第 43 章
    chapter_44_introspection,  # 第 44 章
    chapter_45_type_create_class,  # 第 45 章
    chapter_46_metaclass_basic,  # 第 46 章
    chapter_47_abc,  # 第 47 章
    chapter_48_dataclass,  # 第 48 章
    chapter_49_namedtuple_enum,  # 第 49 章
    chapter_50_exception,  # 第 50 章
    chapter_51_magic_methods,  # 第 51 章
    chapter_52_attribute_access,  # 第 52 章
    chapter_53_object_lifecycle,  # 第 53 章
    chapter_54_init_subclass,  # 第 54 章
    chapter_55_class_getitem,  # 第 55 章
    chapter_56_function_object,  # 第 56 章
    chapter_57_partial,  # 第 57 章
    chapter_58_singledispatch,  # 第 58 章
    chapter_59_validate_decorator,  # 第 59 章
    chapter_60_mini_project,  # 第 60 章
    chapter_61_magic_cheatsheet,  # 第 61 章
    chapter_62_learning_route,  # 第 62 章
    chapter_63_interview_questions,  # 第 63 章
]  # 章节函数列表结束


def main():  # 定义主函数
    print_title("Python函数与类知识大全：可运行教程")  # 打印总标题
    for chapter in CHAPTERS:  # 遍历所有章节函数
        safe_run(chapter)  # 安全运行当前章节
    print_title("教程运行结束")  # 打印结束标题
    print("建议：不要只看输出，请逐章修改代码并重新运行。")  # 输出学习建议


if __name__ == "__main__":  # 判断当前文件是否作为脚本直接运行
    main()  # 调用主函数，开始运行全部章节
