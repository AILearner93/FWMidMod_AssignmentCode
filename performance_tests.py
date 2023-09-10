import timeit

if __name__ == “__main__”:
    time = timeit.repeat(test_code, number=50000, repeat=5)
    print(time)