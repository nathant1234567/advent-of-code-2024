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

            for diff in differences:
                if not (1 <= diff <= 3): 
                    is_increasing = False
                if not (-3 <= diff <= -1): 
                    is_decreasing = False

            if is_increasing or is_decreasing:
                safe_count += 1

    print(safe_count)

if __name__ == "__main__":
    main()
