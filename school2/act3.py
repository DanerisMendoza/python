def luhn_algorithm(card_number):
    # Convert the credit card number into a list of integers
    digits = [int(digit) for digit in card_number if digit.isdigit()]

    # Double the value of every other digit from right to left
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    # Calculate the sum of the digits
    total_sum = sum(digits)

    # Check if the result mod 10 is equal to 0
    if total_sum % 10 == 0:
        return "valid"
    else:
        return "invalid"

# Sample test cases
test_cases = [
    "4624748233249080",  # Invalid
    "4624746433239395",  # Valid
    "4624847434639375"   # Valid
]

for test_case in test_cases:
    result = luhn_algorithm(test_case)
    print(f"Input Credit Card number: {test_case}\n{test_case} number is {result}.")
