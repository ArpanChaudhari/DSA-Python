def intToRoman(num: int) -> str:
    roman_map = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}

    multiple = 1
    ans = ""

    while num > 0:
        last_digit = num % 10
        roman = ""

        if last_digit == 4:
            roman = roman_map[multiple] + roman_map[5 * multiple]
        elif last_digit == 9:
            roman = roman_map[multiple] + roman_map[10 * multiple]
        elif last_digit >= 5:
            roman = roman_map[5 * multiple] + roman_map[multiple] * (last_digit - 5)
        else:
            roman = roman_map[multiple] * last_digit

        ans = roman + ans
        multiple *= 10
        num //= 10

    return ans

num = 1994
print(intToRoman(num))  # Output: MCMXCIV