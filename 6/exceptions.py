'''
assert（断言）用于判断一个表达式，在表达式条件为false
的时候触发异常。
def test_is_factor():
    message = "{} is{} divisible by {}. Your function returned {}."

    true_tests = ((5412, 123), (4823, 371), (6975, 75), (624, 48), (9681, 3227), (4362, 3), (8502, 4251),
                  (5104, 4), (462, 7), (7110, 90), (3128, 4), (9610, 31), (3030, 101), (7644, 294),
                  (1990, 398), (1745, 1), (5577, 11), (4318, 2159), (2220, 12), (2543, 1))

    for a, b in true_tests:
        assert is_factor(a, b), message.format(a, "", b, False)

    false_tests = ((6890, 5059), (2259, 8304), (2697, 3094), (7702, 6643), (4957, 2694), (8872, 818),
                   (7369, 2772), (332, 718), (7293, 9220), (547, 7763), (5144, 3795), (2388, 9018),
                   (6781, 6152), (4365, 9086), (8492, 1194), (6553, 2871), (6535, 5371), (9712, 310),
                   (1881, 7671), (5360, 8180))

    for a, b in false_tests:
        assert not is_factor(a, b), message.format(a, " not", b, True)
'''

'''
Python 有两种错误很容易辨认：语法错误和异常。
'''
# 语法错误
# Python 的语法错误或者称之为解析错，是初学者经常碰到的，如下实例
# while True print('Hello world')

# 异常
# 即便 Python 程序的语法是正确的，在运行它的时候，也有可能发生错误。运行期检测到的错误被称为异常。
# 大多数的异常都不会被程序处理，都以错误信息的形式展现在这里:
# print(10 * (1/0))
# print(4 + spam * 3)
# print('2' + 2)

'''
异常处理
try/except...else...finally
'''
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
print('===================================================')
# try/except 语句还有一个可选的 else 子句，如果使用这个子句，那么必须放在所有的 except 子句之后。
# else 子句将在 try 子句没有发生任何异常的时候执行。
# finally子句无论异常是否发生都会执行。
try:
    f = open("a.txt", mode="r", encoding='utf-8')
    print(f.readline())
    print(f.readline())
# 一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组
except (IOError, NameError) as e:
    print(e)
finally:
    print('这句话，无论异常是否发生都会执行。')
    f.close()

'''
抛出异常
Python 使用 raise 语句抛出一个指定的异常。
'''
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')