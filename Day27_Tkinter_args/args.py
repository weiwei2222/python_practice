# height, width是必选参数
def area(height, width):
    return height * width


my_yard = area(5, 2)
print(my_yard)


# height, width里面有默认参数
def area(height=10, width=10):
    return height * width


my_yard = area(5)
print(my_yard)


# 可变参数，参数的数量不定，*args里面是元组
def add(*args):
    print(args)
    for n in args:
        print(n)


add(1, 2, 3)


# 3种参数，必选参数，默认参数，不定参数
def f1(a, b=1, *args):
    print(a, b, args)


f1(17, 2, 3, 5)

# 匿名函数lambda
square = lambda w: w+w
print(square(4))
