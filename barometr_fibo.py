def fib(generation):
    if generation < 2:
        return 1
    return fib(generation-2) + fib(generation-1)


def main():
    with open("input.txt", "r") as file_in:
        generation = int(file_in.readline().rstrip())
    result = fib(generation)
    with open("output.txt", "w") as file_out:
        file_out.write(str(result))

if __name__ == '__main__':
    main()

