def roman_to_number(roman_numeral):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for i in reversed(roman_numeral):
        current_value = roman_numerals[i]
        if current_value < prev_value:
             total -= current_value
        else:
            total += current_value
        prev_value = current_value

    return total
def main():
    roman_numeral_input = input("Enter a Roman numeral: ") #(IX)
    decimal_output = roman_to_number(roman_numeral_input.upper())
    print("Decimal equivalent:", decimal_output)
    
if __name__=="__main__":
    main()
