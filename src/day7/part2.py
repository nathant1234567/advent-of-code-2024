from itertools import product

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, operator in enumerate(operators):
        if operator == "+":
            result += numbers[i + 1]
        elif operator == "*":
            result *= numbers[i + 1]
        elif operator == "||":
            # Concatenate the current result with the next number
            result = int(str(result) + str(numbers[i + 1]))
    return result

def is_equation_possible(target, numbers):
    # Generate all possible combinations of '+', '*', and '||' for the given numbers
    operator_combinations = product("+*||", repeat=len(numbers) - 1)
    for operators in operator_combinations:
        if evaluate_expression(numbers, operators) == target:
            return True
    return False

def total_calibration_result(input_data):
    total = 0
    for line in input_data.strip().split("\n"):
        # Parse the target and numbers
        target, numbers = line.split(":")
        target = int(target.strip())
        numbers = list(map(int, numbers.strip().split()))
        
        # Check if the equation can produce the target value
        if is_equation_possible(target, numbers):
            total += target
    return total

def main():
    with open("day7-data.txt") as file:
        main_file = file.read()  # Read file content
    
    result = total_calibration_result(main_file)
    print(result)

if __name__ == "__main__":
    main()
