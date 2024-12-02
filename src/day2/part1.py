def main():

    safe_count = 0

    with open("day2-data.txt") as file:
        for line in file:
            # converting the line into a list of integers
            levels = list(map(int, line.split()))

            # calculate the differences between consecutive levels
            differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

            # - all differences are between 1 and 3 (increasing), OR
            # - all differences are between -3 and -1 (decreasing)
            if (
                all(1 <= diff <= 3 for diff in differences) or
                all(-3 <= diff <= -1 for diff in differences)
            ):
                safe_count += 1

    #print(safe_count)


if __name__ == "__main__":
    main()
