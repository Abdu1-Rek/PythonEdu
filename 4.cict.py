for x in range(50):
    for y in range(50):
        b = 5 * 50 ** 7 + 4 * 50 ** 6 + x * 50 ** 5 + 9 * 50 ** 4 + 9 * 50 ** 3 + 7 * 50 ** 2 + y * 50 ** 1 + 2
        if b % 321 == 0:
            print(x*50**1 + y) 