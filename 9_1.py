# Exercise 1

text1 = set(input())
text2 = set(input())
print(text1.intersection(text2))

# Exercise 2

x = []
y = []
z = []
for i in range (1, 100, 1):
    if i % 3 == 0: x.append(i)
    if i % 5 == 0: y.append(i)
a = set(x)
b = set(y)
c = a.intersection(b)
for i in c:  z.append(i)
print('Числа которые имеют оба множества:', z)
