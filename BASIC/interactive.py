the_word_is_flat = True;

if the_word_is_flat:
    print('Be careful not to fall off');


squares = [1, 2, 3, 4, 5, 6]
print(squares)

print(squares + [9, 8, 10, 11])

squares.append(12)

squares.append(2 ** 6)

print(squares)


# 与js一样,python直接复制操作的时候,数组不会改变分配的地址,所以rgba改变,rgb也会改变
rgb = ['red', 'green', 'blue']

rgba = rgb
# id函数是用于获得对象的内存地址
print(id(rgba) == id(rgb)) # True 它俩的内存地址一致

rgba.append('pink')

print(rgba)

# 创建一个列表或者序列的副本,复制整个序列
current_rgb = rgba[:]
current_rgb[-1] = 'black'

print(current_rgb)
print(rgba)


letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(letter)

# replace some values
letter[2:5] = ['C', 'D', 'E']
print(letter)

# now remove them
letter[2:5] = []
print(letter)

# clear the list by replacing all the elements with an empty list
letter[:] = []
print(letter)


# 多维数组

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

print(x)


# 用python实现斐波那契数列
w, q = 0, 1
while w < 10:
    print(w)
    w, q = q, q + w