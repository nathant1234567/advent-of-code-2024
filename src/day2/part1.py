def check_if_safe(input):
        levels = list(map(int, input.split()))

        differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

        # Rule 1
        all_increasing = all(diff > 0 for diff in differences)
        all_decreasing = all(diff < 0 for diff in differences)

        # Rule 2
        valid_differences = all(1 <= abs(diff) <= 3 for diff in differences)

        return (all_increasing or all_decreasing) and valid_differences

def main():

    safe_count = 0

    with open("day2-data.txt") as file:
        for line in file:
            if check_if_safe(line.strip()):
                safe_count += 1

    print(safe_count)


if __name__ == "__main__":
    main()
