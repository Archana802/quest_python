#5. Print an equi lateral triangle of n lines

number = int(input('enter the number of triangles: ')
    k = number - 1

    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1

        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")

print_triangle(number)
