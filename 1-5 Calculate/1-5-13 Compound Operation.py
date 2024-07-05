# 2024-7-3 23:21 start, 2024-7-3 23:38 end  @YoCoco2233 Compound Operation
def complex_operation(numbers):
    # Use list derivations and arithmetic operators to calculate all positive sums
    positive_sum = sum(num for num in numbers if num > 0)

    # Calculate the average of all the numbers in the list
    average = sum(numbers) / len(numbers)

    if positive_sum > average:
        # Logical operators are used to combine conditions
        # Let's say we also want to check if there are negative numbers in the list
        has_negatives = any(num < 0 for num in numbers)

        # Bitwise operators may not be directly applicable here, but we can use logical operators to emulate
        # For example, if there are both positive and negative numbers, we may want to mark them specifically
        special_case = has_negatives and positive_sum

        # Returns a tuple containing multiple pieces of information
        return (True, "Positive sum is greater than average.",
                f"Positive Sum: {positive_sum}, Average: {average}",
                "Special case: Both positives and negatives present.") if special_case else \
            (True, "Positive sum is greater than average.",
             f"Positive Sum: {positive_sum}, Average: {average}")
    else:
        # Use conditional expressions (ternary operators) to simplify your code
        return (False, "Positive sum is not greater than average.",
                f"Positive Sum: {positive_sum}, Average: {average}")




numbers = [1, -2, 3, 4, -5, 6]
result = complex_operation(numbers)
print(result)
