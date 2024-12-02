def main():
    safe_count = 0

    with open("day2-data.txt") as file:
        for line in file:
            # convert the line into a list of integers
            levels = list(map(int, line.split())) # line.split is putting it in a list, map is converting them to strings, list is putting them back into a list.

            # calculate the differences between consecutive levels
            differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

            # assume initially that the report is safe
            is_increasing = True
            is_decreasing = True

            # Check each difference manually
            for diff in differences:
                if not (1 <= diff <= 3):  # If any difference violates the increasing rule
                    is_increasing = False
                if not (-3 <= diff <= -1):  # If any difference violates the decreasing rule
                    is_decreasing = False

            # If either increasing or decreasing condition holds, the report is safe
            if is_increasing or is_decreasing:
                safe_count += 1

    print(safe_count)

if __name__ == "__main__":
    main()
