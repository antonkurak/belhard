number: int = 81
def convert_decimal_to_bin(number:int) -> str:
    bin_number: str = ""
    while number // 2 > 0:
        bin_number += str(number % 2)
        number //= 2
    bin_number += str(number)
    bit_number = bin_number[::-1]
    return bit_number
