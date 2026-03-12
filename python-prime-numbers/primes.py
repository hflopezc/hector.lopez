def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

with open("results.txt", "w") as f:
    for num in range(1, 251):
        if is_prime(num):
            f.write(str(num) + "\n")


