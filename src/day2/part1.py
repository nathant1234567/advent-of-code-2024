def check_if_safe(input):
        # assume initially that the report is safe
            is_increasing = True
            is_decreasing = True

            # Check each difference manually
            for diff in input:
                if not (1 <= diff <= 3):  # If any difference violates the increasing rule
                    is_increasing = False
                if not (-3 <= diff <= -1):  # If any difference violates the decreasing rule
                    is_decreasing = False

            return is_increasing or is_decreasing

def main():

    safe_count = 0

    with open("day2-data.txt") as file:
        for line in file:
            # convert the line into a list of integers
            levels = list(map(int, line.split()))

            # calculate the differences between consecutive levels
            differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

            # If either increasing or decreasing condition holds, the report is safe
            if check_if_safe(differences):
                safe_count += 1

    print(safe_count)


if __name__ == "__main__":
    main()
