#squares - NOTE

1.
squares = []
for i in range(10):
  squares.append(i * i)
print('Squares = ', squares)


2.
squares2 = [x**2 for x in range(10)]
print('Squares2 = ', squares2)


3.Using Map and Lambda Function:

squares3 = list(map(lambda x: x**2, range(10)))
print('Squares3 = ', squares3)