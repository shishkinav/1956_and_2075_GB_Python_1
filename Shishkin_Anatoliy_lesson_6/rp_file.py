import random


RECORD_LENGTH = 6
LINE_LENGTH = RECORD_LENGTH + len('\n')


def generate_source_file():
    with open('rp_qwerty_3.txt', 'w', encoding='utf-8') as fw:
        for number in range(20):
            n = int(random.random() * 10 ** (RECORD_LENGTH - 1)) / 100
            fw.write(str(n).ljust(RECORD_LENGTH, ' ') + '\n')


def external_solution(number: int, new_result: str):
    if len(new_result) > RECORD_LENGTH:
        print(f"Слишком большое значение '{new_result}', допустима длина в символах {RECORD_LENGTH}")
        return
    with open("rp_qwerty_3.txt", encoding="UTF-8", mode="r+") as file:
        # Так определим последнюю позицию в файле => кол-во записей
        end_of_file = file.seek(0, 2)
        record_position = 0 + (number - 1) * LINE_LENGTH
        if record_position <= end_of_file - LINE_LENGTH:
            file.seek(record_position)
            # file.write(f"{new_result:>5s}\n")
            file.write(f"{new_result:<{RECORD_LENGTH}s}\n")
            # file.write(new_result.ljust(RECORD_LENGTH, ' ') + '\n')
        else:
            print("Некорректное значение строки, в файле не обнаружено")


"""
record_length = 5
# Здесь +2 это из двух символов в конце строки
line_length = record_length + 2
number = int(argv[1])
record_new = argv[2]
"""


def main_1():
    with open('rp_qwerty.txt', 'r+', encoding='utf-8') as f:
        f.seek(0)
        print(f.tell())
        line = f.readline()
        while line:
            print(line.strip(), f.tell(), sep='\n')
            f.write(
                'hello'.ljust(len(line.strip()))
            )
            line = f.readline()


# def main_2():
#     with open('rp_qwerty.txt', 'r+', encoding='utf-8') as fr:
#         # cursor = 0
#         for row in fr.rea:
#             # if len('привет'.ljust(len(row.strip()))) <= len(row.strip()):
#             #     fr.write('привет'.ljust(len(row.strip())) + '\n')
#             # if i == 1:
#             #     line = str.replace(row.strip(), 'привет')
#             #     cursor_2 = cursor
#             #     fw.seek(cursor_2)
#             #     fw.write(f'{line}\n')
#             # cursor = fr.tell()
#             # print(row.strip())


def main_3():
    with open('rp_qwerty.txt', 'r', encoding='utf-8') as fr, open('rp_qwerty.txt', 'w', encoding='utf-8') as fw:
        for row in fr:
            fw.write('привет'.ljust(len(row.strip())) + '\n')


if __name__ == '__main__':
    # main_2()
    generate_source_file()
    external_solution(11, '1.1')
