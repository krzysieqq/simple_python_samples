import warnings


def fn(a):
    s=0
    if a>100:
        warnings.warn('Long Wait...')
    for i in range(a):
        s+=i
    return s


print("Start...")
print(fn(1000))
print("Ending...")

# python -W ignore ./demo.py
# Start...
# 499500
# Ending...

# export PYTHONWARNINGS=ignore
# python ./demo.py
# Start...
# 499500
# Ending...
#
# warnings.filterwarnings('ignore', '.*')
#
# print(fn(1000))

# export PYTHONWARNINGS=error
# python ./demo.py
# Start...
# Traceback (most recent call last):
#   File "./demo.py", line 25, in <module>
#     print(fn(1000))
#   File "./demo.py", line 14, in fn
#     warnings.warn('Long Wait...')
# UserWarning: Long Wait...

# python 2.7
# print >> sys.stderr, "Wrong Argument..."

# python 3.6
# print("Wrong Argument", file=sys.stderr)

# import sys
#
# if arg1>0:
#     sys.stderr.write("Wrong Argument...\n")
#     exit(1)

print("start")
try:
    print("start try block")
    f = open("file1")
    print("end try block")
except Exception:
    print("error opening file")

print("end")

print("start")
try:
    print("start try block")
    f = open("file1")
    print("end try block")
except IOError:
    print("error opening file")
except (OSError,NameError):
    print("OS/Name problem")
except Exception:
    print("All other Exceptions")
print("end")

print("start")
try:
    print("start try block")
    f = open("file1")
    print("end try block")
except IOError as errobj:
    print("error opening file:",errobj)
else:
    print("No Exceptions")

print("end")


def f2():
    try:
        print("f2")
        f = open("file1")
    except Exception as e:
        print("Exception in f2")
    else:
        print("No Exceptions")


def f1():
    try:
        print("start try block")
        f2()
        print("end try block")
    except Exception:
        print("Exception in f1")


print("start")
f1()
print("end")


def f2():
    try:
        print("f2")
    except Exception as e:
        print("Exception in f2")
    else:
        print("No Exceptions")
        f = open("file1")


def f1():
    try:
        print("start try block")
        f2()
        print("end try block")
    except Exception:
        print("Exception in f1")


print("start")
f1()
print("end")

print("start")
try:
    print("start try block")
    f = open("file1")
    print("end try block")
except IOError as errobj:
    print("error opening file:",errobj)
else:
    print("No Exceptions")
finally:
    print("Always Executed")
print("end")


def f2(a, b):
    if a > 0:
        raise ValueError("Error in f2")
    return a + b


def f1():
    print("start f1")
    s = f2(10, 20)
    print("end f1", s)


print("start")
f1()
print("end")


class CustomException(Exception):
    pass


def fn(*arguments):
    if not all(arguments):
        raise CustomException("False argument in fn")


try:
    fn('dev','',42)
except CustomException as err:
    print("Oops:",err)

