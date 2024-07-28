"""Документация для кода ID116180198."""


def decoding_instruction(instruction: str) -> str:
    """Функция для расшифровки строки."""
    stack: list[tuple] = []
    sub_string = repeater = ''
    set_1: set = set('0123456789')
    for liter in instruction:
        if liter in set_1:
            repeater += liter
        elif liter == '[':
            stack.append((sub_string, int(repeater)))
            sub_string = ''
            repeater = ''
        elif liter == ']':
            sub_string_before, repeater_0 = stack.pop()
            sub_string = sub_string_before + sub_string * repeater_0
        else:
            sub_string += liter
    return sub_string


def main() -> None:
    with open("input.txt", "r") as file_in:
        instruction = file_in.readline()     
        result = decoding_instruction(instruction)
    with open("output.txt", "w") as file_out:
        file_out.write(result)           


if __name__ == '__main__':
    main()
    # # item = input().split()
    # # print(is_correct_bracket_seq(item))
    # instruction = '3[a2[c]]'
    # print(decoding_instruction(instruction))