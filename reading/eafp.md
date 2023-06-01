# EAFP 原则

EAFP 原则是 Python 世界中的一个基本缩写词汇，与诸如 KISS（kep it simple, stupid!）和 DRY（don't repeat yourself）等一样。EAFP 表示“it's **E**asier to **A**sk for **F**orgiveness than **P**ermission.”（请求原谅比请求许可更容易）。
但是，这意味着什么呢？

简而言之，这意味着应该意识到 Python 中的 `try：... except：...` 语法非常有用，可以放心使用！

## try: ... except: ...

先看下面的代码段

```
while True:
    try:
        num = int(input("Integer >>> "))
        break
    except ValueError:
        print("Please write a valid integer!")

print(f"Your integer was {num}.")
```

这段代码是什么意思？

在上述代码中，创建了一个无限循环，直到当用户输入一个有效的整数才终止循环。为此，使用了 `try: ... except: ...` 语句。

## Try

关键词 `try` 的作用是用于捕获其下的语句块中的代码在程序运行时可能出现的错误。

我们希望用户输入一个有效的整数，以便可以转换并将其赋值给`num` ，但我们不知道用户实际上会输入什么。如果用户输入类似于 `asdfasfd` 或 `12.4`，调用 `int(...)` 时就会抛出 `ValueError` 错误。当用户犯错误时，我们希望让他们有机会改正，这就是 `except: ...` 的用途。

## Except

关键词 `except` 的作用是：只有当 `try` 下面的程序在运行时报错了，`excep` 才被唤醒。

如上面代码那样，如果用户输入了不能被转化为整数的对象，在调用 `int()` 的时候就会抛出 `ValueError` 异常，并且程序会跳转到 `except ValueError: ...` 部分。

注意，你必须在编写 `except` 之前能够正确地预计到 `try` 中的错误类型。比如上面代码中，预计会爆出 `ValueError` 异常，那么就写 `except ValueError` ，如果预计的是 `TypeError` 类型的异常，就写 `except TypeError` 。

## 不要只用一个 except

Python 语法允许这样的代码：

```
try:
    num = int(input("Integer >>> "))
except:
    print("Please write a valid integer!")
```

在这段代码中，移除了 `except` 后面的异常类型 `ValueError` 。

这就是告诉 Python 程序，不论 `try` 下面的程序中爆出什么类型的错误和异常，都应该被 `except` 捕获。像这种不对特定异常进行处理的情景，我们可称之为“bare except” 。

写“bare except”不是好习惯，应该禁止。

原因何在？针对上面的代码，举个例子说明。如果用户输入的是 `Ctrl + C` ，其本意是要终止循环并退出程序，但实际上对于以上代码，因为这种输入对 `try` 而言是 `KeyboardInterrupterror` 异常，“bare except” 会捕获所有异常，也包括这种。也就是说，程序在退出之前还会执行 `except` 下面的代码，这或许并不是我们希望的。

同样的道理，也应该避免使用 `except Exception: ` 这种写法。

最好的写法，就是要在 `except` 后面指明异常类型，然后在代码块中对这种异常进行处理。