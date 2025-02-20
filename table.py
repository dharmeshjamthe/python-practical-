def print_multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i * j:4}", end=" ")
        print()

if __name__ == "__main__":
    number = int(input("Enter the size of the multiplication table: "))
    print_multiplication_table(number)