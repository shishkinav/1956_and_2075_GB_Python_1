import sys


def main(argv):
    program, *args = argv
    print(f'program = {program}; args = {args}')
    result = sum(map(int, args))
    print(f'Результат: {result}')

    return 0


if __name__ == '__main__':
    print(sys.argv)
    sys.exit(main(sys.argv))

