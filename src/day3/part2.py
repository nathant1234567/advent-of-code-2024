import re 

def check_pattern(input):
    # Define the regular expression pattern to match specific instructions
    # The pattern matches either:
    # - 'mul(x,y)' where x and y are integers (1 to 3 digits)
    # - 'do()' 
    # - 'don't()'
    pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
    
    # Use re.findall to find all occurrences of the pattern in the input string
    # It returns a list of tuples with matched groups: 
    # (the entire match, first number, second number) for 'mul', or (the command) for 'do' or 'don't'
    instructions = re.findall(pattern, input)
    print(instructions)

    enabled = True  # Initialize a flag to track whether operations are enabled
    result = 0  # Variable to store the resulting value

    # Loop through all the matched instructions
    for inst in instructions:
        # Match on the first element of the instruction (the entire match)
        match inst[0]:
            case "do()":  # If the instruction is 'do()', enable the operations
                enabled = True
            case "don't()":  # If the instruction is 'don't()', disable the operations
                enabled = False
            case _ if enabled:  # If the operation is enabled and it matches a 'mul' pattern
                # Multiply the first and second number (inst[1] and inst[2]) and add to result
                result += int(inst[1]) * int(inst[2])

    return result

def main():
    with open("day3-data.txt") as file:
        content = file.read()
        result = check_pattern(content)

    print(result)

if __name__ == "__main__":
    main()  
