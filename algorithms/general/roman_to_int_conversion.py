"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.
"""

def roman_to_int(s: str) -> int:
    roman_to_int_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    num = 0
    for i in range(len(s) - 1, -1, -1):
        if i == len(s) - 1:
            num += roman_to_int_map[s[i]]
        else:
            if roman_to_int_map[s[i]] < roman_to_int_map[s[i+1]]:
                num -= roman_to_int_map[s[i]]
            else:
                num += roman_to_int_map[s[i]]
    return num

if __name__ == "__main__":
    print(f"III to integer is {roman_to_int('III')}")
    print(f"LVIII to integer is {roman_to_int('LVIII')}")
    print(f"MCMXCIV to integer is {roman_to_int('MCMXCIV')}")
