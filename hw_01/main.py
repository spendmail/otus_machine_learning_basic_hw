import math
import re

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
DICTIONARY = {ALPHABET[i]: i for i in range(len(ALPHABET))}


# Returns string from the given integer split up with spaces
def int_to_string(num: int, delimiter=' ') -> str:
    result = ''
    for i in range(len(str(num))):
        result = str(num % 10) + (delimiter if i % 3 == 0 and i != 0 else '') + result
        num //= 10

    return result


# Transforms given text from snake case to camel case
def to_camel_case(snake_str: str) -> str:
    return "".join(x.capitalize() for x in snake_str.lower().split("_"))


# Transforms given text from camel case to snake case
def to_snake_case(camel_str: str) -> str:
    return '_'.join(re.findall('[A-Z][^A-Z]*', camel_str)).lower()


# Swaps given text from camel case to snake case and backwards
def swap_the_case(input_str) -> str:
    return to_snake_case(input_str) if len(input_str) > 0 and input_str[0].isupper() else to_camel_case(input_str)


# Returns either roots of the given equation or None if there were not found
def get_square_equation_roots(equation):
    x = re.search("^([-|+]*)(\d)*x\*\*\d+\s+([-|+]+)\s+(\d*)\*x\s+(\+)\s+(\d+)\s+=\s+\d+$", equation)

    if x is None:
        raise Exception(f'Unable to parse the equation: {equation}')

    a_sign = x.group(1) if x.group(1) != '' else '+'

    a = int(x.group(2)) if x.group(2) is not None else 1
    a = a if a_sign == '+' else a * -1

    ab_sign = x.group(3)
    b = int(x.group(4)) if x.group(4) is not None else 1
    b = b if ab_sign == '+' else b * -1

    bc_sign = x.group(5)
    c = int(x.group(6))
    c = c if bc_sign == '+' else c * -1

    dis = b ** 2 - 4 * a * c

    if dis > 0:
        x1 = (-b + math.sqrt(dis)) / (2 * a)
        x2 = (-b - math.sqrt(dis)) / (2 * a)
        return x1, x2
    elif dis == 0:
        x = -b / (2 * a)
        return x

    return None


# Encodes a given text with a caesar cipher
def caesar_encode_string(source: str, key: int) -> str:
    result = ''
    for char in source:
        char = char.lower()

        if char not in DICTIONARY:
            raise Exception(f'Letter {char} does exist in the dictionary')

        result += ALPHABET[(DICTIONARY[char] + key) % len(ALPHABET)]

    return result


# Decodes a given text with a caesar cipher
def caesar_decode_string(source: str, key: int) -> str:
    result = ''
    for char in source:
        char = char.lower()

        if char not in DICTIONARY:
            raise Exception(f'Letter {char} does exist in the dictionary')

        result += ALPHABET[(DICTIONARY[char] - key) % len(ALPHABET)]

    return result


if __name__ == '__main__':

    first_assignment_data = [1234567890, 267, 34976]
    print("\nFirst assignment:")
    for num in first_assignment_data:
        print(f'given: {num}, result: {int_to_string(num)}')

    second_assignment_data = ['my_first_func', 'AnotherFunction']
    print("\nSecond assignment:")
    for text in second_assignment_data:
        print(f'given: {text}, result: {swap_the_case(text)}')

    third_assignment_data = ['x**2 - 11*x + 28 = 0']
    print("\nThird assignment:")
    for equation in third_assignment_data:
        print(f'given: {equation}; result: {get_square_equation_roots(equation)}')

    fourth_assignment_data = [{'source': 'dog', 'key': 3}, {'source': 'python', 'key': 5}]
    print("\nFourth assignment:")
    for i in range(len(fourth_assignment_data)):
        encoded = caesar_encode_string(fourth_assignment_data[i]['source'], fourth_assignment_data[i]['key'])
        decoded = caesar_decode_string(encoded, fourth_assignment_data[i]['key'])
        print(f"{fourth_assignment_data[i]['source']} -> {encoded} -> {decoded}")
