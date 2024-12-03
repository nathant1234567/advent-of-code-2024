import re

def check_pattern(input):
        pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"

        matches = re.findall(pattern, input)

        total_sum = sum(int(x) * int(y) for x, y in matches)

        return total_sum

def main():

    with open("day3-data.txt") as file:
        content = file.read()
        result = check_pattern(content)

    print(result)


if __name__ == "__main__":
    main()
