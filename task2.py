a = 1.44
b = 100
c = 50
d = 25
e = 4
book = d * c * b * e
V = a * 1024 * 1024
Books = int(V // book)
print("Количество книг, помещающихся на дискету:", Books)