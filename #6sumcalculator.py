if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    if n > 0:
        total = 0
        i = 1
        while i <= n:
            total += i
            i += 1
        print(f"The sum of all numbers from 1 to {n} is {total}")
    else:
        print("Please enter a positive integer.")