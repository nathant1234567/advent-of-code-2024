def if_safe(levels):
    """
    Determine if a report is safe based on its levels.

    Args:
        levels (list): A list of integers representing the levels in the report.

    Returns:
        bool: True if the report is safe, False otherwise.
    """
    # Calculate the differences between consecutive levels
    differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

    # Assume initially that the report is safe
    is_increasing = True
    is_decreasing = True

    # check each difference manually
    for diff in differences:
        if not (1 <= diff <= 3):  # If any difference violates the increasing rule
            is_increasing = False
        if not (-3 <= diff <= -1):  # If any difference violates the decreasing rule
            is_decreasing = False

    # return True if either increasing or decreasing condition holds
    return is_increasing or is_decreasing


def main():
    safe_count = 0

    with open("day2-data.txt") as file:
        for line in file:
            # convert the line into a list of integers
            levels = list(map(int, line.split()))

            # check if the report is safe using the if_safe function
            if if_safe(levels):
                safe_count += 1

    print(safe_count)


if __name__ == "__main__":
    main()
