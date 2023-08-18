# 创建上下文管理器

在[《Python 完全自学教程》的第 12 章](https://lqpybook.readthedocs.io/en/latest/chapter12.html)中，以对文件的基本操作为例，简要说明了 `with` 语句和上下文管理器的应用，但由于该部分的重点在于讲解 `open()` 和 `read()` 函数，所以没有对上下文管理器进行深入解释，本文对此给予补充。

## 1. 定义上下文管理器对象

在 Python 中，关键词 `with` 能够调用上下文管理器（context manager），例如：

```python
>>> with open("example.txt", "w") as file:
...     file.write("Hello, world!")
...
13
>>> file.closed
True
```

上下文管理器，在 Python 中也是对象，因此，可以编写类实现此对象，其中最主要的是 `__enter__` 和 `__exit__` 两个方法，如下：

```python
class Example:
    def __enter__(self):
        print("enter")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")
```

如果用 `with` 调用上面所定义的上下文管理器，进入语句块后，首先调用 `__enter__` 方法，执行 `print("enter")` ，打印出字符串 `enter` ；而后执行语句块里面的语句；当退出 `with` 语句块的时候，要执行 `__exit__` 方法。

```python
>>> with Example():
...     print("Yay Python!")
...
enter
Yay Python!
exit
```

## 2. 应用举例

在下面的示例中，创建上下文管理器，并利用它暂时修改环境变量的值。

```python
import os

class SetEnvVar:
    def __init__(self, var_name, new_value):
        self.var_name = var_name
        self.new_value = new_value

    def __enter__(self):
        self.original_value = os.environ.get(self.var_name)
        os.environ[self.var_name] = self.new_value

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.original_value is None:
            del os.environ[self.var_name]
        else:
            os.environ[self.var_name] = self.original_value
```

在我所使用的计算机上，当前用户的是 `qiwsir` 。

```python
>>> import os
>>> print("USER env var is", os.environ["USER"])
USER env var is qiwsir
```

现在使用上面所创建的上下文管理器 `SetEnvVar` ，用关键词 `with` 创建语句块，将环境变量 `USER` 的值暂时修改为 `akin` 。

```python
>>> with SetEnvVar("USER", "akin"):
...     print("USER env var is", os.environ["USER"])
...
USER env var is akin
```

诚然，如果 `with` 语句块执行完毕，即退出之后，该环境变量的值还会恢复原值。

```python
>>> print("USER env var is", os.environ["USER"])
USER env var is qiwsir
```

得到上述效果，其原因就是在 `SetEnvVar` 类中定义了 `__enter__` 和 `__exit__` 两个方法，进入 `with` 语句块之后，执行 `__enter__` 方法，暂时修改环境变量的值；语句块结束，执行 `__exit__` 方法，将环境变量值恢复。

## 3. 关键词 `as` 的作用

在使用上下文管理器的语句块中，有时候还会用到 `as` 关键词，例如：

```python
>>> with SetEnvVar("USER", "akin") as result:
...     print("USER env var is", os.environ["USER"])
...     print("Result from __enter__ method:", result)
...
USER env var is akin
Result from __enter__ method: None
```

关键词 `as` 的作用是制定一个变量（上例中的 `result`），用于引用方法 `__enter__` 的返回值。当然，在 `SetEnvVar` 类中，方法 `__enter__` 没有 `return` 语句，也就是没有返回值，或者说默认返回值是 `None` ，故上面例子中打印出来的是 `None` 。

## 4. `__enter__` 的返回值

前面所创建的上下文管理器 `SetEnvVar` 的 `__enter__` 方法没有用 `return` 返回任何对象，下面看一个有返回值的例子。创建一个文件 `timer.py` ，其中的代码如下：

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = time.perf_counter()
        self.elapsed = self.stop - self.start
```

这个上下文管理器可以用量一个代码块的执行时间，在这里我们使用 `with` 发起代码块。

```python
>>> t = Timer()
>>> with t:
...     result = sum(range(10_000_000))
...
>>> t.elapsed
0.28711878502508625
```

如果没有忘记前面说过的 `as` 关键词，还可以用它写一种更简洁的方式：将创建实例和变量引用放在一行：

```python
>>> with Timer() as t:
...     result = sum(range(10_000_000))
...
>>> t.elapsed
0.3115791230229661
```

这是因为，在 `Timer` 类的 `__enter__` 方法中，有 `return self` ，返回了当前所创建的实例，即 `Timer()` ；再通过 `as` 关键词，将此实例对象引用给变量 `t` 。

这种方法在许多上下文管理器中都会用到，所以，定义上下文管理器时，`__enter__` 方法常常会 `return self` 。

## 5. `__exit__` 的参数

前面所定义的两个上下文管理器对象，其中的 `__exit__` 方法都含有 `exc_type, exc_val, exc_tb` 三个形参，对它们应该提供什么实参？这个方法的返回值是什么？

如果在 `with` 语句块中发生了异常，`__exit__` 方法的那个三个参数会分别引用异常类、异常实例和异常的 traceback 对象。但是，如果没有异常发生，三个参数都会引用 `None` 。

举个例子，就可以看到其中端倪。

创建名为 `log_exception.py` 的文件，并输入下面的代码：

```python
import logging

class LogException:
    def __init__(self, logger, level=logging.ERROR, suppress=False):
        self.logger, self.level, self.suppress = logger, level, suppress

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            info = (exc_type, exc_val, exc_tb)
            self.logger.log(self.level, "Exception occurred", exc_info=info)
            return self.suppress
        return False
```

如果在 `with` 语句块中有异常，利用上面所创建的上下文管理器，可以记录异常信息（使用了 `logging` 模块）。

再创建名为 `log_example.py` 的文件，代码如下：

```python
import logging
from log_exception import LogException

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("example")

with LogException(logger):
    result = 1 / 0  # This will cause a ZeroDivisionError
print("That's the end of our program")
```

显然，在上面的代码中，会发生异常。

```python
$ python log_example.py
ERROR:example:Exception occurred
Traceback (most recent call last):
  File "/home/trey/_/log_example.py", line 8, in <module>
    result = 1 / 0  # This will cause a ZeroDivisionError
             ~~^~~
ZeroDivisionError: division by zero
Traceback (most recent call last):
  File "/home/trey/_/log_example.py", line 8, in <module>
    result = 1 / 0  # This will cause a ZeroDivisionError
             ~~^~~
ZeroDivisionError: division by zero
```

注意观察上面报错信息的第二行：`ERROR:example:Exception occurred` ，这说明已经执行了 `__exit__` 方法。

并且，在上面看到了两行 Taceback 实例，第二个 Tracback 是由 Python 解释器自动生成的。

因为执行了 `__exit__` ，使得程序已经终止，所以 `log_example.py` 的最后一行 `print("That's the end of our program")` 就没有执行。

## 6. `__exit__` 的返回值

在调用上下文管理器对象的语句中，如果提供参数 `suppress=True` （在 `LogException` 类中，令 `suppress=False`），结果会大相径庭。改写 `log_example.py` 文件中的代码：

```python
import logging
from log_exception import LogException

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("example")

with LogException(logger, suppress=True):    # passed suppress=True to context manager
    result = 1 / 0  # This will cause a ZeroDivisionError
print("That's the end of our program")
```

再来执行 `log_example.py` ，观察效果：

```python
$ python3 log_example.py
ERROR:example:Exception occurred
Traceback (most recent call last):
  File "/home/trey/_/_/log_example.py", line 8, in <module>
    result = 1 / 0  # This will cause a ZeroDivisionError
             ~~^~~
ZeroDivisionError: division by zero
That's the end of our program
```

现在看到，除了之前的结果之外，还将该程序执行完毕了。这就是 `suppress` 参数的作用效果，上下文管理器用它把“异常压住”了。

```python
import logging

class LogException:
    ...

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            info = (exc_type, exc_val, exc_tb)
            self.logger.log(self.level, "Exception occurred", exc_info=info)
            return self.suppress
        return False
```

如果 `__exit__` 方法返回了 `True` 或者其他布尔值为真的对象，那么原本正在抛出的异常实际上就会被压制了。

默认情况下，`__exit__` 就像每个函数默认做的那样，返回 `None` ，`None` 的布尔值是 `False`，这与上述 `return False` 是一样的，此时，`__exit__` 方法就只会抛出异常，不会执行任何与默认不同的操作。

但是，如果最后是 `return True`，那么，异常将被压制。

## 7. `contextmanager` 装饰器

除了用上面的方法定义上下文管理器，还可以用生成器函数定义。但是要使用一个装饰器，即来自 `contextlib` 模块的 `contextmanager` 。

```python
from contextlib import contextmanager
import os


@contextmanager
def set_env_var(var_name, new_value):
    original_value = os.environ.get(var_name)
    os.environ[var_name] = new_value
    try:
        yield
    finally:
        if original_value is None:
            del os.environ[var_name]
        else:
            os.environ[var_name] = original_value
```

其实，在这个花哨的装饰器内部仍然涉及 `__enter__` 和 `__exit__` 方法。不过，用这个装饰器，的确是一种非常简单地创建上下文管理器的方法。



## 参考资料

[1]. 齐伟. Python 完全自学教程-编辑文件[DE/OL].[2023-08-18].https://lqpybook.readthedocs.io/en/latest/chapter12.html 

[2]. Trey Hunner. Creating a context manager in Python[DE/OL].(2023-08-07)[2023-08-18].https://www.pythonmorsels.com/creating-a-context-manager/